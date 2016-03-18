# -*- coding: utf-8 -*-

def reading_data():
    data = [[]]

    file1 = open("car-evaluation-dataset/car.data.txt","r")
    
    for line in file1:
        line = line.strip("\n")
        data.append(line.split(','))

    data.remove([])
    print "Total available data: ", len(data)
    
    file1.close()
    
    return data