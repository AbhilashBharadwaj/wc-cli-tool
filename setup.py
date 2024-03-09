from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-16") as fh:
    requirements = fh.read()
setup(
    name="wordcount-cli-tool",
    version="0.0.1",
    author="Abhilash Sampath",
    author_email="iamabhilashsampath@gmail.com",
    license="MIT",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    homepage="https://github.com/AbhilashBharadwaj/wc-cli-tool/",
    py_modules=["word_count", "app"],
    packages=find_packages(),
    install_requires=[requirements],
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    entry_points="""
        [console_scripts]
        ccwc=word_count:count_file_details
    """,
)
