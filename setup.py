# python-pgp A Python OpenPGP implementation
# Copyright (C) 2014 Richard Mitchell
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys

from setuptools import find_packages
from setuptools import setup


PY33 = sys.version_info >= (3, 3)


version = '0.0.1'
long_description = '\n\n'.join([open(f).read() for f in [
    'README.rst',
    'LICENSE.rst',
    'CHANGELOG.rst',
    ]])
requires = [
    'pgpdump3',  # python3 compatible pgpdump
    'python-magic',
    'pycrypto',
    'six',
    'requests',
    'zope.interface',
    ]
tests_require = [
    'coverage',
    'nose',
    'tissue',
    ]
docs_require = [
    'Sphinx',
]
if not PY33:
    tests_require.append('mock')


setup(
    name='pgp',
    version=version,
    description='A Python implementation of OpenPGP',
    long_description=long_description,
    keywords='pgp openpgp gpg cryptography security privacy',
    author='Richard Mitchell',
    author_email='mitch@awesomeco.de',
    url='https://github.com/mitchellrj/python-pgp',
    license='GPL 3',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later ' +
            '(GPLv3+)',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Security :: Cryptography',
        ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    tests_require=tests_require,
    test_suite='nose.collector',
    extras_require={
        # Optional algorithm support
        'camellia': ['camcrypt'],
        'twofish': ['twofish'],

        # Environment shortcuts
        'dev': docs_require + tests_require,
        'docs': docs_require,
        'test': tests_require,
        'integration': ['python-coveralls'] + tests_require,
    },
    entry_points="""
    """,
)
