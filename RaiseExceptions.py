

# raise custom errors using RAISE keyword


def main():
    try:
        for line in readFile('lines.doc'):
            print(line.strip())
    except IOError as e:
        print('cannot read file : ', e)
    except ValueError as e:
        print('bad file name : ', e)




def readFile(filename):
    if filename.endswith('.txt'):
        fh = open('xlines.txt')
        return fh.readlines()
    else:
        raise ValueError('Invalid file name. Filename must end with .txt')      #raise keyword to raise custom error




if __name__ == '__main__': main()

