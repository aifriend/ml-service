def represents_float(s):
    try:
        if isinstance(s, list):
            for f in s:
                float(f)
            return True
        elif isinstance(s, dict):
            for f, v in s.items():
                float(v)
            return True
        else:
            float(s)
            return True
    except ValueError:
        return False


def represents_int(s):
    try:
        if isinstance(s, list):
            for i in s:
                int(i)
            return True
        elif isinstance(s, dict):
            for i, v in s.items():
                float(v)
            return True
        else:
            int(s)
            return True
    except ValueError:
        return False
