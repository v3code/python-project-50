import pytest

from gendiff.formats.stylish import render_diff_stylish
from tests.constants import STYLISH_NESTED_FILE_RESULT, \
    STYLISH_FLAT_FILE_RESULT


@pytest.fixture
def flat_diff_stylish_string():
    with open(STYLISH_FLAT_FILE_RESULT) as f:
        return f.read()


@pytest.fixture
def nested_diff_stylish_string():
    with open(STYLISH_NESTED_FILE_RESULT) as f:
        return f.read()


def test_flat_stylish_render(flat_diff_stylish_string, flat_descriptors):
    rendered_stylish_str = render_diff_stylish(flat_descriptors)
    assert rendered_stylish_str == flat_diff_stylish_string


def test_nested_stylish_render(nested_diff_stylish_string, nested_descriptors):
    rendered_stylish_str = render_diff_stylish(nested_descriptors)
    assert rendered_stylish_str == nested_diff_stylish_string
