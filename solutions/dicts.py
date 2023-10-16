def get_value(data_dict, key):
    """
    Returns the value for the given key in the dictionary.
    If the key is not in the dictionary, return None.
    """
    data=data_dict.get(key)
    return data


def remove_key(data_dict, key):
    """
    Removes the entry with the specified key from the dictionary.
    If the key is not found, the dictionary should remain unchanged.
    Returns the modified dictionary.
    """

