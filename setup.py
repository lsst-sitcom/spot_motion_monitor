#!/usr/bin/env python
import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()
doclink = """
Documentation
-------------

The full documentation is at http://spot_motion_monitor.rtfd.org."""
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = [
    "numpy",
    "PyQt5",
    "scipy"
]

test_requirements = [
    "wheel>=0.22",
    "bumpversion",
    "flake8",
    "tox",
    "coverage",
    "Sphinx",
    "cryptography",
    "PyYAML"
]

setup(
    name='spot_motion_monitor',
    version='0.1.0',
    description='User interface for Dome Seeing Monitor.',
    long_description=readme + '\n\n' + doclink + '\n\n' + history,
    author='Michael Reuter',
    author_email='mareuter@lsst.org',
    url='https://github.com/lsst-com/spot_motion_monitor',
    packages=[
        'spot_motion_monitor',
    ],
    package_dir={'spot_motion_monitor': 'spot_motion_monitor'},
    include_package_data=True,
    install_requires=requirements,
    license='MIT',
    zip_safe=False,
    keywords='spot_motion_monitor',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements

)
