import click
import logging
import pandas as pd
from IVF_extremes.IVF_func import *
import os

resources_dir = os.path.join(os.path.dirname(__file__), 'resources')


@click.command()
@click.option('--coc', required=True, type=int, help='number of cocs')
@click.option('--mii', required=True, type=int, help='number of mature oocytes')
@click.option('--fert', required=True, type=int, help='number of fertilized oocytes')
@click.option('--blast', required=True, type=int, help='Number of developed blastocysts')
@click.option('--age', required=True, type=int, help='Age of the woman')
@click.option('--pvalue_th', default=0.05, show_default=True, help='Pvalue threshold for outliers')
def CLI_single_check(coc, mii, fert, blast, age, pvalue_th):
    single_check(coc, mii, fert, blast, age, pvalue_th)

def single_check(num_cocs, num_mature_oocytes, num_fertlized_oocytes, num_blast, age, pvalue_th=0.05):
    """IVF-extremes

    Analyze IVF clinical data and identify phenotypic extremes"""

    logging.basicConfig(filename='IVF_extremes.log', encoding='utf-8', level=logging.DEBUG,filemode='w',format='%(asctime)s %(levelname)s %(message)s')
    logging.getLogger().addHandler(logging.StreamHandler())

    # 1 parse input data and aggregate by patient ID
    logging.info('\n*** IVF_extremes: analysis started\n')
    baseline_rate = pd.read_csv(os.path.join(resources_dir,'baseline_rates.csv'),index_col='Female Age')
    B_rate = baseline_rate['BR'].iloc[age]
    OM_rate = baseline_rate['OMR'].mean()
    OF_rate = baseline_rate['OFR'].mean()
    logging.info('   Baseline Maturation Rate={:.2f},\n   Baseline Fertilization Rate={:.2f},'
                 '\n   Baseline Blastulation Rate={:.2f}\n'.format(OM_rate,OF_rate,B_rate))

    logging.info('*** Computing pvalues...')
    p_LMR, p_LFR, p_PDA = IVF_binomial_tests(num_cocs, num_mature_oocytes, num_fertlized_oocytes, num_blast, OM_rate, OF_rate, B_rate)
    logging.info('   pvalue Low Maturation Rate={:.2E},\n   pvalue Low Fertilization Rate={:.2E},'
                 '\n   pvalue Preimplantation Development Arrest={:.2E}\n'.format(p_LMR,p_LFR,p_PDA))

    # 4 identify outliers
    logging.info('*** Identifying outliers...')
    outlier_LMR = p_LMR < pvalue_th
    outlier_LFR = p_LFR < pvalue_th
    outlier_PDA = p_PDA < pvalue_th
    if (outlier_LFR)|(outlier_LMR)|(outlier_PDA):
        logging.info('   IVF_extremes outcome: Abnormal IVF values')
        logging.info('   Outlier LMR: {}\n   Outlier LFR: {}\n   Outlier PDA: {}\n'.format(outlier_LMR,outlier_LFR,outlier_PDA))
    else:
        logging.info('   IVF_extremes outcome: Normal IVF values\n')

    return


if __name__ == '__single_check__':
    single_check()


