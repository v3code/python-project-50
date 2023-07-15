from gendiff.core.diff_descriptors import build_diff_descriptors
from gendiff.core.parser import load_file
from gendiff.formats import get_renderer, STYLISH


def generate_diff(file_path1, file_path2, render_format=STYLISH):
    file_1 = load_file(file_path1)
    file_2 = load_file(file_path2)
    diff = build_diff_descriptors(file_1, file_2)
    render = get_renderer(render_format)
    return render(diff)
