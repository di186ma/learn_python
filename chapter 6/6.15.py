# обработка открытия несуществующего файла

def main():
    filename = r'files/' + input("Enter the file name: ") + '.txt'

    try:
        infile = open(filename, 'r')

        contents = infile.read()
        print(contents)
        infile.close()
    except IOError:
        print("File not found")

if __name__ == "__main__":
    main()