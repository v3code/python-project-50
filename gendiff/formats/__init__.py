from .json import render_diff_json

JSON = 'json'


def get_renderer(fmt):
    if fmt == JSON:
        return render_diff_json
