def create_file():
    try:
        with open("my_file.txt", "w") as file:
            file.write("This is line 1\n")
            file.write("12345\n")
            file.write("Another line with some text and numbers: 42\n")
            print("File created successfully.")
    except IOError as e:
        print("Error:", e)
    except Exception as e:
        print("Unexpected error:", e)


def read_file():
    try:
        with open("my_file.txt", "r") as file:
            print("Contents of my_file.txt:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied.")
    except Exception as e:
        print("Unexpected error:", e)


def append_file():
    try:
        with open("my_file.txt", "a") as file:
            file.write("Appending line 1\n")
            file.write("Appending line 2\n")
            file.write("Appending line 3\n")
            print("Lines appended successfully.")
    except IOError as e:
        print("Error:", e)
    except Exception as e:
        print("Unexpected error:", e)
    finally:
        print("File appending process completed.")


if __name__ == "__main__":
    try:
        create_file()
        print("\n")
        read_file()
        print("\n")
        append_file()
    except Exception as e:
        print("An error occurred:", e)
    finally:
        print("Script execution completed.")
