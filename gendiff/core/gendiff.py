import json

from gendiff.core.diff_descriptors import build_diff_descriptors
from gendiff.formats import get_renderer, JSON


def load_json_from_file(file_path):
    with open(file_path) as file:
        return json.load(file)


def generate_diff(file_path1, file_path2, render_format=JSON):
    file_1 = load_json_from_file(file_path1)
    file_2 = load_json_from_file(file_path2)
    diff = build_diff_descriptors(file_1, file_2)
    render = get_renderer(render_format)
    return render(diff)
