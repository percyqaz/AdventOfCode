import json
data = json.loads(open("input.txt").read())

def deep_count(obj):
    if isinstance(obj, dict):
        for key in obj:
            if obj[key] == "red": return 0
        return sum([deep_count(obj[key]) for key in obj])
    elif isinstance(obj, list):
        return sum([deep_count(value) for value in obj])
    elif isinstance(obj, str):
        return 0
    else:
        return obj

print(deep_count(data))
