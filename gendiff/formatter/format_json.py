import json


def format_json(diff):

    def convert_to_nested_dict(diff):
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
