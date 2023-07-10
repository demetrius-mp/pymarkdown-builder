"""A Markdown document builder with line and span writing modes."""

from dataclasses import dataclass, field
from enum import Enum
from functools import wraps
from typing import Callable

from typing_extensions import Concatenate, ParamSpec, Self, TypeVar


TMarkdownBuilder = TypeVar("TMarkdownBuilder", bound="MarkdownBuilder")
Params = ParamSpec("Params")
TReturn = TypeVar("TReturn")


class WriteMode(Enum):
    """The writing mode of the builder."""

    LINE = "line"
    """Line mode."""

    SPAN = "span"
    """Span mode."""


def fixed_write_mode(mode: WriteMode):
    """A decorator to set the writing mode of a builder method."""

    def decorator(
        method: Callable[Concatenate[TMarkdownBuilder, Params], TReturn],
    ) -> Callable[Concatenate[TMarkdownBuilder, Params], TReturn]:
        @wraps(method)
        def inner(
            self: TMarkdownBuilder,
            *args: Params.args,
            **kwargs: Params.kwargs,
        ) -> TReturn:
            original_write_mode = self.mode

            self.mode = mode
            result = method(self, *args, **kwargs)
            self.mode = original_write_mode

            return result

        return inner

    return decorator


@dataclass
class MarkdownBuilder:
    """A Markdown document builder with line and span writing modes."""

    document: str = field(default="")
    """Content of the builder."""

    mode: WriteMode = field(default=WriteMode.LINE, init=False)
    """Write mode of the builder. See [`WriteMode`][pymarkdown_builder.builder.WriteMode]."""  # noqa: E501

    def line_mode(self) -> Self:
        """Sets the builder to `line` mode.

        Returns:
            The builder instance.
        """
        self.mode = WriteMode.LINE
        return self

    def span_mode(self) -> Self:
        """Sets the builder to `span` mode.

        Returns:
            The builder instance.
        """
        self.mode = WriteMode.SPAN
        return self

    def toggle_mode(self) -> Self:
        """Toggles between `line` and `span` modes.

        Returns:
            The builder instance.
        """
        if self.mode == WriteMode.LINE:
            self.span_mode()

        elif self.mode == WriteMode.SPAN:
            self.line_mode()

        return self

    def is_mode(self, mode: WriteMode) -> bool:
        """Checks if the builder is in the given mode.

        Args:
            mode (WriteMode): Mode to check.

        Returns:
            True if the builder is in the given mode, False otherwise.
        """
        return self.mode == mode

    def write(self, /, text: str) -> Self:
        """Appends the text to the current document.

        If on `line`, mode,
            the text will be prepended with double line breaks.

        Args:
            text (str): Text to be appended.

        Returns:
            The builder instance.
        """  # noqa: E501
        if self.is_mode(WriteMode.LINE) and self.document != "":
            text = "\n\n" + text

        self.document += text

        return self

    @fixed_write_mode(WriteMode.LINE)
    def write_lines(self, *lines: str) -> Self:
        """Joins the lines with double line breaks and appends to the document.

        Args:
            *lines (str): Unpacked iterable of lines to be appended.

        Returns:
            The builder instance.
        """
        joined_lines = "\n\n".join(lines)
        self.write(joined_lines)

        return self

    @fixed_write_mode(WriteMode.SPAN)
    def write_spans(self, *spans: str) -> Self:
        """Joins the spans and appends to the document.

        Args:
            *spans (str): Unpacked iterable of spans to be appended.

        Returns:
            The builder instance.
        """
        joined_spans = "".join(spans)
        self.write(joined_spans)

        return self

    def __str__(self) -> str:
        """Returns the content of the builder."""
        return self.document

    lines = write_lines
    spans = write_spans
