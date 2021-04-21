import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='clang-html',
    version='1.3.3',    
    description='Generates an html file that organizes your clang-tidy log output with the latest clang-tidy checks.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/austinbhale/Clang-Visualizer',
    author='Austin Hale',
    author_email='ah@unc.edu',
    license='MIT License',
    install_requires=[
        "argparse",
        "beautifulsoup4"   
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)