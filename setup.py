from distutils.core import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(name='IVF_extremes',
      version='0.0.7',
      packages=['IVF_extremes','IVF_extremes/test'],
      #py_modules=['main'],
      author='Matteo Figliuzzi',
      author_email='matteo.figliuzzi@igenomix.com',
      install_requires=required,
      entry_points={
        "console_scripts": [
            "IVF_extremes=IVF_extremes.main:CLI_main"
        ]},
      data_files=['data/Sample_IVF_data.csv','requirements.txt']
      )