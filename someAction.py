import os
from datetime import datetime


def mkdir(path: str):
    if not os.path.exists(path):
        os.mkdir(path)


def writeToFile(data: str, path: str):
    with open(path, "w") as f:
        f.write(data)


def main():
    mkdir("./output")
    time = datetime.now().isoformat()
    someData = [
        "This is some demo text only,",
        "nothing but just text.",
        "",
        f"written @ {time}",
    ]

    writeToFile("\n".join(someData), "./output/mytext.txt")
    print("DONE!")


if __name__ == "__main__":
    main()
