import json
import pathlib
import yaml

JSON_FORMAT = 'json'
YAML_FORMAT = 'yaml'
YML_FORMAT = 'yml'


def load_file(file_path):
    file_format = get_extension(file_path)
    with open(file_path) as file:
        return parse_file(file, file_format)


def get_extension(file_path):
    return pathlib.Path(file_path).suffix[1:]


def parse_file(file, file_format):
    file_format = file_format.lower()
    if file_format == JSON_FORMAT:
        return json.load(file)
    elif file_format in (YAML_FORMAT, YML_FORMAT):
        return yaml.safe_load(file)
    else:
        raise NotImplementedError(
            f'File with format "{file_format}" is not implemented'
        )
