#!/usr/bin/env python
"""Aether Project, Alphagriffin.com.
Eric Petersen @Ruckusist <eric.alphagriffin@gmail.com>
"""

from setuptools import setup, find_packages
from codecs import open
from os import path

if __name__ == '__main__':
    # long_description breaks out of DIR installs!
    setup(

        name='Aether_Project',
        version='0.0.1',
        license='AG',  # FIXME

        namespace_packages=['ag'],  # home for Alpha Griffin libraries
        packages=find_packages(exclude=['tests']),

        author='Ruckusist @ Alpha Griffin',
        author_email='ruckusist@alphagriffin.com',

        description='Crypto Currency Manager.',

        long_description=open('README.rst').read(),
        url='http://github.com/AlphaGriffin/Aether',

        # @see https://pypi.python.org/pypi?%3Aaction=list_classifiers
        classifiers=[
            'Development Status :: 3 - Alpha',
            "Environment :: Console",
            "Environment :: Console :: Curses",
            'Intended Audience :: Developers',
            "Operating System :: POSIX",
            "Operating System :: Unix",
            "Operating System :: MacOS :: MacOS X",
            'Natural Language :: English',
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.2",
            "Programming Language :: Python :: 3.3",
            "Programming Language :: Python :: 3.4",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: Implementation :: PyPy",
            'Topic :: System :: Installation/Setup',
            'Topic :: Utilities'
        ],

        # space-separated list of keywords
        keywords='alphagriffin tensorflow utilities curses ui user interface text',
        platforms="unix-like",

        install_requires=['numpy',
                          'redis',
                          ],

        extras_require={
        },

        package_data={
        },

        data_files=[],

        entry_points={
            'console_scripts': [
                'Aether = ag.Aether.__main__:main'
            ]
        },
        test_suite='nose.collector',
        tests_require=['nose'],
    )
