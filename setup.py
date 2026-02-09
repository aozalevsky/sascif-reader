# Copyright (C) 2014-2015 European Molecular Biology Laboratory (EMBL)
#
# EMBL licenses this file to you under the Apache License,
# Version 2.0 ("the License"); you may not use this file
# except in compliance with the License.
# You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.


from setuptools import setup

setup(
    name='sasciftools',
    version='3.0.0',
    description='Package for reading and writing files in sascif format',
    url='https://git.embl.de/grp-svergun/sasciftools3',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        # Licence is "Apache License, Version 2.0" but the PyPI classifers
        # do not give a way to distinguish versions of the Apache License
        # https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
    packages=[
        'sasciftools',
        'sasciftools.mmCif',
    ],
)
