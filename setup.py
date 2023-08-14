from setuptools import setup, find_packages

__version__ = "1.0"

setup(
    name="python-geodb-cities",
    version=__version__,
    author="Oleh Baran",
    author_email="lolikktra@gmail.com",
    url="https://github.com/lolikktra/python-geodb-cities.git",
    packages=find_packages(),
    dependencies=["requests",
                  "pytest",
                  "requests-mock"],
    description="Python API Wrapper for Geo DB Cities",
    license="Unlicense",
    keywords=["api", "geo", "geodb", "cities"],
    install_requires=["requests"],
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
)
