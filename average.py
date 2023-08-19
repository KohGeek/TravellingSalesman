# take the average of each of the key of json file
# input: json file

import json


def average(json_file):
    with open(json_file) as f:
        data = json.load(f)
    for key in data:
        sum = 0
        for item in data[key]:
            sum += item
        data[key] = sum/len(data[key])
    return data


if __name__ == "__main__":
    data = average("elite.json")
    print(data)
