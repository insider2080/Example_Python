'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
                               Recursive Function
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def RecursiveFunction(i, count, index1, index2):
    if (count == 0):
        return;
    else:
        RecursiveFunction(i, count-1, index1, index2);
        PrintFunction(i, count, index1, index2);

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
                                Print Function
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def PrintFunction(i, count, index1, index2):
    if (i == 0):
        print("\t'0%d': {"%count);
    elif (i == 1):
        if (count != index2):
            print("\t\t'0%d-0%d': None,"%(index1, count));
        else:
            print("\t\t'0%d-0%d': {"%(index1, count));
    elif (i == 2):
        print("\t\t\t'0%d-0%d-0%d': None,"%(index1, index2, count));

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
                                 Main Function
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("tree = {");
num_list = [1, 5, 4];

#   Call RecursiveFunction
for i in range(3):
    RecursiveFunction(i, num_list[i], num_list[0], num_list[1]);

print ("\t\t}");
print ("\t}");
print ("}");