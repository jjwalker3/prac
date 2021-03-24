from setuptools import setup, find_packages

VERSION = '0.0.1'
PACKAGE_NAME = 'PRAC'
AUTHOR = 'You'
AUTHOR_EMAIL = 'you@email.com'
URL = 'https://github.com/jjwalker3/prac/'

LICENSE = 'Apache License 2.0'
DESCRIPTION = 'Describe your package in one sentence....NOPE'
LONG_DESCRIPTION = "LONG DESCRIPTION GOES HERE I GUESS"
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = [
    'numpy',
    'pandas',
    'gensim',
]

setup(name=PACKAGE_NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type=LONG_DESC_TYPE,
      author=AUTHOR,
      license=LICENSE,
      author_email=AUTHOR_EMAIL,
      url=URL,
      install_requires=INSTALL_REQUIRES,
      packages=find_packages()
      )