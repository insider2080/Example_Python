'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
                                Sum Function
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def SumFunction(input_list):
    return input_list[0]+input_list[1];

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
                            Calculation Function
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def CalculateFuction(sum):
    if(sum != 10):
        print("You inputed wrong numbers. Please retry!");
    else:
        print("Congratulations!");

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
                                Main Function
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("Input 2 numbers. If 2 number's sum is 10, you can exit from infinite loop.");
#   Init variable
sum=0;
input_list = [0, 0];

#   Input 2 numbers using 'while'
while sum != 10:
    for i in range(2):
        input_list[i] = input();
    sum = SumFunction(input_list);
    CalculateFuction(sum);