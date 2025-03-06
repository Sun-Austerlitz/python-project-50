import json
from typing import Any, Dict, List


def format_json(diff: List[Dict[str, Any]]) -> str:
    """
    Formats the diff in a JSON format.

    Parameters:
        diff (list): The diff representation.

    Returns:
        str: The formatted JSON diff.
    """

    def convert_to_nested_dict(diff: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Converts the diff list to a nested dictionary format.

        Parameters:
            diff (list): The diff representation.

        Returns:
            dict: The nested dictionary representation.
        """
        nested_dict = {}
        for item in diff:
            key = item["key"]
            status = item["status"]
            if status == "nested":
                nested_dict[key] = {
                    "status": "unchanged",
                    "value": convert_to_nested_dict(item["children"]),
                }
            elif status in ["added", "removed", "unchanged"]:
                nested_dict[key] = {
                    "status": status,
                    "value": item["value"],
                }
            elif status == "changed":
                nested_dict[key] = {
                    "status": status,
                    "old_value": item["old_value"],
                    "new_value": item["new_value"],
                }
        return nested_dict

    nested_diff = convert_to_nested_dict(diff)
    return json.dumps(nested_diff, indent=4)
