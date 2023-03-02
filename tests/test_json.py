import pytest

from gendiff.formats.json import build_json_dict


@pytest.fixture
def flat_diff_json_dict():
    return {
        "- follow": False,
        "host": "hexlet.io",
        "- proxy": "123.234.53.22",
        "- timeout": 50,
        "+ timeout": 20,
        "+ verbose": True
    }


def test_build_flat_json_dict(flat_diff_json_dict, flat_descriptors):
    built_flat_diff_json_dict = build_json_dict(flat_descriptors)
    assert flat_diff_json_dict == built_flat_diff_json_dict
