# -*- coding: utf-8 -*-

def reading_data():
    por_data = [[]]

    por_file = open("student-performance-dataset/student-por.csv","r")

    next(por_file)

    for line in por_file:
        line = line.strip("\n")
        line = line + ';"Portuguese"'
        por_data.append(line.split(';'))

    por_data.remove([])
    
    mat_data = [[]]

    math_file = open("student-performance-dataset/student-mat.csv","r")

    next(math_file)

    for line in math_file:
        line = line.strip('\n')
        line = line + ';"Math"'
        mat_data.append(line.split(';'))

    mat_data.remove([])
 
#    mat_rem = []
#    por_rem = []
    #noise removal.
#    for line in mat_data:
#        for chk in por_data:
#            if all(x in chk for x in [line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9], line[10], line[19], line[21]]):            
#                por_rem.append(por_data.index(chk))
#        mat_rem.append(mat_data.index(line))

#    print len(mat_rem)
#    
#    print len(por_rem)
    
    data = []
    i = 0
    while(i < len(por_data) and i < len(mat_data)):
        if all(x in por_data[i] for x in [mat_data[i][0], mat_data[i][1], mat_data[i][2], mat_data[i][3], mat_data[i][4], mat_data[i][5], mat_data[i][6], mat_data[i][7], mat_data[i][8], mat_data[i][9], mat_data[i][10], mat_data[i][19], mat_data[i][21]]): 
            i = i+1
        else:
            data.append(por_data[i])
            data.append(mat_data[i])
            i = i+1
        #print "new" , i
    if(i < len(por_data)):
        while(i < len(por_data)):
            #print "new" , i            
            data.append(por_data[i])
            i += 1
    if(i < len(mat_data)):
        #print "new" , i
        while(i < len(mat_data)):
            data.append(mat_data[i])
            i += 1
    print "Total available data: ", len(data)
    
    por_file.close()
    math_file.close()
    
    return data