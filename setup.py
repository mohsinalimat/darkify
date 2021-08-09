from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in darkify/__init__.py
from darkify import __version__ as version

setup(
	name="darkify",
	version=version,
	description="Switches to dark theme. Stupid.",
	author="Hussain Nagaria",
	author_email="hussain@frappe.cloud",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
