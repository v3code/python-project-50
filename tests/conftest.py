import pytest

from gendiff.core.diff_descriptors import DELETED, UNCHANGED, \
    ADDED, MODIFIED, SUBDESCRIPTORS


@pytest.fixture
def flat_files():
    file_1 = {
        'host': 'hexlet.io',
        'timeout': 50,
        'proxy': '123.234.53.22',
        'follow': False
    }

    file_2 = {
        'timeout': 20,
        'verbose': True,
        'host': 'hexlet.io',
    }

    return file_1, file_2


@pytest.fixture
def nested_files():
    file_1 = {'common': {'setting1': 'Value 1', 'setting2': 200, 'setting3': True,
                         'setting6': {'key': 'value', 'doge': {'wow': ''}}},
              'group1': {'baz': 'bas', 'foo': 'bar', 'nest': {'key': 'value'}},
              'group2': {'abc': 12345, 'deep': {'id': 45}}
              }
    file_2 = {
        'common': {'setting1': 'Value 1', 'setting2': 100, 'setting6': {'list': [1, 2, 3],
                                                                        'doge': {'wow': 'mew'}}},
        'group3': {'baz': 'bas', 'foo': 'bar', 'nest': {'add_key': 'new_value'}},
        'group2': {'abc': 'abcd', 'deep': {'id': 45, 'name': 'john'}}
    }
    return file_1, file_2


@pytest.fixture
def flat_descriptors():
    return [
        {
            'key': 'follow',
            'value': False,
            'type': DELETED
        },
        {
            'key': 'host',
            'value': 'hexlet.io',
            'type': UNCHANGED
        },
        {
            'key': 'proxy',
            'value': '123.234.53.22',
            'type': DELETED
        },
        {
            'key': 'timeout',
            'value':
                {
                    'before': 50,
                    'after': 20
                },
            'type': MODIFIED
        },
        {
            'key': 'verbose',
            'value': True,
            'type': ADDED
        }
    ]


@pytest.fixture
def nested_descriptors():
    return [
        {
            "key": "common",
            "value": [
                {"key": "setting1", "value": "Value 1", "type": UNCHANGED},
                {
                    "key": "setting2",
                    "value": {"before": 200, "after": 100},
                    "type": MODIFIED,
                },
                {"key": "setting3", "value": True, "type": DELETED},
                {
                    "key": "setting6",
                    "value": [
                        {
                            "key": "doge",
                            "value": [
                                {
                                    "key": "wow",
                                    "value": {"before": "", "after": "mew"},
                                    "type": "modified",
                                }
                            ],
                            "type": SUBDESCRIPTORS,
                        },
                        {"key": "key", "value": "value", "type": DELETED},
                        {"key": "list", "value": [1, 2, 3], "type": ADDED},
                    ],
                    "type": SUBDESCRIPTORS,
                },
            ],
            "type": SUBDESCRIPTORS,
        },
        {
            "key": "group1",
            "value": {"baz": "bas", "foo": "bar", "nest": {"key": "value"}},
            "type": DELETED,
        },
        {
            "key": "group2",
            "value": [
                {
                    "key": "abc",
                    "value": {"before": 12345, "after": "abcd"},
                    "type": "modified",
                },
                {
                    "key": "deep",
                    "value": [
                        {"key": "id", "value": 45, "type": UNCHANGED},
                        {"key": "name", "value": "john", "type": ADDED},
                    ],
                    "type": SUBDESCRIPTORS,
                },
            ],
            "type": SUBDESCRIPTORS,
        },
        {
            "key": "group3",
            "value": {"baz": "bas", "foo": "bar", "nest": {"add_key": "new_value"}},
            "type": ADDED,
        },
    ]
