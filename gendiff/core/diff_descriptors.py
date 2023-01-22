MODIFIED = 'modified'
ADDED = 'added'
DELETED = 'deleted'
UNCHANGED = 'unchanged'
SUBDESCRIPTORS = 'subdescriptors'


def build_descriptor(key, value, change_type):
    return {
        "key": key,
        "value": value,
        "type": change_type,
    }


def get_added_field_descriptor(key, value):
    return build_descriptor(key, value, ADDED)


def get_unchanged_field_descriptor(key, value):
    return build_descriptor(key, value, UNCHANGED)


def get_modified_field_descriptor(key, value_before, value_after):
    descriptor_val = {
        "before": value_before,
        "after": value_after,
    }
    return build_descriptor(key, descriptor_val, MODIFIED)


def get_deleted_field_descriptor(key, value):
    return build_descriptor(key, value, DELETED)


def build_diff_subdescriptors(key, subdict_1, subdict_2):
    return build_descriptor(key,
                            build_diff_descriptors(subdict_1, subdict_2),
                            SUBDESCRIPTORS)


def build_diff_descriptors(dict_1, dict_2):
    keys = dict_1.keys() | dict_2.keys()
    descriptors = []
    for key in sorted(keys):
        if key not in dict_2:
            descriptors.append(get_deleted_field_descriptor(key, dict_1[key]))
        elif key not in dict_1:
            descriptors.append(get_added_field_descriptor(key, dict_2[key]))
        elif isinstance(dict_1[key], dict) and isinstance(dict_2[key], dict):
            descriptors.append(build_diff_subdescriptors(key,
                                                         dict_1[key],
                                                         dict_2[key]))
        elif dict_1[key] != dict_2[key]:
            descriptors.append(get_modified_field_descriptor(key,
                                                             dict_1[key],
                                                             dict_2[key]))
        else:
            descriptors.append(
                get_unchanged_field_descriptor(key, dict_1[key]))

    return descriptors
