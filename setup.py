import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="snoozingmail",
    version="0.0.1",
    author="Nicolas Knaian",
    author_email="nickknaian@gmail.com",
    description="A minimal python3 wrapper for the Gmail API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nknaian/snoozin",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.8',
)