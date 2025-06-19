from setuptools import setup, find_packages

setup(
    name="ezfetch",
    version="1.0.0",
    description="A clean, Python-based system info tool like Neofetch",
    author="Your Name",
    packages=find_packages(),
    install_requires=["psutil"],
    entry_points={
        "console_scripts": [
            "ezfetch = ezfetch.main:display_info"
        ]
    },
)
