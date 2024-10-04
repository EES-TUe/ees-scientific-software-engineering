# ees-scientific-software-engineering

This is a training project for Scientific Software Engineering for EES group.


## Installation

In a Python environment, in the root of the repository, install it in develop mode using the command below.

**NOTE: you need to re-run the following command everytime you add new (optional) dependencies!**

```shell
pip install -e .[dev,example]
```

After installation, run the test.

```shell
pytest
```

## Code style and quality check

You can run the following two commands to automatically format your code style.

```shell
isort .
black .
```

You can run the following command to check the code quality.
It will return errors if the quality check fails.
You need to read the errors and make required adjustments.

```shell
pylint ees_scientific_software_engineering 
```

## Folder structure of the repository

The folder structure of the repository is explained as below.


* [`src/ees_scientific_software_engineering `](./src/ees_scientific_software_engineering) is the main folder of the package. You should put your new functionality code there.
* [`tests`](./tests) is the folder containing the test files. You should put your test code there.
* [`.vscode`](./.vscode) contains the setting file for the IDE VSCode.
* [`.github/workflows`](./.github/workflows) contains the continuous integration (CI) configurations.
