from gendiff.core.gendiff import load_file
from constants import FLAT_FILE_1_JSON_PATH, \
    FLAT_FILE_2_JSON_PATH, FLAT_FILE_1_YAML_PATH, FLAT_FILE_2_YML_PATH


def test_json_load(flat_files):
    file1 = load_file(FLAT_FILE_1_JSON_PATH)
    file2 = load_file(FLAT_FILE_2_JSON_PATH)
    real_file1, real_file2 = flat_files
    assert file1 == real_file1
    assert file2 == real_file2


def test_yaml_load(flat_files):
    file1 = load_file(FLAT_FILE_1_YAML_PATH)
    file2 = load_file(FLAT_FILE_2_YML_PATH)
    real_file1, real_file2 = flat_files
    assert file1 == real_file1
    assert file2 == real_file2
