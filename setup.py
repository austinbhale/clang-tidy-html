# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='clang-html',
    version='1.5.0',
    description='Generates an html file that organizes your clang-tidy log output with the latest clang-tidy checks.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/austinbhale/Clang-Visualizer',
    author='Austin Hale',
    author_email='ah@unc.edu',
    license='MIT License',
    install_requires=[
        "argparse",
        "beautifulsoup4",
        "certifi",
        "lxml",
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    keywords='clang, clang-tidy, html',
    entry_points={
        'console_scripts': [
            'clang-tidy-html=clang_html.clang_visualizer:main',
        ],
    },
    python_requires='>=3.6, <4',
    packages=find_packages()
)
