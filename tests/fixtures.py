import pytest

from gendiff.core.diff_descriptors import DELETED, UNCHANGED, ADDED, MODIFIED, SUBDESCRIPTORS


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
