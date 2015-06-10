'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
                                Sum Function
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def SumFunction(input_list):
    return input_list[0]+input_list[1];

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
                            Calculation Function
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def CalculateFuction(total):
    if(total != 10):
        print("You inputed wrong numbers. Please retry!");
    else:
        print("Congratulations!");

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
                                Main Function
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("Input 2 numbers. If 2number's sum is 10, you can exit from infinite loop.");
#   Init variable
total=0;
input_list = [0, 0];

#   Input 2 numbers using 'while'
while total != 10:
    for i in range(2):
        input_list[i] = input();
    total = SumFunction(input_list);
    CalculateFuction(total);