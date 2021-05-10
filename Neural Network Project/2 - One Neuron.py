### AUTHOR: TMRM   
### PROJECT: Neural Net - One Neuron 
### VER: 1.0
### DATE: 05-24-2020

### Declare CALLs ###



### Declare/Input VALs & STRINGs ###


#NB: Inputs can be true inputs into the system (such as a sensor) or input from a previous layer's outputs
inputs = [1, 2, 3, 2.5]

weights = [0.2, 0.8, -0.5, 1.0]

bias = 2

### CALCs ###

output = inputs[0]*weights[0] + inputs[1]*weights[1] + inputs[2]*weights[2]+ inputs[3]*weights[3] + bias

##OUTPUTs
print(output)
