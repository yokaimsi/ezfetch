from setuptools import setup, find_packages

setup(
    name="ezfetch",
    version="1.0.3",
    description="A clean, Python-based system info tool like Neofetch",
    author="yokaimsi",
    packages=find_packages(),
    install_requires=["psutil"],
    entry_points={
        "console_scripts": [
            "ezfetch = ezfetch.main:display_info"
        ]
    },
)
