import os

def main():
    #Basic Print
    print("Hello World")

    #Example of accessing a persistent output file
    content = open("output/output.txt", 'r').read()
    f = open("output/output.txt", 'w')
    f.write(content)
    f.write("Test")
    f.close()


if __name__ == "__main__":
    main()