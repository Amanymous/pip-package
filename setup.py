import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="syccure-validators",
    version="1.0.0",
    description="It is use for Environment Validator",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Amanymous/pip-package",
    author="Muhammad Aman Mirza",
    author_email="aman.mirza358@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["syccure"],
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "syccure=syccure.__main__:Validator",
        ]
    },
)
