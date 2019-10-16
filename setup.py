from setuptools import find_packages, setup

setup(
    name="ffile",
    version="2.0.0",
    description="F-strings for a whole file.",
    author="Matthew Sochor",
    author_email="matthew.sochor@gmail.com",
    url="https://github.com/matthew-sochor/ffile",
    download_url="https://github.com/matthew-sochor/ffile",
    license="MIT",
    tests_require=["pytest", "pyyaml", "json"],
    python_requires=">=3.6",
    entry_points={"console_scripts": ["ffile = ffile.ffile:cli"]},
    packages=find_packages(),
)
