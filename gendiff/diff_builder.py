from typing import Any, Dict, List

from .constants import (
    STATUS_ADDED,
    STATUS_CHANGED,
    STATUS_NESTED,
    STATUS_REMOVED,
    STATUS_UNCHANGED,
)


def build_diff(
    data1: Dict[str, Any],
    data2: Dict[str, Any],
) -> List[Dict[str, Any]]:
    """
    Builds a diff between two dictionaries.

    Parameters:
        data1 (dict): The first dictionary.
        data2 (dict): The second dictionary.

    Returns:
        list: The diff representation.
    """
    keys = sorted(set(data1) | set(data2))
    diff = []

    for key in keys:
        if key not in data1:
            diff.append(
                {
                    "key": key,
                    "status": STATUS_ADDED,
                    "value": data2[key],
                }
            )
        elif key not in data2:
            diff.append(
                {
                    "key": key,
                    "status": STATUS_REMOVED,
                    "value": data1[key],
                }
            )
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            diff.append(
                {
                    "key": key,
                    "status": STATUS_NESTED,
                    "children": build_diff(data1[key], data2[key]),
                }
            )
        elif data1[key] != data2[key]:
            diff.append(
                {
                    "key": key,
                    "status": STATUS_CHANGED,
                    "old_value": data1[key],
                    "new_value": data2[key],
                }
            )
        else:
            diff.append(
                {
                    "key": key,
                    "status": STATUS_UNCHANGED,
                    "value": data1[key],
                }
            )

    return diff
