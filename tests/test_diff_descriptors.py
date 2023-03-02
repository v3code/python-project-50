import pytest
from faker import Faker
import json

from gendiff.core.diff_descriptors import get_added_field_descriptor, \
    ADDED, MODIFIED, UNCHANGED, DELETED, SUBDESCRIPTORS, \
    get_modified_field_descriptor, get_deleted_field_descriptor, \
    get_unchanged_field_descriptor, build_diff_descriptors

def test_diff_builder(test_json_files_and_descriptors):
    json_1, json_2, expected_descriptors = test_json_files_and_descriptors

    descriptors = build_diff_descriptors(json_1, json_2)
    assert descriptors == expected_descriptors


def test_get_added_descriptor(faker: Faker):
    mock_key = faker.name()
    mock_value = faker.unique.random_int()

    expected_descriptor = {
        "key": mock_key,
        "value": mock_value,
        "type": ADDED
    }

    add_descriptor = get_added_field_descriptor(mock_key, mock_value)

    assert add_descriptor == expected_descriptor


def test_get_modified_descriptor(faker: Faker):
    mock_key = faker.name()
    mock_value_before = faker.unique.random_int()
    mock_value_after = faker.unique.random_int()

    expected_descriptor = {
        "key": mock_key,
        "value": {
            "before": mock_value_before,
            "after": mock_value_after
        },
        "type": MODIFIED
    }

    modified_descriptor = get_modified_field_descriptor(mock_key,
                                                        mock_value_before,
                                                        mock_value_after)

    assert modified_descriptor == expected_descriptor


def test_get_deleted_descriptor(faker: Faker):
    mock_key = faker.name()
    mock_value = faker.unique.random_int()

    expected_descriptor = {
        "key": mock_key,
        "value": mock_value,
        "type": DELETED
    }

    deleted_descriptor = get_deleted_field_descriptor(mock_key, mock_value)

    assert deleted_descriptor == expected_descriptor


def test_get_unchanged_descriptor(faker: Faker):
    mock_key = faker.name()
    mock_value = faker.unique.random_int()

    expected_descriptor = {
        "key": mock_key,
        "value": mock_value,
        "type": UNCHANGED
    }

    unchanged_descriptor = get_unchanged_field_descriptor(mock_key, mock_value)

    assert unchanged_descriptor == expected_descriptor
