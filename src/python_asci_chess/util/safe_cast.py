def to_int(string: str):
    try:
        return int(string)
    except ValueError:
        return 0
