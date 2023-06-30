import json

from gendiff.core.config import INDENT


def render_diff_json(descriptors):
    return json.dumps(descriptors, indent=INDENT)
