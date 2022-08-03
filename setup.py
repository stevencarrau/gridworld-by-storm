from setuptools import setup, find_packages
setup(
    name="gridfull",
    version="0.1",
    packages=find_packages(),
    scripts=[],
    package_data={
        # If any package contains *.nm or *.rst files, include them:
        "": ["*.rst"],
        "gridfull.models": ["files/*.nm"]
    },
    include_package_data=True,

    # metadata to display on PyPI
    author=["Sebastian Junges"],
    description="This is a benchmark set visualiser for simulating grid worlds with storm.",
    keywords="gridworld storm model-checking",
    install_requires=[
        "stormpy>=1.6.0", "matplotlib", "tqdm"
    ],
)
