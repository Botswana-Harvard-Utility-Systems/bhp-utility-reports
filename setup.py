# -*- coding: utf-8 -*-
import os

from setuptools import find_packages
from setuptools import setup


# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='bhp-utility-reports',
    version='0.1.28',
    author=u'Software Engineering & Data Management',
    author_email='se-dmc@bhp.org.bw',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/covid19-vaccine/esr21',
    license='GPL license, see LICENSE',
    description='bhp utility reports',
    zip_safe=False,
    keywords='django',
    install_requires=[
        'django-cors-headers',
        'django-rest-framework'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
