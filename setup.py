try: 
    from setuptools import setup 
except ImportError: 
    from distutils.core import setup 
import sys 

pkgdir = {'': 'python%s' % sys.version_info[0]}
VERSION = '0.1'

setup(name='cognitive_luis',
      version=VERSION,
      description='LUIS SDK for python',
      url='https://github.com/Microsoft/Cognitive-LUIS-Python',
      author='Ahmed El-Hinidy',
      author_email='t-ahelhi@microsoft.com',
      license='MIT',
	  package_dir=pkgdir,
      packages=['luis_sdk'],
      zip_safe=False
)