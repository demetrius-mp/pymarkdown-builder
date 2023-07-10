"""Implementation of partial tokens.

A partial token is a callable that wraps text with a given string.
It can also be used with pipe operators to allow composition with other tokens.

To create your own partial tokens, use the [`create_partial_token`][pymarkdown_builder.partial_tokens.create_partial_token] function.
"""  # noqa: E501


from typing import Optional


class InvalidPartialTokenCompositionError(Exception):
    """Raised when a partial token is constructed in an invalid way."""


class PartialTokenContent(str):
    """An "overloaded" string to support pipe operations with [`PartialToken`][pymarkdown_builder.partial_tokens.PartialToken]."""  # noqa: E501

    def __new__(cls, string: str):
        """Creates a new partial token content."""
        return super().__new__(cls, string)

    def __or__(self, value: "str | PartialToken") -> "PartialTokenContent":
        """Executed when on the **left** side of the pipe operator.

        The right side of the pipe operator can be either a `#!python str` or a
            [`PartialToken`][pymarkdown_builder.partial_tokens.PartialToken].
            Always returns a [`PartialToken`][pymarkdown_builder.partial_tokens.PartialToken].
        """  # noqa: E501
        if isinstance(value, str):
            return PartialTokenContent(self + value)

        if isinstance(value, PartialToken):
            return PartialTokenContent(self + value.close_tag)

    def __ror__(self, value: "str | PartialToken") -> "PartialTokenContent":
        """Executed when on the **right** side of the pipe operator.

        The left side of the pipe operator can be either a `#!python str` or a
            [`PartialToken`][pymarkdown_builder.partial_tokens.PartialToken].
            Always returns a [`PartialToken`][pymarkdown_builder.partial_tokens.PartialToken].
        """  # noqa: E501
        if isinstance(value, str):
            return PartialTokenContent(value + self)

        if isinstance(value, PartialToken):
            return PartialTokenContent(value.close_tag + self)


class PartialToken:
    """Partial token representation.

    A partial token is a callable that wraps text with a given string.
        It can also be used with pipe operators to allow composition with other tokens.

    Examples:
        >>> bold = PartialToken("**")
        >>> italic = PartialToken("_")
        >>> bold | "hello" | italic | "world" | italic | bold
        '**hello_world_**'
    """

    open_tag: str
    """String that will be prepended to the text."""
    close_tag: str
    """String that will be appended to the text."""

    def __init__(
        self,
        open_tag: str,
        close_tag: Optional[str] = None,
    ) -> None:
        """Initializes the partial token.

        Args:
            open_tag (str): The string that will be prepended to the text.
            close_tag (Optional[str]): The string that will be appended to the text. If not provided, will use the `open_tag` value.
        """  # noqa: E501
        close_tag = close_tag or open_tag

        self.open_tag = open_tag
        self.close_tag = close_tag

    def __call__(self, text: str) -> str:
        """Wraps the text with the tags."""
        return f"{self.open_tag}{text}{self.close_tag}"

    def __or__(self, value: "str | PartialToken") -> PartialTokenContent:
        """Executed when on the **left** side of the pipe operator, **opening** the tag.

        The right side of the pipe operator can be either a `#!python str` or a
            [`PartialToken`][pymarkdown_builder.partial_tokens.PartialToken].
            Always returns a [`PartialTokenContent`][pymarkdown_builder.partial_tokens.PartialTokenContent].
        """  # noqa: E501
        if isinstance(value, PartialToken):
            return PartialTokenContent(self.open_tag + value.open_tag)

        if isinstance(value, str):
            return PartialTokenContent(self.open_tag + value)

    def __ror__(self, value: PartialTokenContent) -> PartialTokenContent:
        """Executed when on the **right** side of the pipe operator, **closing** the tag.

        The left side of the pipe operator must be a
            [`PartialTokenContent`][pymarkdown_builder.partial_tokens.PartialTokenContent].
            Always returns a [`PartialTokenContent`][pymarkdown_builder.partial_tokens.PartialTokenContent].
        """  # noqa: E501
        if isinstance(value, PartialTokenContent):
            return PartialTokenContent(value + self.close_tag)

        raise InvalidPartialTokenCompositionError()


def create_partial_token(
    open_tag: str,
    close_tag: Optional[str] = None,
):
    """Creates a partial token.

    Args:
        open_tag (str): The string that will be prepended to the text.
        close_tag (Optional[str]): The string that will be appended to the text. If not provided, will use the `open_tag` value.
    """  # noqa: E501
    return PartialToken(open_tag, close_tag)
