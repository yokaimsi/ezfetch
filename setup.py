from setuptools import setup, find_packages

setup(
    name="ezfetch",
    version="1.0.6",
    description="A fast, cross-platform terminal system info tool written in Python (like neofetch)",
    version="1.0.5",
    description="A minimal yet powerful system information tool",
    author="yokaimsi",
    author_email="contact.now.itachi@gmail.com",
    packages=find_packages(),
    install_requires=["psutil"],
    entry_points={
        "console_scripts": [
            "ezfetch=ezfetch.main:display_info",
        ],
    },
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
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
