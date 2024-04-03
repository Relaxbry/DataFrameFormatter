from setuptools import setup, find_packages

setup(
    name='dataframe_formatter',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'fuzzywuzzy',
    ],
    author='Bry',
    author_email='ortiz9p@me.com',
    description='A Python package for formatting DataFrame columns.',
    url='https://github.com/relaxbry/dataframe_formatter',
)