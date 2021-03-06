from os import path
from setuptools import setup, find_packages
import sys
import versioneer


# NOTE: This file must remain Python 2 compatible for the foreseeable future,
# to ensure that we error out properly for people with outdated setuptools
# and/or pip.
min_version = (3, 6)
if sys.version_info < min_version:
    error = """
jem does not support Python {0}.{1}.
Python {2}.{3} and above is required. Check your Python version like so:

python3 --version

This may be due to an out-of-date pip. Make sure you have pip >= 9.0.1.
Upgrade pip like so:

pip install --upgrade pip
""".format(
        *sys.version_info[:2], *min_version
    )
    sys.exit(error)

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.rst"), encoding="utf-8") as readme_file:
    readme = readme_file.read()

with open(path.join(here, "requirements.txt")) as requirements_file:
    # Parse requirements.txt, ignoring any commented-out lines.
    requirements = [
        line
        for line in requirements_file.read().splitlines()
        if not line.startswith("#")
    ]


setup(
    name="jem",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="Python package for MRI and electrophysiology analysis.",
    long_description=readme,
    author="Inati Lab, NINDS, NIH",
    author_email="souheil.inati@gmail.com",
    url="https://github.com/inatilab/jem",
    packages=find_packages(exclude=["docs", "tests"]),
    entry_points={
        "console_scripts": [
            # 'some.module:some_function',
            "contrast_normalization=jem.cli:contrast_normalization",
            "coil_correction=jem.cli:coil_correction",
            "laplacian_pyramid=jem.cli:compute_laplacian_pyramid",
            "riff=jem.cli:compute_riff",
        ]
    },
    include_package_data=True,
    package_data={
        "jem": [
            # When adding files here, remember to update MANIFEST.in as well,
            # or else they will not be included in the distribution on PyPI!
            # 'path/to/data_file',
        ]
    },
    install_requires=requirements,
    license="Public Domain",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
    ],
)
