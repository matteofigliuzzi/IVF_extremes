#!/bin/sh

pip install twine
rm -r dist
python setup.py sdist

#pypi test
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
pip install --index-url https://test.pypi.org/simple/ IVF_extremes==0.0.3

#pypi
twine upload dist/*
pip install IVF_extremes==0.0.3