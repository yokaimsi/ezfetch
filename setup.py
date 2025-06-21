from setuptools import setup, find_packages

setup(
    name="ezfetch",
    version="1.0.5",
    description="A minimal yet powerful system information tool",
    author="yokaimsi",
    packages=find_packages(),
    install_requires=["psutil"],
    entry_points={
        'console_scripts': [
            'ezfetch=ezfetch.main:display_info',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
