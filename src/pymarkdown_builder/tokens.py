"""Markdown tokens. These are the building blocks of a markdown document."""

from typing import Dict, Iterable, Optional

from pymarkdown_builder.partial_tokens import create_partial_token


class Tokens:
    """Markdown tokens. These are the building blocks of a markdown document."""

    @staticmethod
    def heading(
        text: str,
        level: Optional[int] = None,
    ) -> str:
        """Creates a heading with the given level by by prepending the text with `#`.

        Args:
            text (str): The text of the heading.
            level (int): The level of the heading. Must be between `#!python 1` and `#!python 6`. If not provided, will use `#!python 1`.

        Examples:
            >>> Tokens.heading("Hello, world!")
            '# Hello, world!'
            >>> Tokens.heading("Hello, world!", 2)
            '## Hello, world!'
        """  # noqa: E501
        level = level if level is not None else 1

        if level < 1 or level > 6:
            raise ValueError("Level must be between 1 and 6.")

        return f"{'#' * level} {text}"

    @staticmethod
    def h1(
        text: str,
    ) -> str:
        """Creates a level 1 heading."""
        return Tokens.heading(text, 1)

    @staticmethod
    def h2(
        text: str,
    ) -> str:
        """Creates a level 2 heading."""
        return Tokens.heading(text, 2)

    @staticmethod
    def h3(
        text: str,
    ) -> str:
        """Creates a level 3 heading."""
        return Tokens.heading(text, 3)

    @staticmethod
    def h4(
        text: str,
    ) -> str:
        """Creates a level 4 heading."""
        return Tokens.heading(text, 4)

    @staticmethod
    def h5(
        text: str,
    ) -> str:
        """Creates a level 5 heading."""
        return Tokens.heading(text, 5)

    @staticmethod
    def h6(
        text: str,
    ) -> str:
        """Creates a level 6 heading."""
        return Tokens.heading(text, 6)

    @staticmethod
    def paragraph(
        text: str,
    ) -> str:
        """Creates a paragraph. In fact, will just return the text.

        Args:
            text (str): The text of the paragraph.

        Examples:
            >>> Tokens.paragraph("Hello, world!")
            'Hello, world!'
        """  # noqa: E501
        return text

    @staticmethod
    def quote(
        text: str,
    ) -> str:
        """Creates a quote by prepending the text with `>`.

        Args:
            text (str): The text of the quote.

        Examples:
            >>> Tokens.quote("Hello, world!")
            '> Hello, world!'
        """
        return f"> {text}"

    @staticmethod
    def horizontal_rule() -> str:
        """Creates a horizontal rule using `---`.

        Examples:
            >>> Tokens.horizontal_rule()
            '---'
        """
        return "---"

    @staticmethod
    def link(
        href: str,
        text: Optional[str] = None,
    ) -> str:
        """Creates a link with `[text](href)` syntax.

        Args:
            href (str): The href of the link.
            text (Optional[str]): The text to be shown as the link. If not provided, will use the `href` value.

        Examples:
            >>> Tokens.link("https://example.com")
            '[https://example.com](https://example.com)'
            >>> Tokens.link("https://example.com", "Example")
            '[Example](https://example.com)'
        """  # noqa: E501
        text = text or href

        return f"[{text}]({href})"

    @staticmethod
    def image(
        src: str,
        alt: Optional[str] = None,
        mouseover: Optional[str] = None,
    ):
        """Creates an image with `![alt](src "mouseover")` syntax.

        Args:
            src (str): The source of the image. Can be a path or a URL.
            alt (Optional[str]): The alt text. If not provided, will use an empty string.
            mouseover (Optional[str]): The mouseover text. If not provided, will not be set.

        Examples:
            >>> Tokens.image("https://example.com/image.png")
            '![](https://example.com/image.png)'
            >>> Tokens.image("https://example.com/image.png", "alt text", "mouseover text")
            '![alt text](https://example.com/image.png "mouseover text")'
        """  # noqa: E501
        alt = alt or ""

        if mouseover is None:
            mouseover = ""

        if mouseover != "":
            mouseover = f' "{mouseover}"'

        return f"![{alt}]({src}{mouseover})"

    @staticmethod
    def code_block(
        text: str,
        lang: Optional[str] = None,
    ) -> str:
        r"""Creates a code block with triple backticks syntax.

        Args:
            text (str): The text of the code block.
            lang (Optional[str]): The language of the code block. If not provided, will not be set.

        Examples:
            >>> Tokens.code_block("print('Hello, world!')", "python")
            "```python\nprint('Hello, world!')\n```"
        """  # noqa: E501
        lang = lang or ""

        return f"```{lang}\n{text}\n```"

    @staticmethod
    def unordered_list(
        *items: str,
    ) -> str:
        r"""Creates an unordered list by prepending each item with `- `.

        Args:
            items (Iterable[str]): Items to be listed.

        Examples:
            >>> Tokens.unordered_list("Hello", "World")
            '- Hello\n- World'
        """
        return "\n".join(f"- {item}" for item in items)

    @staticmethod
    def ordered_list(
        *items: str,
    ) -> str:
        r"""Creates an ordered list by prepending each item with `1. `.

        Args:
            items (Iterable[str]): Items to be listed.

        Examples:
            >>> Tokens.ordered_list("Hello", "World")
            '1. Hello\n1. World'
        """
        return "\n".join(f"1. {item}" for item in items)

    @staticmethod
    def table(
        *rows: Iterable[str],
    ) -> str:
        r"""Creates a table from an iterable of rows with `|` syntax. Will separate the header and the body using `---`.

        Args:
            *rows (Iterable[str]): Unpacked iterable of rows. The first row is the header, and the rest are the body.

        Examples:
            >>> Tokens.table(["name", "age"], ["John", "20"], ["Jane", "19"])
            'name | age\n--- | ---\nJohn | 20\nJane | 19'
        """  # noqa: E501
        rows_iter = iter(rows)
        header_row = next(rows_iter, None)

        if header_row is None:
            return ""

        header_row = list(header_row)

        first_row = next(rows_iter, None)

        if first_row is None:
            return ""

        header_str = " | ".join(header_row)
        divider_str = " | ".join("---" for _ in header_row)
        body_str = "\n".join((" | ".join(row) for row in (first_row, *rows_iter)))

        return "\n".join((header_str, divider_str, body_str))

    @staticmethod
    def table_from_dicts(
        *dicts: Dict[str, str],
        header: Iterable[str] | None = None,
    ) -> str:
        r"""Creates a table from an iterable of dicts with `|` syntax. Will separate the header and the body using `---`.

        Args:
            *dicts (Dict[str, str]): Unpacked iterable of dicts. Each dict will be a row.
            header (Iterable[str] | None): Custom table header. If `None`, the keys of the first dict will be used.

        Examples:
            >>> Tokens.table_from_dicts({"name": "John", "age": "20"}, {"name": "Jane", "age": "19"})
            'name | age\n--- | ---\nJohn | 20\nJane | 19'
        """  # noqa: E501
        dicts_iter = iter(dicts)
        first_row = next(dicts_iter, None)

        if first_row is None:
            return ""

        header = header or list(first_row.keys())
        body = ((value for value in row.values()) for row in (first_row, *dicts_iter))

        return Tokens.table(*(header, *body))

    # short tokens
    h = heading
    p = paragraph
    ul = unordered_list
    ol = ordered_list
    hr = horizontal_rule
    img = image

    bold = create_partial_token("**")
    """Creates bold text by wrapping the text with `**`.

    Args:
        text (str): The text to be set as bold.

    Examples:
        >>> Tokens.bold("Hello, world!")
        '**Hello, world!**'
        >>> Tokens.bold | "Hello, world!" | Tokens.bold
        '**Hello, world!**'
    """

    italic = create_partial_token("*")
    """Creates italic text by wrapping the text with `*`.

    Args:
        text (str): The text to be set as italic.

    Examples:
        >>> Tokens.italic("Hello, world!")
        '**Hello, world!**'
        >>> Tokens.italic | "Hello, world!" | Tokens.italic
        '*Hello, world!*'
    """

    code = create_partial_token("`")
    """Creates code text by wrapping the text with backticks ``` ` ```.

    Args:
        text (str): The text to be set as code.

    Examples:
        >>> Tokens.code("Hello, world!")
        '`Hello, world!`'
        >>> Tokens.code | "Hello, world!" | Tokens.code
        '`Hello, world!`'
    """

    strike = create_partial_token("~~")
    """Creates strike through text by wrapping the text with `~~`.

    Args:
        text (str): The text to striked.

    Examples:
        >>> Tokens.strike("Hello, world!")
        '~~Hello, world!~~'
        >>> Tokens.strike | "Hello, world!" | Tokens.strike
        '~~Hello, world!~~'
    """
