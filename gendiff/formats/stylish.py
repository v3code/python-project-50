from gendiff.core.config import INDENT, INDENT_CHAR
from gendiff.core.diff_descriptors import ADDED, \
    DELETED, MODIFIED, SUBDESCRIPTORS

SYMBOL_DISPLACEMENT = 2


def reformat_key(key, descriptor_type):
    if descriptor_type == ADDED:
        return f'+ {key}'
    if descriptor_type == DELETED:
        return f'- {key}'
    return key


def get_indent(depth, displace=0):
    return (depth * INDENT - displace) * INDENT_CHAR


def add_field(key, value, depth=0, displace=0):
    return f'{get_indent(depth, displace)}{key}: {value}'


def process_value(value, depth=0):
    if isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, dict):
        formatted = ['{']
        next_depth = depth + 1
        for key, dict_val in value.items():
            dict_val_processed = process_value(dict_val, next_depth)
            formatted.append(
                add_field(key, dict_val_processed, next_depth)
            )
        formatted.append(f'{get_indent(depth)}}}')
        return '\n'.join(formatted)

    return value


def format_descriptors(descriptors, depth=0):
    formatted_list = ['{']
    depth += 1
    for descriptor in descriptors:
        key = descriptor['key']
        value = descriptor['value']

        if descriptor['type'] == MODIFIED:
            value_before = process_value(value['before'], depth)
            value_after = process_value(value['after'], depth)
            formatted_list.append(
                add_field(reformat_key(key, DELETED), value_before, depth, SYMBOL_DISPLACEMENT)
            )
            formatted_list.append(
                add_field(reformat_key(key, ADDED), value_after, depth, SYMBOL_DISPLACEMENT)
            )
        elif descriptor['type'] == ADDED:
            formatted_list.append(
                add_field(reformat_key(key, ADDED), process_value(value, depth), depth, SYMBOL_DISPLACEMENT)
            )
        elif descriptor['type'] == DELETED:
            formatted_list.append(
                add_field(reformat_key(key, DELETED), process_value(value, depth), depth, SYMBOL_DISPLACEMENT)
            )
        elif descriptor['type'] == SUBDESCRIPTORS:
            formatted_list.append(
                add_field(key, format_descriptors(value, depth), depth)
            )
        else:
            formatted_list.append(
                add_field(key, process_value(value, depth), depth)
            )
    formatted_list.append(f'{get_indent(depth - 1)}}}')
    return '\n'.join(formatted_list)


def render_diff_stylish(descriptors):
    return format_descriptors(descriptors)
