import json

from gendiff.core.config import JSON_INDENT


def render_diff_json(descriptors):
    json.dumps(descriptors, indent=JSON_INDENT)
