import setuptools

description = "API wrapper for img-api"
#long_description = open("README.md").read()
version = "1.0.0"

packages = ["imgapi"]

setuptools.setup(
    name="imgapi",
    version=version,
    description=description,
    #long_description=long_description,
    url="https://github.com/pollen5/img-api.py",
    author="PoLLeN",
    author_email="itsladybug5852@gmail.com",
    license="MIT",
    packages=packages,
    include_package_data=True,
    install_requires=["aiohttp>=2.0.0"]
)
