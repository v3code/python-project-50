import json

from src.gendiff.core.config import JSON_INDENT
from src.gendiff.core.diff_descriptors import ADDED, \
    DELETED, MODIFIED, SUBDESCRIPTORS


def reformat_key(key, descriptor_type):
    if descriptor_type == ADDED:
        return f'+ {key}'
    if descriptor_type == DELETED:
        return f'- {key}'
    return key


def build_json_dict(descriptors):
    json_dict = {}
    for descriptor in descriptors:
        key = descriptor["key"]
        value = descriptor["value"]
        descriptor_type = descriptor["type"]
        if descriptor_type == ADDED or descriptor_type == DELETED:
            json_dict[reformat_key(key, descriptor_type)] = value
        elif descriptor_type == MODIFIED:
            json_dict[f'- {key}'] = value["before"]
            json_dict[f'+ {key}'] = value["after"]
        elif descriptor_type == SUBDESCRIPTORS:
            json_dict[key] = build_json_dict(value)
        else:
            json_dict[key] = value
    return json_dict


def render_diff_json(descriptors):
    json_dict = build_json_dict(descriptors)
    return json.dumps(json_dict, indent=4,)
