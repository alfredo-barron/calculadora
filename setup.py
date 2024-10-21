from setuptools import setup, find_packages

setup(
    name='proyecto',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas'
    ],
    entry_points={
        'console_scripts': [
            'proyecto=proyecto.modulo1:main',
        ],
    },
)
