#from distutils.core import setup
from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(name='IVF_extremes',
      version='0.0.14',
      #packages=['IVF_extremes','IVF_extremes/test'],
      packages = find_packages(),
      package_data = {'': ['*.csv']},
      author='Matteo Figliuzzi',
      author_email='matteo.figliuzzi@igenomix.com',
      install_requires=required,
      entry_points={
        "console_scripts": [
            "IVF_extremes_batch=IVF_extremes.batch_check:CLI_batch",
            "IVF_extremes=IVF_extremes.single_check:CLI_single_check",
        ]},
      data_files=['data/Sample_IVF_data.csv','requirements.txt','IVF_extremes/resources/baseline_rates.csv']
      )