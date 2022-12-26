# how to upload to PyPI
1. `rm -r dist`
2. `python -m build`
3. `python -m twine upload dist/*`