# clang-html
A visualizer for LLVM's linting tool: clang-tidy.

## Getting Started with pip 
![test](https://static.pepy.tech/personalized-badge/clang-html?period=total&units=international_system&left_color=black&right_color=blue&left_text=Downloads)

Install it:
```
python -m pip install clang-html
```
In your shell:
```
# Call it as python module
python -m clang_html [logfile.log] [-o clang.html]

# Call it directly
clang-tidy-html [logfile.log] [-o clang.html]
```

In your python terminal:
```
>>> from pathlib import Path
>>> from clang_html import clang_tidy_visualizer

>>> clang_tidy_visualizer(Path("examples/sample.log"))
2021-04-23 12:30:40,619 - clang_html.clang_visualizer -     INFO - Writing results to clang.html
```

### Libraries
- [argparse](https://pypi.org/project/argparse/)
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
- [certifi](https://pypi.org/project/certifi/)
- [lxml](https://pypi.org/project/lxml/)

### Prerequisites

Install [Clang-Tidy](http://clang.llvm.org/extra/clang-tidy/) to use for your C/C++ source files.

On your local Linux machine, installation is as easy as:

```
sudo apt install clang-tidy
```

You will need bash or some other terminal to execute the script. Download Python 3 or higher [here](https://www.python.org/downloads/).

When running clang-tidy on your files, be sure to pipe it into a new log file of checks:

```
clang-tidy -checks=* [filename.c] | tee [newfile.log]
```

If you are receiving the following error:

> Error while trying to load a compilation database:
> Could not auto-detect compilation database for file "your_file.c"
> No compilation database found in /your/directory or any parent directory

Create a simple json file to be compiled into your project documented [here](http://clang.llvm.org/docs/JSONCompilationDatabase.html).

## Running the script locally

Clone or fork this repository to run the script on your native system.

The script takes in one file argument of a txt or log file with your outputted clang-tidy checks.

```
python -m clang_html [newfile.log] [-o clang.html]
```

## Example Output

Inside the same directory as clang_visualizer.py, you will find a new html file called 'clang.html'.

You can also specify your custom file name when calling the script with `[-o, --out] other_name.html` or `clang_tidy_visualizer(Path("sample.log"), Path("clang.html"))`.

An example html output can be found [here](https://austinbhale.com/Clang-Visualizer/examples/clang.html).

The highlighting functionality uses your local session storage, which will save your changes on exit.

## Contributing

Feel free to create a pull request for any updates or fixes to this repository.

## Versioning

This repository uses [LLVM Clang](http://clang.llvm.org/extra/clang-tidy/index.html) for versioning. All checks confirmed for version 6.0-10.0+. Earlier versions should have support for the vast majority of checks. Later versions update based on the information presented on LLVM's official [checks list](http://clang.llvm.org/extra/clang-tidy/checks/list.html).

## Authors

- **Austin Hale**

See also the list of [contributors](https://github.com/austinbhale/Clang-Visualizer/graphs/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/austinbhale/Clang-Visualizer/LICENSE) file for details.
