import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name='jb_bootcamp',
    version='0.0.1',
    author='Jeesoo Lee',
    author_email='jeesoolee.0318@gmail.com',
    description='Utilities for use in bootcamp.',
    long_description=long_description,
    long_description_content_type='ext/markdown',
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
)