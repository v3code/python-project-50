import json

from gendiff.core.config import INDENT


def render_diff_json(descriptors):
    json.dumps(descriptors, indent=INDENT)
