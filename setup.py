from setuptools import setup, find_packages

setup(
    name="docstring-generator",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'docgen=cli:main',
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A simple CLI tool to automatically generate Google-style docstrings for Python functions.",
    keywords="docstring, generator, python, ast",
    url="https://github.com/yourusername/docstring-generator",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)