filename = 'output.txt'

try:
    A = input('Enter text to write to the file :')
    file1 = open(filename, 'w')
    Awriten = file1.write(A)
    file1.close()
    if int(Awriten) > 0: print('Data successfully written to \'',filename,'\'. \n')

    B = input('Enter additional text to append :')
    file1 = open(filename, 'a')
    file1.write('\n')
    Bwriten = file1.write(B)
    file1.close()
    if int(Bwriten) > 0: print('Data successfully appended. \n')

    file1 = open(filename, 'r')
    filedata = file1.readlines()
    file1.close()
    print('Final Content of ',filename,':')
    if len(filedata) == 0: print('No data found in file')
    else:
        for line in filedata:print(line)

except FileNotFoundError:
    print('Error : The File \'',filename,'\' does not exist')

