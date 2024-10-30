def to_int(string: str):
    try:
        int(string)
        return True
    except ValueError as e:
        return False
