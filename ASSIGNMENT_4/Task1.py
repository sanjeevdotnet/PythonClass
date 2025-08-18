try:
    file1 = open('sample.txt', 'r')
    filedata = file1.readlines()
    file1.close()
    print('Reading File Content : ')
    if len(filedata) == 0:
        print('No data found in file')
    else:
        for line in filedata:
            LineNo = filedata.index(line)
            print('Line ',LineNo+1,':',line)
except FileNotFoundError:
    print('Error : The File \'sample.txt\' does not exist')

