### AUTHOR: TMRM   
### PROJECT: INTRO TO PYTHON - FUNCTIONS
### VER: 1.0
### DATE: 05-28-2020

##Declare CALLs & DEFs

### PARAMETERS ###
# Parameters are used to pass information to functions
# Parameters are specified after the function name, inside the parentheses. You can add as many parameters as you want, just separate them with a comma.

# The following ex. has a function with one parameter (fname). When the function is called, we pass along a first name,
# which is used inside the function to print the full name. Then we add the last name so that when we call the function
# it will attach the last name to whatever you put before.


def name_function(fname):
    print(fname + " Moss ")

name_function("Ann")
name_function("Edwin")
name_function("Tyrie")

### DEFAULT PARAMETER VALUE ###
# If we call the function without parameter, it uses the default value defined in the def statement

# The following ex. has a function with a default value, observe what happens when we call the function without a value and then with one.
def country_function(country = "INSERT COUNTRY HERE"):
    print ("I am from " + country)

country_function()
country_function("The Bahamas")
country_function("Cuba")
country_function("Jamaica")


### RETURN VALUES ###
# To let a function return a value, use the return statement

# The following ex. has a function with a return statement, NOTE THE INDENTATION ON THE RETURN STATEMENT
def num_function(x):
    return 5 * x

print(num_function(3))
print(num_function(5))
print(num_function(9))




