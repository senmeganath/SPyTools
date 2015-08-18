__author__ = 'Senthilkumar Meganathan'

def splitFile():
    try:
        filename = raw_input("Enter the File Name : ")
        lineSplit = raw_input("Enter the Split file Size: ")
        print "Opening the file..."
        target = open(filename, 'r')
        lineCount = 0
        splitCount = 0
        output = open('out' + str(splitCount) + '.sen', 'w')
        while 1:
            line = target.readline()
            if not line:
                break
            lineCount += 1
            if lineCount == int(lineSplit):
                output.close()
                splitCount += 1
                print 'File out' + str(splitCount) + ".sen created"
                output = open('out' + str(splitCount) + '.sen', 'w')
                lineCount = 0
            output.write(line)
        target.close
    except Exception as e:
        print str(e)

if __name__ == "__main__":
    splitFile()
