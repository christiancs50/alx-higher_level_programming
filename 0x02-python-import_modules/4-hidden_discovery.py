#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    files = dir()
    for i in range(0, len(files)):
        if files[i][:2] != "__":
            print("{}".format(files[i]))
