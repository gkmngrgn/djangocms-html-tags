# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from djangocms_html_tags import __version__


setup(
    name='djangocms-html-tags',
    version=__version__,
    description=open('README.rst').read(),
    author='Gokmen Gorgen',
    author_email='gokmen@alageek.com',
    packages=find_packages(),
    platforms=['OS Independent'],
    install_requires=[],
    include_package_data=True,
    zip_safe=False,
)
