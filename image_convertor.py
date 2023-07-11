import os
import sys
from PIL import Image
# Note this program will change all the files in the desired directory

# I will be assuming I am only inputting image file for now
def main():
    path = path_input()
    # print(os.listdir(sys.argv[1]))
    # convertor(filepath, ext)
    # sys.argv[0]

def path_input():

    try:
        if len(sys.argv) == 3 :
            if os.path.isfile(sys.argv[1]):
                filepath = sys.argv[1]
            else:
                sys.exit("Please provide valid path")

        else:
            sys.exit("Please use only one argument which should be the file path")
        return filepath
    except IndexError:
        sys.exit("Please provide valid details.")

def convertor(filepath,ext):
    folder = os.getcwd()
    for filepath in os.listdir():
        if filepath.endswith('.jpg'):
            f = Image.open(filepath)
            fname, fext = os.path.splitext(filepath)
            f.save(f"images/{fname}.{ext}")




if __name__== "__main__":
    main()