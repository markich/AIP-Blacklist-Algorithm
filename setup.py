"""
GNU GENERAL PUBLIC LICENSE
Version 3, 29 June 2007
Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
Everyone is permitted to copy and distribute verbatim copies
of this license document, but changing it is not allowed.
"""
#! /usr/local/bin/python3

from setuptools import setup, find_packages

# read version
version_globals = {}
with open("version.py") as fp:
    exec(fp.read(), version_globals)
version = version_globals['__version__']

setup(
    name='AIP',
    packages=find_packages(exclude=("tests",)),
    version=version,
    author='Stratosphere IPS',
    author_email='stratosphere@aic.fel.cvut.cz',
    url='https://github.com/stratosphereips/AIP-Blocklist-Algorithm',
    download_url=f"https://github.com/stratosphereips/AIP-Blocklist-Algorithm/tarball/{version}",
    description='The Attacker IP Prioritizer (AIP) algorithm is a IPv4 address blocklist generator.',
    license='GPL-3.0 License',
    install_requires=['netaddr',
                      'maxminddb'
                      ],
    include_package_data=True
)
