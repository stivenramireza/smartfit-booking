from __version__ import __version__

import setuptools

with open('requirements.txt') as f:
    required = f.read().splitlines()

setuptools.setup(
    name="smartfit_booking",
    version=__version__,
    author="Stiven Ramírez Arango",
    author_email="stivenramireza@gmail.com",
    description="Smart Fit gym booking package",
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    install_requires=required
)