import json
import util

with open('resources/input.json') as f:
    elements = json.load(f)

root = util.list_to_tree(elements)

with open('resources/output.json', 'w') as f:
    json.dump(root, f, indent=2)

ids = util.get_tree_ids(root)
ids = util.get_tree_ids(root)
ids = util.get_tree_ids(root)

print(ids)