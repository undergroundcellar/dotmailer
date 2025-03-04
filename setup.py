from __future__ import absolute_import
from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md')) as f:
    long_description = f.read()

setup(
    name='ucdotmailer',
    version='0.5.0',
    description='DotMailer API wrapper',
    long_description=long_description,

    url='https://github.com/undergroundcellar/dotmailer',

    author='originally Keith M Franklin',
    author_email='test@test.com',

    license='MIT',

    classifiers = [
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7'
    ],

    keywords='python dotmailer api',
    packages=find_packages(exclude=[]),
    install_requires=['peppercorn','simplejson'],


)
