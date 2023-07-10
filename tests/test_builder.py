from pymarkdown_builder.builder import MarkdownBuilder


def test_write_lines_should_not_prepend_lines_with_double_line_breaks_if_document_is_empty():
    builder = MarkdownBuilder()
    builder.write_lines(
        "content",
        "other content",
    )

    assert builder.document == "content\n\nother content"


def test_write_lines_should_prepend_lines_with_double_line_breaks_if_document_is_not_empty():
    builder = MarkdownBuilder("# Title")
    builder.write_lines(
        "content",
        "other content",
    )

    assert builder.document == "# Title\n\ncontent\n\nother content"


def test_write_lines_should_return_builder_instance():
    builder = MarkdownBuilder()
    result = builder.write_lines("")

    assert builder is result


def test_write_spans_should_join_spans():
    builder = MarkdownBuilder()
    builder.write_spans("Hello ", "World!")

    assert builder.document == "Hello World!"


def test_write_spans_should_return_builder_instance():
    builder = MarkdownBuilder()
    result = builder.write_spans("")

    assert builder is result


def test_line_break_should_append_double_line_break():
    builder = MarkdownBuilder()

    builder.br()

    assert builder.document == "\n\n"


def test_str_should_return_document():
    builder = MarkdownBuilder("Hello World!")

    assert str(builder) == builder.document == "Hello World!"
