import os
from datetime import datetime


lorem = " ".join(
    [
        "Lorem Ipsum is simply dummy text of the printing and typesetting industry.",
        "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,",
        "when an unknown printer took a galley of type and scrambled it to make",
        "a type specimen book. It has survived not only five centuries, but also",
        "the leap into electronic typesetting, remaining essentially unchanged.",
        "It was popularised in the 1960s with the release of Letraset sheets",
        "containing Lorem Ipsum passages, and more recently with desktop publishing",
        "software like Aldus PageMaker including versions of Lorem Ipsum.",
    ]
)


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
        lorem,
        "",
        f"written @ {time}",
        "",
    ]

    writeToFile("\n".join(someData), "./output/mytext.txt")
    print("DONE!")


if __name__ == "__main__":
    main()
