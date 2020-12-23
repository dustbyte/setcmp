from setuptools import setup, find_packages

def readme_content():
    with open('README.md') as handle:
        return handle.read()

setup(
    name="setcmp",
    version="1.0",
    author="Pierre Wacrenier",
    license="MIT",
    author_email="pierre@wacrenier.com",
    description="Perform set operation on list of items",
    long_description=readme_content(),
    url="https://github.com/mota/setcmp",
    packages=find_packages(),

    entry_points={
        "console_scripts": [
            "setcmp=setcmp.main:main"
        ]
    }
)
