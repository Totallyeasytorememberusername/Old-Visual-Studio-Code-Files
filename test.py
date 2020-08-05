matt_smells_bad_times_number_on_the_side = 8574

guess = input("Input something please! ")
if guess == "float":
    print("Works!")
if guess == "int":
    print("Works!")
if guess == "str":
    print("Fail. Wah wah wah...")

class Test: 
    a = matt_smells_bad_times_number_on_the_side
    
TestInstance = Test() 
  
print(isinstance(TestInstance, Test)) 
print(isinstance(TestInstance, (list, tuple))) 
print(isinstance(TestInstance, (list, tuple, Test)))

if isinstance("this is a string", str) == True:
    print("matt smells like poo yeah he does and if he says no he is a liar")