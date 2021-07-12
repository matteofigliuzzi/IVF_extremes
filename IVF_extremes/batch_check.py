import pandas as pd
import click
import logging
from IVF_extremes.IVF_func import *
import os



@click.command()
@click.option('-i','--input_file', required=True,help='Path to the input file.')
@click.option('-o','--out_path', required = False, default='out_IVF', show_default=True, help='Path to the input file.')
@click.option('-e','--estimate-baseline', is_flag=True, show_default=True, help='Estimate IVF baseline rates from input dataset')
@click.option('--om_rate', default=0.8, show_default=True, help='Baseline Oocyte Maturation Rate')
@click.option('--of_rate', default=0.8, show_default=True, help='Baseline Oocyte Fertilization Rate')
@click.option('--blast_rate', default=0.6, show_default=True, help='Baseline Blastocyst Production Rate')
@click.option('--pvalue_th', help='Pvalue threshold for outliers')
def CLI_batch(input_file, out_path='output_IVF_extremes', estimate_baseline=False, om_rate=0.8, of_rate=0.8, blast_rate=0.6, pvalue_th=None):
    batch_check(input_file, out_path, estimate_baseline, om_rate, of_rate, blast_rate, pvalue_th)

def batch_check(input_file, out_path='output_IVF_extremes', estimate_baseline=False, om_rate=0.8, of_rate=0.8, blast_rate=0.6, pvalue_th=None):
    """IVF-extremes

    Analyze IVF clinical data and identify phenotypic extremes"""

    os.makedirs(out_path, exist_ok=True)
    logging.basicConfig(filename=os.path.join(out_path,'IVF_extremes.log'), encoding='utf-8', level=logging.DEBUG,filemode='w',format='%(asctime)s %(levelname)s %(message)s')
    logging.getLogger().addHandler(logging.StreamHandler())

    # 1 parse input data and aggregate by patient ID
    logging.info('IVF_extremes: analysis started')
    logging.info('Parsing input data')
    df_IVF = pd.read_csv(input_file)
    df_patients = df_IVF.groupby(['Patient_ID', 'Age'])[['COC', 'MII', 'Fertilized', 'Blastocysts']].sum().reset_index()
    # 2 estimate baseline data if not provided
    if estimate_baseline:
        logging.info('Estimating baseline from input dataset')
        OM_rate, OF_rate, B_rate_age = estimate_baseline_rate(df_patients)
    else:
        logging.info('Fixing baseline with custom values')
        OM_rate, OF_rate = (om_rate,of_rate)
        B_rate_age = {0:blast_rate,100:blast_rate}
    # 3 compute pvalues
    logging.info('Computing pvalues')
    df_pvalues = compute_pvalues(df_patients, OM_rate, OF_rate, B_rate_age)
    # 4 identify outliers
    logging.info('Identifying outliers')
    df_outliers = find_IVF_outliers(df_pvalues, pvalue_th)
    # 5 output results
    logging.info('Exporting results to {} folder'.format(out_path))
    df_pvalues.to_csv(os.path.join(out_path, 'IVF_pvalues.csv'), index=False)
    df_outliers.to_csv(os.path.join(out_path, 'IVF_outliers.csv'), index=False)

    return df_outliers


if __name__ == '__batch_check__':
    batch_check()


