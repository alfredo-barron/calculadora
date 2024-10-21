from setuptools import setup, find_packages

setup(
    name='calculadora',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas'
    ],
    entry_points={
        'console_scripts': [
            'calculadora=calculadora.modulo1:main',
        ],
    },
)
