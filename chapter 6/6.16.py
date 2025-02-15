# обработка нескольких исключений

def main():
    filename = r'files/' + input("Enter the file name: ") + '.txt'
    total = 0

    try:
        infile = open(filename, 'r')

        for line in infile:
            amount = float(line)
            total += amount

        infile.close()
        print(total)

    except IOError:
        print("File not found.")
    except ValueError:
        print("value is not an integer.")
    except:
        print("Something went wrong.")

if __name__ == "__main__":
    main()