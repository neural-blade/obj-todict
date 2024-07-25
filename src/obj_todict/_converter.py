def todict(obj):
    if isinstance(obj, dict):
        data = {}
        for (k, v) in obj.items():
            data[k] = todict(v)
        return data
    elif isinstance(obj, list | tuple | set):
        data = []
        for item in obj:
            data.append(todict(item))
        return data
    else:
        try:
            return todict(obj.__dict__)
        except AttributeError:
            return obj
