from scipy import stats
from scipy.interpolate import interp1d
import logging

def estimate_baseline_rate(df_patients):
    "Estimate baseline rate from input dataframe"
    OM_rate = (df_patients['MII'] / df_patients['COC']).mean()
    OF_rate = (df_patients['Fertilized'] / df_patients['MII']).mean()
    fert_age = df_patients.groupby('Age')['Fertilized'].sum()
    bla_age = df_patients.groupby('Age')['Blastocysts'].sum()
    B_rate_age = ( bla_age / fert_age ).to_dict()
    return OM_rate, OF_rate, B_rate_age


def compute_pvalues(df_protocol, OM_rate, OF_rate, B_rate_age):
    "Perform binomial hypothesis tests to compare individual IVF outcomes with baseline rates"
    for i in range(len(df_protocol)):
        Patient_ID = df_protocol.loc[i, 'Patient_ID']
        n_coc = df_protocol.loc[i, 'COC']
        n_mII = df_protocol.loc[i, 'MII']
        n_fert = df_protocol.loc[i, 'Fertilized']
        n_bla = df_protocol.loc[i, 'Blastocysts']
        age = df_protocol.loc[i, 'Age']
        x = list(B_rate_age.keys())
        y = list(B_rate_age.values())
        func_age = interp1d(x, y, fill_value=(max(y),min(y)),bounds_error=False)
        B_rate = func_age(age)
        p_LMR, p_LFR, p_PDA = IVF_binomial_tests(n_coc, n_mII, n_fert, n_bla, OM_rate, OF_rate, B_rate, Patient_ID)
        df_protocol.loc[i, 'pvalue_LFR'] = p_LFR
        df_protocol.loc[i, 'pvalue_LMR'] = p_LMR
        df_protocol.loc[i, 'pvalue_PDA'] = p_PDA
    return df_protocol


def IVF_binomial_tests(coc, mII, fert, bla, OM_rate, OF_rate, B_rate, Patient_ID=''):
    "Binomial tests to estimate probabilities of IVF outcome"

    try:
        if (coc < mII) | (mII < fert) | (fert < bla):
            logging.warning(
                "Inconsistent IVF values for Patient_ID={}: coc={}, mII={}, fert={}, bla={}".format(Patient_ID, coc,
                                                                                                    mII, fert,bla))
            raise ValueError
        p_LMR = stats.binom_test(x=mII, n=coc, p=OM_rate, alternative='less')
        p_LFR = stats.binom_test(x=fert, n=mII, p=OF_rate, alternative='less')
        p_PDA = stats.binom_test(x=bla, n=fert, p=B_rate, alternative='less')
    except:
        p_LMR, p_LFR, p_PDA = None, None, None

    return p_LMR, p_LFR, p_PDA


def find_IVF_outliers(df_protocol, pvalue_th):
    "Classify individuals as outliers if the pvalue from the binomial test is lower than threshold"
    if pvalue_th is None:
        pvalue_th = 0.05 / df_protocol.shape[1]  # bonferroni correction
    df_protocol['LMR_outlier'] = df_protocol['pvalue_LMR'] < pvalue_th
    df_protocol['LFR_outlier'] = df_protocol['pvalue_LFR'] < pvalue_th
    df_protocol['PDA_outlier'] = df_protocol['pvalue_PDA'] < pvalue_th
    df_outliers = df_protocol[
        (df_protocol['LMR_outlier']) | (df_protocol['LFR_outlier']) | (df_protocol['PDA_outlier'])]
    logging.info('Found the following outliers:\n\nEndophenotype\tNumber of cases\n{}\n'.format(df_outliers[['LMR_outlier','LFR_outlier','PDA_outlier']].sum()))
    return df_outliers[['Patient_ID', 'LMR_outlier', 'LFR_outlier', 'PDA_outlier']]
