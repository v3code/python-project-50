from .json import render_diff_json
from .stylish import render_diff_stylish
from .plain import render_diff_plain

JSON = 'json'
PLAIN = 'plain'
STYLISH = 'stylish'


def get_renderer(fmt):
    if fmt == STYLISH:
        return render_diff_stylish
    elif fmt == PLAIN:
        return render_diff_plain
    elif fmt == JSON:
        return render_diff_json
    else:
        raise NotImplementedError(f"Format '{fmt}' is not supported")
