import sys
from output import print_directory


def main():

    if len(sys.argv) <= 1:
        print("Directory not entered")
        return

    directory = sys.argv[1]
    try:
        print_directory(directory)
    except FileNotFoundError:
        print("Directory not found")


if __name__ == "__main__":
    main()

# python3 task_3/main.py /Users/rostyslavohochyi/Desktop/Course/Home_works/goit-algo-hw-04/task_1/