import pandas as pd
from IVF_cycles_analyzer.IVF_func import *
import os


def main(input_file, out_path='IVF_outliers', estimate_baseline=True, OM_rate=0.8, OF_rate=0.8, B_rate_age={18:0.8,50:0.2}, pvalue_th=None):
    ""
    # 1 parse input data and aggregate by patient ID
    df_IVF = pd.read_csv(input_file)
    df_patients = df_IVF.groupby(['Patient_ID', 'Age'])[['COC', 'MII', 'Fertilized', 'Blastocysts']].sum().reset_index()
    # 2 estimate baseline data if not provided
    if estimate_baseline:
        OM_rate, OF_rate, B_rate_age = estimate_baseline_rate(df_patients)
    # 3 compute pvalues
    df_pvalues = compute_pvalues(df_patients, OM_rate, OF_rate, B_rate_age)
    # 4 identify outliers
    df_outliers = find_IVF_outliers(df_pvalues, pvalue_th)
    # 5 output results
    os.makedirs(out_path, exist_ok=True)
    df_pvalues.to_csv(os.path.join(out_path, 'IVF_pvalues.csv'), index=False)
    df_outliers.to_csv(os.path.join(out_path, 'IVF_outliers.csv'), index=False)


if __name__ == '__main__':
    pass


