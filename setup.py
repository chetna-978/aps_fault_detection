from setuptools import  find_packages,setup

setup(
    name="sensor",
    version="0.0.1",
    author="chetna",
    author_email="happychetna5@gmail.com",
    packages= find_packages(),
    install_requires=get_requirements(),
)