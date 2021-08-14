from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in tcis/__init__.py
from tcis import __version__ as version

setup(
	name='tcis',
	version=version,
	description='Customizations',
	author='Bantoo Accounting',
	author_email='technical@thebantoo.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
