def sum(a, b):
    return a + b


def main():
    print("This is irrelevant code.")


# If you call this file directly from a CLI, __name__ will be __main__. If this file has been imported in other file or module, the __name__ will be the filename. This way can avoid unnecessary code to run at runtime.
if __name__ == "__main__":
    main()
