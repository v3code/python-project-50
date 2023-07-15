import json

import pytest

from gendiff.core.config import INDENT
from gendiff.formats import render_diff_json


@pytest.fixture
def flat_diff_json_string(flat_descriptors):
    return json.dumps(flat_descriptors, indent=INDENT)


@pytest.fixture
def nested_diff_json_string(nested_descriptors):
    return json.dumps(nested_descriptors, indent=INDENT)


def test_flat_json_render(flat_diff_json_string, flat_descriptors):
    rendered_json_str = render_diff_json(flat_descriptors)
    assert rendered_json_str == flat_diff_json_string


def test_nested_json_render(nested_diff_json_string, nested_descriptors):
    rendered_json_str = render_diff_json(nested_descriptors)
    assert rendered_json_str == nested_diff_json_string
