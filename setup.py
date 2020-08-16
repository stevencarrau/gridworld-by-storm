from setuptools import setup, find_packages
setup(
    name="gridstorm",
    version="0.1",
    packages=find_packages(),
    scripts=[],
    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    #install_requires=["docutils>=0.3"],
    package_data={
        # If any package contains *.nm or *.rst files, include them:
        "": ["*.nm", "*.rst"],
        "gridstorm.models": ["files/*.nm"]
    },
    include_package_data=True,

    # metadata to display on PyPI
    author=["Sebastian Junges"],
    description="This is a benchmark set visualiser for simulating grid worlds with storm.",
    keywords="gridworld storm model-checking",
    install_requires=[
        "stormpy>=1.6.0", "matplotlib"
    ],
)