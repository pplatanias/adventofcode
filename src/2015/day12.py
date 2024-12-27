import json


def iterate(jsondata):
    global summer
    if isinstance(jsondata, list):
        for i in jsondata:
            iterate(i)
    elif isinstance(jsondata, int):
        summer += jsondata
    elif isinstance(jsondata, dict):
        for v in jsondata.values():
            iterate(v)


def iterate_no_reds(jsondata):
    global summer
    if isinstance(jsondata, list):
        for i in jsondata:
            iterate_no_reds(i)
    elif isinstance(jsondata, int):
        summer += jsondata
    elif isinstance(jsondata, dict):
        if not any(v == "red" for v in jsondata.values()):
            for v in jsondata.values():
                iterate_no_reds(v)


with open('inputs/2015/day12.txt') as file:
    jsondata = json.loads(file.read())

summer = 0
iterate(jsondata)
print(summer)

summer = 0
iterate_no_reds(jsondata)
print(summer)
