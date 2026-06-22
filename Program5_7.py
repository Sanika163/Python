#Boolean
#List all values that evaluates to False

def main():
    values = [
        False,
        None,
        0,
        0.0,
        0j,
        "",
        [],
        (),
        {},
        range(0)
    ]

    for value in values:
        print(value, "=", bool(value))

if (__name__ == "__main__"):
    main()