#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    files = dir(hidden_4)
    for name in files:
        if files[:2] != "__":
            print(name)
