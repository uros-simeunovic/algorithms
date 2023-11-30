def list_to_tree(elements):
    while len(elements) > 1:
        last = elements.pop()
        for e in elements:
            if e.get("id") == last.get("parent"):
                if "elements" not in e:
                    e["elements"] = []
                del last["parent"]
                e["elements"].append(last)
    return elements[0]

def print_tree_ids(element):
    print(element["id"])
    if "elements" in element:
        for e in element["elements"]:
            print_id(e)


def get_tree_ids(element):
    n = [element["id"]]
    if "elements" in element:
        for e in element["elements"]:
            n.extend(get_tree_ids(e))
    return n

