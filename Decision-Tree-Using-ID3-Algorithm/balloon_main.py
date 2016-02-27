# -*- coding: utf-8 -*-

def reading_data():
    data = [[]]

    file1 = open("balloon-dataset/adult-stretch.txt","r")
    file2 = open("balloon-dataset/adult+stretch.txt","r")
    file3 = open("balloon-dataset/yellow-small.txt","r")
    file4 = open("balloon-dataset/yellow-small+adult-stretch.txt","r")
    
    for line in file1:
        line = line.strip("\n")
        data.append(line.split(','))

    for line in file2:
        line = line.strip("\n")
        data.append(line.split(','))

    for line in file3:
        line = line.strip("\n")
        data.append(line.split(','))

    for line in file4:
        line = line.strip("\n")
        data.append(line.split(','))

    data.remove([])
    print "Total available data: ", len(data)
    
    file1.close()
    file2.close()
    file3.close()
    file4.close()
    
    return data