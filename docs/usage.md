---
hide:
  - navigation
---

# Usage

## Basic

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

## Adding more tokens

You can add more tokens by subclassing the [`Tokens`][pymarkdown_builder.Tokens] class.


```python
from pymarkdown_builder import MarkdownBuilder
from pymarkdown_builder import Tokens as BaseTokens

class Tokens(BaseTokens):
    @staticmethod
    def inline_python(code: str) -> str:
        return f"`#!python {code}`"


t = Tokens

builder = (
    MarkdownBuilder()
    .lines(
        t.h1("pymarkdown-builder"),
        t.inline_python("print('Hello, world!')"),
    )
)

assert builder.document == "# pymarkdown-builder\n\n`#!python print('Hello, world!')`"
```