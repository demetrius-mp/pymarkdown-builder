from pymarkdown_builder.builder import MarkdownBuilder, WriteMode


def test_line_mode_should_set_to_line_mode():
    builder = MarkdownBuilder()
    builder.line_mode()

    assert builder.mode == WriteMode.LINE


def test_span_mode_should_set_to_span_mode():
    builder = MarkdownBuilder()
    builder.span_mode()

    assert builder.mode == WriteMode.SPAN


def test_line_mode_should_return_builder():
    builder = MarkdownBuilder()

    assert builder.line_mode() == builder


def test_span_mode_should_return_builder():
    builder = MarkdownBuilder()

    assert builder.span_mode() == builder


def test_toggle_mode_should_toggle_mode():
    builder = MarkdownBuilder()

    assert builder.mode == WriteMode.LINE
    assert builder.toggle_mode().mode == WriteMode.SPAN
    assert builder.toggle_mode().mode == WriteMode.LINE


def test_toggle_mode_should_return_builder():
    builder = MarkdownBuilder()

    assert builder.toggle_mode() == builder


def test_is_mode_should_return_true_if_mode_is_correct():
    builder = MarkdownBuilder()

    assert builder.is_mode(WriteMode.LINE) is True

    builder.span_mode()

    assert builder.is_mode(WriteMode.SPAN) is True


def test_write_should_append_to_document_if_document_is_empty():
    builder = MarkdownBuilder()
    builder.write("Hello World!")

    assert builder.document == "Hello World!"


def test_write_should_prepend_text_with_double_line_breaks_if_document_is_not_empty():
    builder = MarkdownBuilder("Hello World!")
    builder.write("Hello World!")

    assert builder.document == "Hello World!\n\nHello World!"

    builder = MarkdownBuilder()
    builder.write("Hello World!")
    builder.write("Hello World!")

    assert builder.document == "Hello World!\n\nHello World!"


def test_write_lines_should_join_lines_with_double_line_breaks():
    builder = MarkdownBuilder()
    builder.write_lines("Hello World!", "Hello World!")

    assert builder.document == "Hello World!\n\nHello World!"


def test_write_lines_should_ignore_current_mode():
    builder = MarkdownBuilder()
    builder.span_mode()

    builder.write_lines("Hello World!", "Hello World!")

    assert builder.document == "Hello World!\n\nHello World!"


def test_write_lines_should_not_change_mode():
    builder = MarkdownBuilder()
    builder.span_mode()

    assert builder.mode == WriteMode.SPAN

    builder.write_lines("Hello World!", "Hello World!")

    assert builder.mode == WriteMode.SPAN


def test_write_spans_should_join_spans():
    builder = MarkdownBuilder()
    builder.write_spans("Hello ", "World!")

    assert builder.document == "Hello World!"


def test_write_spans_should_ignore_current_mode():
    builder = MarkdownBuilder()
    builder.line_mode()

    builder.write_spans("Hello ", "World!")

    assert builder.document == "Hello World!"


def test_write_spans_should_not_change_mode():
    builder = MarkdownBuilder()
    builder.line_mode()

    assert builder.mode == WriteMode.LINE

    builder.write_spans("Hello ", "World!")

    assert builder.mode == WriteMode.LINE


def test_str_should_return_document():
    builder = MarkdownBuilder("Hello World!")

    assert str(builder) == "Hello World!"
