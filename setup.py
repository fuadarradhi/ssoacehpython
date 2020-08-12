import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ssoacehpython",
    version="0.1.1",
    author="Fuad Ar-Radhi",
    author_email="fuad.arradhi@gmail.com",
    description="SSO Aceh client for python language",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fuadarradhi/ssoacehpython",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
