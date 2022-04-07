"""Install lra package."""
import os
import setuptools


# Read in requirements
with open(os.path.join(os.path.dirname(__file__), 'requirements.txt')) as f:
  requirements = [r.strip() for r in f]

setuptools.setup(
    name='lra',
    version='0.0.2',
    license='Apache 2.0',
    install_requires=requirements,
    url='https://github.com/google-research/long-range-arena/',
    packages=setuptools.find_packages(),
    python_requires='>=3.7')
