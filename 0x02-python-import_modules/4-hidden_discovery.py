#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4 as hidden
    li = dir(hidden)
    sorted_names = sorted(name for name in li if not name.startswith("__"))
    for name in sorted_names:
        print(name)
