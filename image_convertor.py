from colorama import Fore, Back, Style

import os
import sys
from PIL import Image
# Note this program will change all the files in the desired directory

# I will be assuming I am only inputting image file for now
def main():
    intro()

    path = path_input()
    # print(os.listdir(sys.argv[1]))
    # convertor(filepath, ext)
    # sys.argv[0]

def intro():
    print(Fore.RED+"   ****************  **************               WELCOME TO IMAGE CONVERTOR!!")
    print(Fore.RED+"     *************  ************                                                                       ")
    print(Fore.RED+"        ******       *********                                                               ")
    print(Fore.RED+"         ****        ******            This is in testing phase therefore it only works to convert jpg to png")
    print(Fore.RED+"         ****        ******                                                                        ")
    print(Fore.BLUE+"         ****        ******             Convert all the images in a folder to a desired extension")
    print(Fore.BLUE+"         ****        ******                  ")
    print(Fore.BLUE+"        ******       *********   ")
    print(Fore.BLUE+"   ****************  ************   ")
    print(Fore.BLUE+"   ****************  **************   ")

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