from setuptools import setup, find_packages

setup(
    name='montecarlo',
    version='1.0.0',
    url='https://github.com/mypackage.git',
    author='Varun Bhatnagar',
    author_email='bhatnagarvarun2020@gmail.com',
    description='Implements a Monte Carlo simulation',
    packages=find_packages(),    
    install_requires=['numpy', 'pandas']
)