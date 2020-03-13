import os
from distutils.core import setup


with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='CIP Project Team 10',
    version="0.0.1",
    url='https://github.com/highproformas/CIP-10',
    license='FREE',
    author="Niclas Simmler, Pascal Himmelberger, Silvan Leibacher",
    author_email="niclas.simmler@stud.hslu.ch, pascal.himmelberger@stud.hslu.ch, silvan.leibacher@stud.hslu.ch",
    description='Code for the CIP Project @ HSLU FS 2020',
    long_description="Code for the CIP Project @ HSLU FS 2020",
    platforms='any',
    install_requires=required
)
