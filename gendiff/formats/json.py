import json

INDENT = 2


def render_diff_json(descriptors):
    json.dumps(descriptors, indent=INDENT)
