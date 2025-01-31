"""
Constants for formatting the diff output.
"""
# if a key is present in the second file but not in the first
ADDED = "  + {key}: {value}"

# if a key is present in both files but with different values
REMOVED = "  - {key}: {value}"

# if a key is present in both files with the same value
UNCHANGED = "    {key}: {value}"

# the template for the diff output
DIFF_TEMPLATE = "{{\n{diff}\n}}"
