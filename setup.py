from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in social_studio/__init__.py
from social_studio import __version__ as version

setup(
	name="social_studio",
	version=version,
	description="social studio customization",
	author="techwizards",
	author_email="suraj@techwizards.io",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
