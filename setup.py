from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in pantaucovid/__init__.py
from pantaucovid import __version__ as version

setup(
	name='pantaucovid',
	version=version,
	description='Aplikasi Pantau Covid',
	author='Sinawardi',
	author_email='punyaibun@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
