
def read_text():
    with open("numbers.txt", "r") as file:
        read_file  = file.read()
        splited = read_file.split(",")
        for item in splited:
            print(item)


if __name__ == "__main__":
    read_text()