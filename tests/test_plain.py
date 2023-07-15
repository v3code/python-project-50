import pytest

from gendiff.formats import render_diff_plain
from tests.constants import PLAIN_FLAT_FILE_RESULT, PLAIN_NESTED_FILE_RESULT


@pytest.fixture
def flat_diff_plain_string():
    with open(PLAIN_FLAT_FILE_RESULT) as f:
        return f.read()


@pytest.fixture
def nested_diff_plain_string():
    with open(PLAIN_NESTED_FILE_RESULT) as f:
        return f.read()


def test_flat_plain_render(flat_diff_plain_string, flat_descriptors):
    rendered_plain_str = render_diff_plain(flat_descriptors)
    assert rendered_plain_str == flat_diff_plain_string


def test_nested_plain_render(nested_diff_plain_string, nested_descriptors):
    rendered_plain_str = render_diff_plain(nested_descriptors)
    assert rendered_plain_str == nested_diff_plain_string
