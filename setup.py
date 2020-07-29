from setuptools import setup

def long_description():
    with open("README.md", "r") as f:
        return f.read()

setup(
    name="fcgf",
    version=0.1,
    license="MIT",
    description="Fully Convolutional Geometric Features",
    long_description=long_description(),
    long_description_content_type="text/markdown",
    install_requires=["torch", "MinkowskiEngine"],
    author="Christopher Choy",
    url="https://github.com/SergioRAgostinho/fcgf",
    py_modules=["fcgf"],
    python_requires=">=3.6",
)