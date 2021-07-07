from distutils.core import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(name='IVF_outlier_detector',
      version='1.0',
      packages=['IVF_cycles_analyzer'],
      py_modules=['main'],
      author='Matteo Figliuzzi',
      author_email='matteo.figliuzzi@igenomix.com',
      install_requires=required
      )