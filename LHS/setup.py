from setuptools import setup, find_packages

setup(
    name="signal_ICT_AadilAdmani_92510133026",  # Your package name
    version="0.1",  # Initial version
    packages=find_packages(),  # Automatically find all packages
    install_requires=[  # Dependencies
        'numpy',
        'matplotlib',
    ],
    description="A Python package for generating and manipulating signals",
    author="Aadil Admani",
    author_email="aadil@example.com",  # Replace with your email
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Python version requirement
)
