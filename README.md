# pymarkdown-builder

> A Markdown document builder with line and span writing modes.

[![PyPI version](https://badge.fury.io/py/pymarkdown-builder.svg)](https://badge.fury.io/py/pymarkdown-builder)
[![Documentation Status](https://readthedocs.org/projects/pymarkdown-builder/badge/?version=latest)](https://pymarkdown-builder.readthedocs.io/en/latest/?badge=latest)
[![CI](https://github.com/demetrius-mp/pymarkdown-builder/actions/workflows/pipeline.yaml/badge.svg)](https://github.com/demetrius-mp/pymarkdown-builder/actions/workflows/pipeline.yaml)
[![codecov](https://codecov.io/gh/demetrius-mp/pymarkdown-builder/branch/main/graph/badge.svg?token=PXK3OH6R8Q)](https://codecov.io/gh/demetrius-mp/pymarkdown-builder)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v0.json)](https://github.com/charliermarsh/ruff)
[![Docstring Style](https://img.shields.io/badge/%20style-google-3666d6.svg)](https://google.github.io/styleguide/pyguide.html#s3.8-comments-and-docstrings)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

## Installation

You can install with `pip`, `poetry`, or any other package manager:

```bash
pip install pymarkdown-builder
```

## Usage

> For more examples, see the [documentation](https://pymarkdown-builder.readthedocs.io/en/latest/usage).

```python
from pymarkdown_builder import MarkdownBuilder
from pymarkdown_builder import Tokens as t


builder = (
    MarkdownBuilder()
    .lines(
        t.h1("pymarkdown-builder"),
        t.quote("A Markdown document builder with line and span writing modes."),
    )
    .br()
    .spans(
        t.p("A paragraph with an "),
        t.link("https://google.com", "inline link"),
        t.p(" and a "),
        t.bold | "bold " | t.italic | "and italic" | t.italic | t.bold,
    )
)

assert builder.document == "# pymarkdown-builder\n\n> A Markdown document builder with line and span writing modes.\n\nA paragraph with an [inline link](https://google.com) and a **bold *and italic***"
```

## License

This project is licensed under the terms of the [GPL-3.0-only license](https://spdx.org/licenses/GPL-3.0-only.html).