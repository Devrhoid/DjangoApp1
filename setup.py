import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__),'README.rst')).read()

#Allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__),os.pardir)))

setup(
	name='django-polls',
	version='0.1',
	packages=['polls'],
	include_package_data=True,
	license='BSD License', # example license
	description='A simple Django app to conduct to conduct Web-based polls.',
	long_description=README,
	url='http://www.example.com/',
	author='Derhoid',
	author_email='devrhoid.davis@gmail.com',
	classifiers=[
		'Enviroment :: Web Environement',
		'Framework  :: Django',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: BSD License', #example license
		'Operating System :: OS Independent',
		'Programming Language :: Python',
		'Programming Language :: Python :: 2.6',
		'Programming Language :: Python :: 2.7',
		'Topic :: Internet :: WWW/HTTP',
		'Topic :: Internet :: WWW/HTTP :: Dynamic COntent',
		],
   )
