"""A Markdown document builder with line and span writing modes."""

from dataclasses import dataclass, field

from typing_extensions import ParamSpec, Self, TypeVar


TMarkdownBuilder = TypeVar("TMarkdownBuilder", bound="MarkdownBuilder")
Params = ParamSpec("Params")
TReturn = TypeVar("TReturn")


@dataclass
class MarkdownBuilder:
    """A Markdown document builder with line and span writing modes."""

    document: str = field(default="")
    """Content of the builder."""

    def write_lines(self, *lines: str) -> Self:
        """Joins the lines with double line breaks and appends to the document.

        Args:
            *lines (str): Unpacked iterable of lines to be appended.

        Returns:
            The builder instance.
        """
        joined_lines = "\n\n".join(lines)

        if self.document != "":
            self.document += "\n\n"

        self.document += joined_lines

        return self

    def write_spans(self, *spans: str) -> Self:
        """Joins the spans and appends to the document.

        Args:
            *spans (str): Unpacked iterable of spans to be appended.

        Returns:
            The builder instance.
        """
        joined_spans = "".join(spans)

        self.document += joined_spans

        return self

    def line_break(self) -> Self:
        """Appends a line break to the document.

        Returns:
            The builder instance.
        """
        self.document += "\n\n"

        return self

    def __str__(self) -> str:
        """Returns the content of the builder."""
        return self.document

    lines = write_lines
    spans = write_spans
    br = line_break
