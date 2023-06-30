import pytest

from gendiff.formats.stylish import render_diff_stylish
from tests.constants import FLAT_FILE_RESULT


@pytest.fixture
def flat_diff_stylish_string():
    with open(FLAT_FILE_RESULT) as f:
        return f.read()


def test_build_flat_json_dict(flat_diff_stylish_string, flat_descriptors):
    rendered_stylish_str = render_diff_stylish(flat_descriptors)
    assert rendered_stylish_str == flat_diff_stylish_string
