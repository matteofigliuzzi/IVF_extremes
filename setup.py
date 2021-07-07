from distutils.core import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(name='IVF_extremes',
      version='0.1',
      packages=['IVF_extremes'],
      #py_modules=['main'],
      author='Matteo Figliuzzi',
      author_email='matteo.figliuzzi@igenomix.com',
      install_requires=required
      )