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