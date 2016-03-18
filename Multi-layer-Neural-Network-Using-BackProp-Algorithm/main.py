# -*- coding: utf-8 -*-
import sample_main
import cancer_main
import car_main
import student_main
import balloon_main
import balance_main
import attribute
import neural_network
import create_pattern

def main():
    
    print "1 : Breast Cancer dataset"  
    print "2 : Car Evaluation dataset"
    print "3 : Student Performance dataset"
    print "4 : Balloon dataset"
    print "5 : Balance Scale dataset"
    
    
    user_input = input("Enter choice of dataset: ")
    
    
    #Reading the control file and associated data.
    if user_input == 0:
        ctrl_file = open("sample-dataset/control-file.txt","r")
        data = sample_main.reading_data()
    elif user_input == 1:
        ctrl_file = open("breast-cancer-dataset/control-file.txt","r")
        data = cancer_main.reading_data()
    elif user_input == 2:
        ctrl_file = open("car-evaluation-dataset/control-file.txt","r")
        data = car_main.reading_data()
    elif user_input == 3:
        ctrl_file = open("student-performance-dataset/control-file.txt","r")
        data = student_main.reading_data()
    elif user_input == 4:
        ctrl_file = open("balloon-dataset/control-file.txt","r")
        data = balloon_main.reading_data()
    elif user_input == 5:
        ctrl_file = open("balance-scale-dataset/control-file.txt","r")
        data = balance_main.reading_data()
    
    # list of all the attributes with their properties.
    attr_list = [] 
    for line in ctrl_file:
        line = line.strip('\n')
        words = line.split(" ")
        if(line[0] != "#"):        
            num = words[0]
            name = words[1]
            num_of_vals = words[2]
            obj = attribute.Attribute(num, name, num_of_vals)
            for x in words[3:]:
                obj.adding_values(x) 
            attr_list.append(obj)
         
    #copying target attribute from list of attributes seperately and removing it from the total list
    target_attr = attribute.Attribute(attr_list[-1].num, attr_list[-1].name, attr_list[-1].num_of_vals)
    for y in attr_list[-1].vals:
        target_attr.adding_values(y)
    print "Target attribute details:",
    target_attr.printvals()
    del attr_list[-1]

    pat = create_pattern.pattern(data, attr_list, target_attr)
    f_pat = []    
    for p in pat:
        f_pat.append(p)
    myNN = neural_network.NN(5, 10, 2)
    myNN.train(f_pat)

#    datasets = [[]]    
#    
#    valid_data_len = len(NN_data)*1/10 # dividing data into 10 sets.
#    j=0
#    for i in range(1,11): 
#        dat = []
#        for d in range(j,j+valid_data_len):
#            dat.append(NN_data[d])
#            j=j+1
#        i=i+1
#        datasets.append(dat)
#    datasets.remove([])
#    #print "it should be 10: ", len(datasets)
#
#    accuracy = []
#    errors = []
#    sizes = []
#    num = 1
#
#    for d in datasets:
#        print "***********Iteration", num, "***********"
#        num += 1
#        test_data = d
#        t_data = []
#        for left_d in datasets:
#            if left_d != d:
#                t_data = t_data + left_d
#    
#        #print "test data: ", len(test_data)
#    
#        #dividing data into training and pruning datasets.        
#        train_data_len = len(t_data)*6/10
#        prune_data = []
#        train_data = []
#        for d in range(0,train_data_len):
#            train_data.append(t_data[d])
#        for d in range(train_data_len, len(t_data)):
#            prune_data.append(t_data[d])
#            
#        #creating a neural network for training dataset.
#        neural_network.NN([len(attr_list), 10, int(target_attr.getvals()[2])])
#        # math = 0 and portugese = 1
#        for td in train_data:
#            
#            
#        
#        
#
#    #finding accuracy and confidence interval.
#    print "***********Statistics***********"
#    sum_acc = 0.0        
#    for acc in accuracy:
#        #print acc*100
#        sum_acc += (acc*100)
#    #print sum_acc
#    mean_acc = sum_acc/len(accuracy)
#    print "Mean accuracy: ", mean_acc
#    print "Mean Error rate: ", 100-mean_acc
#    sum_err = 0.0        
#    for err in errors:
#        #print err
#        sum_err += err
#    mean_err = sum_err/len(accuracy)
#    print "Mean Size of tree (before pruning):", max(sizes)
#    print "Mean Size of tree (after pruning):", min(sizes)    
#    print "Confidence Interval on Accuracy: [",(mean_acc-1.96*mean_err)," , ",(mean_acc+1.96*mean_err) , "]" 


if __name__ == '__main__':
    main()
        