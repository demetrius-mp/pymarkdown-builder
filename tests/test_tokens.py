import pytest
from pymarkdown_builder.tokens import Tokens as t


def test_heading_without_level_should_return_h1():
    result = t.heading("hello")
    expected = "# hello"

    assert result == expected


def test_heading_levels():
    assert t.heading("hello", 1) == "# hello"
    assert t.heading("hello", 2) == "## hello"
    assert t.heading("hello", 3) == "### hello"
    assert t.heading("hello", 4) == "#### hello"
    assert t.heading("hello", 5) == "##### hello"
    assert t.heading("hello", 6) == "###### hello"


def test_heading_level_less_than_1_should_raise_value_error():
    with pytest.raises(ValueError):
        t.heading("hello", 0)

    with pytest.raises(ValueError):
        t.heading("hello", -1)


def test_h1_should_return_h1():
    result = t.h1("hello")
    expected = "# hello"

    assert result == expected


def test_h2_should_return_h2():
    result = t.h2("hello")
    expected = "## hello"

    assert result == expected


def test_h3_should_return_h3():
    result = t.h3("hello")
    expected = "### hello"

    assert result == expected


def test_h4_should_return_h4():
    result = t.h4("hello")
    expected = "#### hello"

    assert result == expected


def test_h5_should_return_h5():
    result = t.h5("hello")
    expected = "##### hello"

    assert result == expected


def test_h6_should_return_h6():
    result = t.h6("hello")
    expected = "###### hello"

    assert result == expected


def test_paragraph():
    result = t.paragraph("hello")
    expected = "hello"

    assert result == expected


def test_bold():
    result = t.bold("hello")
    expected = "**hello**"

    assert result == expected


def test_italic():
    result = t.italic("hello")
    expected = "*hello*"

    assert result == expected


def test_inline_code():
    result = t.code("hello")
    expected = "`hello`"

    assert result == expected


def test_quote():
    result = t.quote("hello")
    expected = "> hello"

    assert result == expected


def test_strike():
    result = t.strike("hello")
    expected = "~~hello~~"

    assert result == expected


def test_horizontal_rule():
    result = t.horizontal_rule()
    expected = "---"

    assert result == expected


def test_link_without_text_should_return_link_with_href_as_text():
    result = t.link("https://example.com")
    expected = "[https://example.com](https://example.com)"

    assert result == expected


def test_link_with_text_should_return_link_with_text():
    result = t.link("https://example.com", "example")
    expected = "[example](https://example.com)"

    assert result == expected


def test_image_without_alt_and_mouseover_should_return_image_with_empty_alt_and_no_mouseover():
    result = t.image("/path/to/image.png")
    expected = "![](/path/to/image.png)"

    assert result == expected


def test_image_with_alt_and_without_mouseover_should_return_image_with_alt():
    result = t.image("/path/to/image.png", alt="alt")
    expected = "![alt](/path/to/image.png)"

    assert result == expected


def test_image_with_mouseover_and_without_alt_should_return_image_with_mouseover_and_empty_alt():
    result = t.image("/path/to/image.png", mouseover="mouseover")
    expected = '![](/path/to/image.png "mouseover")'

    assert result == expected


def test_image_with_alt_and_mouseover_should_return_image_with_alt_and_mouseover():
    result = t.image("/path/to/image.png", alt="alt", mouseover="mouseover")
    expected = '![alt](/path/to/image.png "mouseover")'

    assert result == expected


def test_code_block_without_lang_should_return_code_block_without_lang():
    result = t.code_block("hello")
    expected = "```\nhello\n```"

    assert result == expected


def test_code_block_with_python_lang_should_return_python_code_block():
    result = t.code_block("import math\n\nprint(math.pi)", lang="python")
    expected = "```python\nimport math\n\nprint(math.pi)\n```"

    assert result == expected


def test_unordered_list_with_no_items_should_return_empty_string():
    result = t.unordered_list()
    expected = ""

    assert result == expected


def test_unordered_list_with_one_item_should_return_one_item():
    result = t.unordered_list("hello")
    expected = "- hello"

    assert result == expected


def test_unordered_list_with_two_items_should_return_two_items():
    result = t.unordered_list("hello", "world")
    expected = "- hello\n- world"

    assert result == expected


def test_ordered_list_with_no_items_should_return_empty_string():
    result = t.ordered_list()
    expected = ""

    assert result == expected


def test_ordered_list_with_one_item_should_return_one_item():
    result = t.ordered_list("hello")
    expected = "1. hello"

    assert result == expected


def test_ordered_list_with_two_items_should_return_two_items():
    result = t.ordered_list("hello", "world")
    expected = "1. hello\n1. world"

    assert result == expected


def test_table_with_no_rows_should_return_empty_string():
    result = t.table()
    expected = ""

    assert result == expected


def test_table_with_one_row_should_return_empty_string():
    result = t.table(
        # header
        ["name", "age", "city"],
        # body
    )

    expected = ""

    assert result == expected


def test_table_should_return_first_row_as_header():
    result = t.table(
        # header
        ["name", "age"],
        # body
        ["John", "30"],
        ["Mary", "20"],
    )

    header, _, *_ = result.split("\n")

    assert header == "name | age"


def test_table_should_use_triple_dash_as_header_separator():
    result = t.table(
        # header
        ["name", "age"],
        # body
        ["John", "30"],
        ["Mary", "20"],
    )

    _, header_separator, *_ = result.split("\n")

    assert header_separator == "--- | ---"


def test_table_header_separator_should_have_3_columns():
    result = t.table(
        # header
        ["name", "age", "city"],
        # body
        ["John", "30", "London"],
        ["Mary", "20", "Paris"],
    )

    _, header_separator, *_ = result.split("\n")

    assert header_separator.count("---") == 3


def test_table_body_should_have_4_rows():
    result = t.table(
        # header
        ["name", "age", "city"],
        # body
        ["John", "30", "London"],
        ["Mary", "20", "Paris"],
        ["Bob", "40", "New York"],
        ["Alice", "50", "Tokyo"],
    )

    _, _, *body = result.split("\n")

    assert len(body) == 4


def test_table_from_dicts_with_no_dicts_should_return_empty_string():
    result = t.table_from_dicts()
    expected = ""

    assert result == expected


def test_table_from_dicts_should_return_first_dict_keys_as_header():
    result = t.table_from_dicts(
        {"name": "John", "age": "30"},
        {"name": "Mary", "age": "20"},
    )

    header, _, *_ = result.split("\n")

    assert header == "name | age"


def test_table_from_dicts_with_1_dict_should_return_body_with_1_row():
    result = t.table_from_dicts(
        {"name": "John", "age": "30"},
    )

    _, _, *body = result.split("\n")

    assert len(body) == 1


def test_table_from_dicts_with_header_should_override_first_dict_keys():
    result = t.table_from_dicts(
        {"name": "John", "age": "30"},
        header=["NAME", "AGE"],
    )

    header, _, *_ = result.split("\n")

    assert header == "NAME | AGE"
