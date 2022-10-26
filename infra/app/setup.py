import setuptools

with open('../../README.md') as fp:
    long_description = fp.read()

setuptools.setup(
    name='app',
    version='0.0.1',
    description='An empty CDK python app',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Vinay Kiran Bhavanam',
    package_dir={"": "app"},
    packages=setuptools.find_packages(where="app"),
    python_requires='>=3.6',
    classifiers=[
        "Development Status :: 1 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Typing :: Typed"
    ],
)
