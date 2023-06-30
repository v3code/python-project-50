from gendiff.core.diff_descriptors import MODIFIED, ADDED, DELETED, SUBDESCRIPTORS

FIELD_TEMPLATE = ''


def resolve_value(value):
    if isinstance(value, str):
        return f"'{value}'"
    elif value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, dict) or isinstance(value, list):
        return '[complex value]'
    else:
        return value


def get_modified_description(descriptor):
    value_from = resolve_value(descriptor['value']['before'])
    value_to = resolve_value(descriptor['value']['after'])
    return f"updated. From {value_from} to {value_to}"


def get_added_description(descriptor):
    value = resolve_value(descriptor['value'])
    return F"added with value: {value}"


def get_removed_description():
    return 'removed'


def resolve_field(field, root_field=None):
    if root_field is None:
        return field
    return '.'.join((root_field, field))


def get_field_description(root_field, field, change_description):
    description_field = resolve_field(field, root_field)
    return f"Property '{description_field}' was {change_description}."


def parse_descriptors(descriptors, root_field=None, diff_description_list=None):
    if diff_description_list is None:
        diff_description_list = []
    for descriptor in descriptors:
        if descriptor['type'] == MODIFIED:
            diff_description_list.append(
                get_field_description(root_field,
                                      descriptor['key'],
                                      get_modified_description(descriptor)))

        elif descriptor['type'] == ADDED:
            diff_description_list.append(
                get_field_description(root_field,
                                      descriptor['key'],
                                      get_added_description(descriptor))
            )

        elif descriptor['type'] == DELETED:
            diff_description_list.append(
                get_field_description(root_field,
                                      descriptor['key'],
                                      get_removed_description())
            )
        elif descriptor['type'] == SUBDESCRIPTORS:
            parse_descriptors(descriptor['value'],
                              resolve_field(descriptor['key'], root_field),
                              diff_description_list)

    return diff_description_list


def render_diff_plain(descriptors):
    diff_descriptions = parse_descriptors(descriptors)
    return '\n'.join(diff_descriptions)
