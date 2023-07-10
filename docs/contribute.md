---
hide:
  - navigation
---

# Contribute

In this page you will find information on how to contribute to this package.

## Development environment

This package is developed using primarily [vscode](https://code.visualstudio.com/). You can find configuration files such as recommended extensions and settings in the `.vscode` folder.

The package manager (dependencies/packaging) used for development is [poetry](https://python-poetry.org/). To install poetry, please refer to their [installation docs](https://python-poetry.org/docs/#installation).

With poetry you can install the project with the following command. This will create a virtual environment for the project, and install the package in the new environment, along with the necessary dependencies.

```bash
poetry install
```

With the project installed, you can open a `shell` within the virtual environment with the following command:

```sh
poetry shell
```

## Development workflow

You can run tasks such as tests, formatting, etc. with [poethepoet](https://github.com/nat-n/poethepoet). To see the available tasks, run the following command:

```sh
poe --help
```

!!! note
    The `poe` command only exists within the virtual environment. This means you need to either enter the virtual environment shell, or run the following command:

    ```sh
    poetry run poe test  # poetry run poe task-name
    ```

    Check out [poetry run](https://python-poetry.org/docs/cli#run) docs.

The most important tasks are `test` and `lint-fmt`. The first one runs the test suite, and the second one will lint and format the code, and also format the `pyproject.toml` file.

To run the test suite, use the following command:

```sh
poe test
```

To lint and format the code, use the following command:

```sh
poe format
```