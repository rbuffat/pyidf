from setuptools import setup
from pyidf import __version__

setup(name='pyidf',
      version=__version__,
      description='Python library to read, modify and create EnergyPlus idf files',
      url='https://github.com/rbuffat/pyidf',
      download_url='https://github.com/rbuffat/pyidf/tarball/{}'.format(__version__),
      author='Rene Buffat',
      author_email='buffat@gmail.com',
      license='Apache License 2.0',
      classifiers=['Development Status :: 3 - Alpha'],
      packages=['pyidf'],
      keywords=['EnergyPlus', 'IDF'])
