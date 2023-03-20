from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in donation_coupon_system/__init__.py
from donation_coupon_system import __version__ as version

setup(
	name="donation_coupon_system",
	version=version,
	description="Donation Coupon System Allows to collect donations via Coupon books from diffrent collection areas.",
	author="Venture Force Global Inc",
	author_email="shahrukh@telniasoft.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
