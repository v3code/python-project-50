from .json import render_diff_json

JSON = 'json'


def get_renderer(format):
    if format == JSON:
        return render_diff_json
