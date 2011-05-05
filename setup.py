#!/usr/bin/python

from os.path import join
from setuptools import setup, find_packages

name = 'dolmen.app.security'
version = '2.0a1'
readme = open('README.txt').read()
history = open(join('docs', 'HISTORY.txt')).read()

install_requires = [
    'dolmen.security.components',
    'setuptools',
    'zope.i18nmessageid',
    'zope.interface',
    ]

tests_require = [
    'grokcore.security',
    'zope.testing',
    'zope.component',
    ]

setup(name=name, 
      version=version,
      description="Dolmen application security declarations",
      long_description=readme + '\n\n' + history,
      keywords='Dolmen Security',
      author='The Dolmen team',
      author_email='dolmen@list.dolmen-project.org',
      url='http://gitweb.dolmen-project.org',
      license='ZPL',
      packages=find_packages('src', exclude=['ez_setup']),
      package_dir={'': 'src'},
      namespace_packages=['dolmen', 'dolmen.app'],
      include_package_data=True,
      zip_safe=False,
      tests_require = tests_require,
      install_requires = install_requires,
      extras_require = {'test': tests_require},
      classifiers=[
          'Environment :: Web Environment',
          'Programming Language :: Python',
          ],
      )
