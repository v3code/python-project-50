from .json import render_diff_json
from .plain import render_diff_plain

JSON = 'json'
PLAIN = 'plain'


def get_renderer(fmt):
    if fmt == JSON:
        return render_diff_json
    elif fmt == PLAIN:
        return render_diff_plain
    else:
        raise NotImplementedError(f"Format '{fmt}' is not supported")
