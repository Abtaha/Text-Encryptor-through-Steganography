import cv2
import os
from random import randint

def encypt(img, txt):
    for i in range(len(txt)):
        char = ord(txt[i])
        
        img[i][0][1] = randint(0, img.shape[0])
        img[i][0][2] = randint(0, img.shape[1])
        
        a = img[i][0][1]
        b = img[i][0][2]
        
        img[a][b][0] = char
        
    for i in range(len(img[0][len(txt) - 1])):
        img[len(txt)][0][2] = 10
    return img

def decrypt(img):
    text = []
    
    for i in range(len(img)):
        if img[i][0][2] == 10:
            return "".join(text)
        
        a = img[i][0][1]
        b = img[i][0][2]
        char = chr(img[a][b][0])
        text.append(char)

def main():
    try:
        print()
        print("1. Encrypt")
        print("2. Decrypt")
        print("E. Exit")
        inp = input("> ")
        
        if inp == "1":
            text = input("What text do you want to encrypt > ")
            img_file = input("Which file do you want to encrypt to > ")
            img = cv2.imread(img_file)
            btText = list(text)
            os.remove(img_file)
            cv2.imwrite(img_file, encypt(img, btText))
            print("Done")
            main()

        elif inp == "2":
            img_file = input("Which file do you want to decrypt from > ")
            img = cv2.imread(img_file)
            print(decrypt(img))
            main()
        
        elif inp == "E" or inp == "e":
            print("Exiting")
            exit()
        
        else:
            print("That is not a valid command.\nTry again")
            main()
            
    except Exception as e:
        print("Error")
        main()

if __name__ == "__main__":
    print("-"*60)
    print("TEXT ENCRYPTOR")
    print("-"*60)
    
    main()