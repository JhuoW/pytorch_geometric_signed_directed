from setuptools import find_packages, setup

url = "https://github.com/SherylHYX/pytorch_geometric_signed_directed"
__version__ = (
    subprocess.run(["git", "describe", "--tags"], stdout=subprocess.PIPE)
    .stdout.decode("utf-8")
    .strip()
)
assert "." in _version_

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

install_requires = [
    "torch",
    "torch_sparse",
    "torch_scatter",
    "sklearn",
    "torch_geometric",
    "numpy",
    "scipy"
]

setup_requires = ["pytest-runner"]

tests_require = ["pytest", "pytest-cov", "mock"]

keywords = [
    "machine-learning",
    "deep-learning",
    "deeplearning",
    "deep learning",
    "machine learning",
    "signal processing",
    "signed graph",
    "graph",
    "directed graph",
    "embedding",
    "clustering",
    "graph convolution",
    "graph neural network",
    "representation learning",
    "learning",
]

setup(
    name="torch_geometric_signed_directed",
    packages=find_packages(),
    version=__version__,
    license="MIT",
    description="An Extension Library for PyTorch Geometric on signed and directed networks.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    include_package_data=True,
    author="Yixuan He",
    author_email="He_YX@outlook.com",
    url=url,
    download_url='{}/archive/{}.tar.gz'.format(url, __version__),
    keywords=keywords,
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    python_requires=">=3.6",
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
    ],
)
