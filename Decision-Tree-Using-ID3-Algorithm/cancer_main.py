# -*- coding: utf-8 -*-

def reading_data():
    data = [[]]

    file1 = open("breast-cancer-dataset/breast-cancer-wisconsin.data.txt","r")
    
    for line in file1:
        line = line.strip("\n")
        line = line.split(',')
        new_line = []
        for l in range(1,len(line)):
            new_line.append(line[l])
                
        #print new_line
        data.append(new_line)

    
    data.remove([])
    print "Total available data: ", len(data)
    
    file1.close()
    
    return data