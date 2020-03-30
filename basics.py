# 1. print
print("Hello world")
print("Hello " + "world")

message = "Hello there"
print(message)

# Syntax
# No semicolon
# Whitespace dependent!
# Tabs matter


# Primitive Data Types
# int, float, str, list, dictionary
int_example = 5
float_example = 7.4
string_example = "here's a string"
bool_example = True

list_example = ["First Item", "Second Item", "Third Item"]
print("list_example[0]: " + list_example[0])

dict_example = {
    "key": "value"
}
print("dict_example['key']: " + dict_example['key'])


# Control structures
# if, read "if ______ then _____".
# if condition:
#     # code goes here
if True:
    print("This is from within an if statement")

if not True:
    print("This won't ever run")

if 5 == 5:
    # This will run
    pass

if "test" == "test":
    # This will run
    pass

if False:
    # This won't run
    pass
else:
    # This will
    pass







# functions
def my_func():
    print("You called a function")

# Not called when created
# you need to call it
my_func()

# You can specify arguments for functions
def func_with_args(string):
    print("You gave the function: " + string)

# and pass values to those arguments
func_with_args("Here's a message")




# What you'll need for the lab

# be able to define a function
def a_function():
    # Create a dictionary
    my_dict = {
        "some_key": "some value",
        "some_other_key": "some over value"
    }
    # pass the dictionary to a function
    function_that_takes_a_dict(my_dict)



def function_that_takes_a_dict(dictionary):
    pass
