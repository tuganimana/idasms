import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Idasms", # Replace with your own username
    version="0.0.1",
    author="Telesphore Tuganimana",
    author_email="telesphore@idatech.rw",
    description="A package that allow you to send a bulk sms in all countries",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tuganimana/idasms",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    
    install_requires=['PyYAML'],
    zip_safe=False
)