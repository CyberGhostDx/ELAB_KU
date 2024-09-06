import json


def read_json(filename):
    with open(filename) as f:
        data = f.read()
        data = json.loads(data)
    return data


# specifying the zip file name
filename = "IMDB_movies_merged.json"

data = read_json(filename)


def q1():
    harrison = []
    for x in data:
        if x.get("cast"):
            if "Harrison Ford" in [y["name"] for y in x["cast"]]:
                harrison.append(x)

    harrison = [
        x
        for x in harrison
        if x["director"]["name"] != "Steven Spielberg" and x["ratingValue"]
    ]

    harrison.sort(key=lambda x: float(x["ratingValue"]), reverse=True)

    count = 1
    top_five = [harrison[0]["director"]["name"]]

    for i in range(1, len(harrison)):
        if harrison[i - 1]["ratingValue"] == harrison[i]["ratingValue"]:
            top_five.append(harrison[i]["director"]["name"])
        else:
            count += 1
            if count == 6:
                break
            top_five.append(harrison[i]["director"]["name"])

    for x in sorted(top_five):
        print(x)


def q2():
    har_geo = []
    for x in data:
        if x.get("cast"):
            if "Harrison Ford" in [
                y["name"] for y in x["cast"]
            ] and "Tommy Lee Jones" in [y["name"] for y in x["cast"]]:
                har_geo.append(x)

    har_geo = [
        x
        for x in har_geo
        if x["director"]["name"] != "Steven Spielberg"
        and x["director"]["name"] != "George Lucas"
        and x["ratingValue"]
    ]

    print(max(har_geo, key=lambda x: float(x["ratingValue"]))["name"])


print("(1) Answer of Q1")
print("(2) Answer of Q2")
ans = input("or just press (Enter): ")

if ans == "1":
    q1()
elif ans == "2":
    q2()
else:
    print("Nothing to do..")
