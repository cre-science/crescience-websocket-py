"""
crescience-websocket-py setup.py file
"""
from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\\n" + fh.read()

setup(
    name="crescience_websocket_py",
    version='1.0.0',
    # version='{{VERSION_PLACEHOLDER}}',
    author="Crescience",
    author_email="development@cre.science",
    description="Websocket Client for Crescience devices",
    url = "https://github.com/cre-science/crescience-websocket-py",
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[],
    keywords=['pypi','crescience', 'python'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows"
    ]
)