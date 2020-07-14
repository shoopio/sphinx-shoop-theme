# -*- coding: utf-8 -*-
"""`sphinx_shuup_theme` lives on `Github`_.

.. _github: https://github.com/rtfd/sphinx_shuup_theme

"""

import os
import subprocess
import distutils.cmd
import setuptools.command.build_py
from io import open
from setuptools import setup


class WebpackBuildCommand(setuptools.command.build_py.build_py):

    """Prefix Python build with Webpack asset build"""

    def run(self):
        if not 'CI' in os.environ and not 'TOX_ENV_NAME' in os.environ:
            subprocess.run(['npm', 'install'], check=True)
            subprocess.run(['node_modules/.bin/webpack', '--config', 'webpack.prod.js'], check=True)
        setuptools.command.build_py.build_py.run(self)


class WebpackDevelopCommand(distutils.cmd.Command):

    description = "Run Webpack dev server"

    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        subprocess.run(
            ["node_modules/.bin/webpack-dev-server", "--open", "--config", "webpack.dev.js"],
            check=True
        )


setup(
    name='sphinx_shuup_theme',
    version='0.6.0',
    url='https://github.com/rtfd/sphinx_shuup_theme/',
    license='MIT',
    author='Shoop Ltd (original by Dave Snider)',
    description='Sphinx Theme for Shoop',
    long_description=open('README.rst', encoding='utf-8').read(),
    cmdclass={
        'build_py': WebpackBuildCommand,
        'watch': WebpackDevelopCommand,
    },
    zip_safe=False,
    packages=['sphinx_shuup_theme'],
    package_data={'sphinx_shuup_theme': [
        'theme.conf',
        '*.html',
        'static/css/*.css',
        'static/css/fonts/*.*'
        'static/js/*.js',
    ]},
    include_package_data=True,
    # See http://www.sphinx-doc.org/en/stable/theming.html#distribute-your-theme-as-a-python-package
    entry_points = {
        'sphinx.html_themes': [
            'sphinx_shuup_theme = sphinx_shuup_theme',
        ]
    },
    install_requires=[
        'sphinx'
    ],
    tests_require=[
        'pytest',
    ],
    extras_require={
        'dev': [
            'transifex-client',
            'sphinxcontrib-httpdomain',
            'bump2version',
        ],
    },
    classifiers=[
        'Framework :: Sphinx',
        'Framework :: Sphinx :: Theme',
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Customers',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
    ],
)
