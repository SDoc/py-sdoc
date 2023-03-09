from codecs import open
from os import path

from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='SDoc',

    version='1.0.0',

    description='A super format documentation document preparation system for SAAS and multi tenant applications',
    long_description=long_description,

    url='https://github.com/SDoc/py-sdoc',

    author='Set Based IT Consultancy',
    author_email='info@setbased.nl',

    license='MIT',

    classifiers=[
        'Development Status :: 4 - Beta',

        'Environment :: Console',

        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',

        'License :: OSI Approved :: MIT License',

        'Operating System :: OS Independent',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: PyPy',

        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
        'Topic :: Text Editors :: Documentation',
    ],

    keywords='Documentation, SAAS',

    packages=find_packages(exclude=['build', 'test']),

    install_requires=['antlr4-python3-runtime==4.12.*',
                      'cleo~=2.0.0',
                      'httplib2~=0.21.0'],

    entry_points={
        'console_scripts': [
            'sdoc = sdoc:main',
        ],
    }
)
