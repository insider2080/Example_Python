'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
                                Sum Function
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def SumFunction(input_list):
    return input_list[0]+input_list[1]+input_list[2];

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
                                Main Function
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("Input 3 numbers. Please separate numbers to enter.\nEx) 70 60 50");
#   Init array
input_list = [0, 0, 0];
#   Input 3 numbers using 'for'
for i in range(3):
    input_list[i] = input();
#   Call SumFunction
total = SumFunction(input_list);
#   Print total_value
print("Your number's sum is ", total);