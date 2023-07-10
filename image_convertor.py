import os
import sys
from PIL import Image
# Note this program will change all of the files in the desired directory

# I will be assuming I am only inputting image file for now
def main():
    folder = os.getcwd()
    for filepath in os.listdir():
        if filepath.endswith('.jpg'):
            f = Image.open(filepath)
            fname, fext = os.path.splitext(filepath)
            f.save(f"pngs/{fname}.png" )

# def path():
#     try:
#         ofile = sys.argv[1]
#         nfile = sys.argv[2]
#     except IndexError:
#         print("please give both original file name as well as the file to be converted")
# def convertor(ext):
#
#     folder = os.getcwd()
#     os.mkdir("images")
#     for file in os.listdir():
#         if file.endswith(ext):
#             with open(file) as file:
#                 fname,fext = os.path.splitext(file)



if __name__== "__main__":
    main()