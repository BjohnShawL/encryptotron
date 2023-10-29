from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()

setup(
    name="encryptotron", version="0.0.1", author="BJS Liddle", author_email="bjohnshawl@gmail.com", license="MIT",
    description="A tool for generating and decrypting cyphers",
    long_description=long_description, long_description_content_type="text/markdown",
    url='https://github.com/BjohnShawL/encryptotron', py_modules=["encryptotron", "app"], packages=find_packages(),
    install_requires=[requirements], python_requires='>3.10', classifiers=[
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ], entry_points='''
        [console_scripts]
        encryptotron=encryptotron:cli
    '''
)