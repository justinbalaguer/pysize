from setuptools import setup
setup(
  name = 'pysize',
  version = '0.1.0',
  packages = ['pysize'],
  entry_points = {
    'console_scripts': [
      'pysize = pysize.__main__:main'
    ]
  }
)