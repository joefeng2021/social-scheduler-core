from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="social-scheduler-core",
    version="0.1.0",
    author="Joe Feng",
    author_email="joefeng2021@gmail.com",
    description="Cross-platform social media scheduler core library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/joefeng2021/social-scheduler-core",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "tweepy>=4.14.0",
        "python-dotenv>=1.0.0",
    ],
)