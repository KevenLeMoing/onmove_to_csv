from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["ipython>=6", "nbformat>=4", "nbconvert>=5", "requests>=2"]

setup(
    name="pyonmove",
    version="0.0.2",
    author="Keven Le Moing",
    author_email="keven.lemoing@gmail.com",
    description="A package to convert your OnMove activity data into into csv file",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/KevenLeMoing/pyOnMove",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)