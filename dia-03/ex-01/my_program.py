from local_lib import path

def main():
    try:
        path.os.makedirs("new_folder")
        new_file = path.io.open("new_folder/new_file.txt", "w")
        new_file.write('Hello word!')
        new_file.close()
        
        my_file = path.io.open("new_folder/new_file.txt", "r")
        my_file = my_file.read()
        print(my_file)
    except FileExistsError as ex:
        print(ex)


if __name__ == "__main__":
    main()