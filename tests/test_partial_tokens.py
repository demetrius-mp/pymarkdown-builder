import pytest
from pymarkdown_builder import partial_tokens as pt


def test_partial_token_content_should_work_as_string():
    content = pt.PartialTokenContent("string")

    assert content == "string"


def test_partial_token_content_or_op_with_string_should_return_partial_token_content():
    content = pt.PartialTokenContent("string")

    result = content | "hello"
    assert result == "stringhello"
    assert isinstance(result, pt.PartialTokenContent)

    result = content.__or__("hello")
    assert result == "stringhello"
    assert isinstance(result, pt.PartialTokenContent)


def test_partial_token_content_or_op_with_partial_token_should_return_partial_token_content():
    content = pt.PartialTokenContent("string")
    partial_token = pt.PartialToken("**")

    result = content | partial_token
    assert result == "string**"
    assert isinstance(result, pt.PartialTokenContent)

    result = content.__or__(partial_token)
    assert result == "string**"
    assert isinstance(result, pt.PartialTokenContent)


def test_partial_token_content_ror_op_with_string_should_return_partial_token_content():
    content = pt.PartialTokenContent("string")

    result = "hello" | content
    assert result == "hellostring"
    assert isinstance(result, pt.PartialTokenContent)

    result = content.__ror__("hello")
    assert result == "hellostring"
    assert isinstance(result, pt.PartialTokenContent)


def test_partial_token_content_ror_op_with_partial_token_should_return_partial_token_content():
    content = pt.PartialTokenContent("string")
    partial_token = pt.PartialToken("**")

    result = partial_token | content
    assert result == "**string"
    assert isinstance(result, pt.PartialTokenContent)

    result = content.__ror__(partial_token)
    assert result == "**string"
    assert isinstance(result, pt.PartialTokenContent)


def test_partial_token_as_function_call_should_return_string():
    bold = pt.PartialToken("**")

    result = bold("hello")
    assert result == "**hello**"
    assert isinstance(result, str)


def test_partial_token_or_op_with_string_should_return_partial_token_content():
    bold = pt.PartialToken("**")

    result = bold | "hello"
    assert result == "**hello"
    assert isinstance(result, pt.PartialTokenContent)

    result = bold.__or__("hello")
    assert result == "**hello"
    assert isinstance(result, pt.PartialTokenContent)


def test_partial_token_or_op_with_partial_token_should_return_partial_token_content():
    bold = pt.PartialToken("**")
    italic = pt.PartialToken("_")

    result = bold | italic
    assert result == "**_"
    assert isinstance(result, pt.PartialTokenContent)

    result = bold.__or__(italic)
    assert result == "**_"
    assert isinstance(result, pt.PartialTokenContent)


def test_partial_token_ror_op_with_string_should_raise_invalid_partial_token_composition_error():
    bold = pt.PartialToken("**")

    with pytest.raises(pt.InvalidPartialTokenCompositionError):
        "string" | bold  # type: ignore
        bold.__ror__("string")  # type: ignore


def test_partial_token_ror_op_with_partial_token_content_should_return_partial_token_content():
    bold = pt.PartialToken("**")
    content = pt.PartialTokenContent("hello")

    result = content | bold
    assert result == "hello**"
    assert isinstance(result, pt.PartialTokenContent)

    result = bold.__ror__(content)
    assert result == "hello**"
    assert isinstance(result, pt.PartialTokenContent)


def test_partial_token_composition_should_return_partial_token_content():
    bold = pt.PartialToken("**")
    italic = pt.PartialToken("_")

    result = bold | "hello" | italic | "world" | italic | bold
    assert result == "**hello_world_**"
    assert isinstance(result, pt.PartialTokenContent)


def test_create_partial_token_should_return_partial_token_content_with_correct_tags():
    bold = pt.create_partial_token("**")
    assert bold.open_tag == "**"
    assert bold.close_tag == "**"

    python_inline = pt.create_partial_token("`#!python", "`")
    assert python_inline.open_tag == "`#!python"
    assert python_inline.close_tag == "`"
