# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

readme = ''

setup(
    long_description=readme,
    name='kantorotanium',
    version='0.0.1',
    description='Eve Online: optimize compressed ore purchases',
    python_requires='==3.*,>=3.7.0',
    author='Chris Danis',
    author_email='cdanis@gmail.com',
    entry_points={
        "console_scripts": ["kantorotanium = kantorotanium.__main__:main"]
    },
    packages=['kantorotanium'],
    package_dir={"": "."},
    package_data={},
    install_requires=[],
    extras_require={
        "dev": [
            "dataclasses-json==0.*,>=0.5.1", "logzero==1.*,>=1.5.0",
            "ortools==7.*,>=7.6.0", "pytest==4.*,>=4.6.0",
            "requests==2.*,>=2.0.0"
        ]
    },
)
