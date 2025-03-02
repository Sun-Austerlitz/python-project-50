import json
from typing import Any, Dict


def format_json(diff: Dict[str, Any]) -> str:
    """
    Formats the diff in a JSON format.

    Parameters:
        diff (dict): The diff representation.

    Returns:
        str: The formatted JSON diff.
    """

    def replace_nested_status(diff: Dict[str, Any]) -> Dict[str, Any]:
        """
        Recursively replaces 'nested' status with 'unchanged' in the diff.

        Parameters:
            diff (dict): The diff representation.

        Returns:
            dict: The updated diff with 'nested' status replaced.
        """
        updated_diff = {}
        for key, value in diff.items():
            if value.get("status") == "nested":
                updated_diff[key] = {
                    "status": "unchanged",
                    "value": replace_nested_status(value["children"]),
                }
            else:
                updated_diff[key] = value
        return updated_diff

    updated_diff = replace_nested_status(diff)
    return json.dumps(updated_diff, indent=4)
