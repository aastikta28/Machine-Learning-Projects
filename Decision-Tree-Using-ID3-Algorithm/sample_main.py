# -*- coding: utf-8 -*-

def reading_data():
    por_data = [[]]

    por_file = open("sample-dataset/student-por.csv","r")

    next(por_file)

    for line in por_file:
        line = line.strip("\n")
        line = line + ';"Portuguese"'
        por_data.append(line.split(';'))

    por_data.remove([])
    
    mat_data = [[]]

    math_file = open("sample-dataset/student-mat.csv","r")

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
    
    
    data = por_data + mat_data        
    print len(data)
    
    por_file.close()
    math_file.close()
    
    return data# -*- coding: utf-8 -*-

