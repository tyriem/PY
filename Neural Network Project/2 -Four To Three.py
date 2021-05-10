### AUTHOR: TMRM   
### PROJECT: Neural Net - Three Neurons
### VER: 1.0
### DATE: 05-24-2020

### OBJECTIVE ###
# Mapping 4 inputs to 3 outputs

### Declare CALLs ###



### Declare/Input VALs & STRINGs ###


#NB: Inputs can be true inputs into the system (such as a sensor) or input from a previous layer's outputs
inputs = [1, 2, 3, 2.5]

# We tune/tweak the weights and biases to push the neural net to certain outcomes, we never really tweak the input
# as it is the real data or previous input into the system
weights1 = [0.2, 0.8, -0.5, 1.0]
weights2 = [0.5, -0.91, 0.26, -0.5]
weights3 = [-0.26, -0.27, 0.17, 0.87]

bias1 = 2
bias2 = 3
bias3 = 0.5

### CALCs ###

# This matrix list takes the four inputs and outputs 3 outputs
output = [inputs[0]*weights1[0] + inputs[1]*weights1[1] + inputs[2]*weights1[2]+ inputs[3]*weights1[3] + bias1,
          inputs[0]*weights2[0] + inputs[1]*weights2[1] + inputs[2]*weights2[2]+ inputs[3]*weights2[3] + bias2,
          inputs[0]*weights3[0] + inputs[1]*weights3[1] + inputs[2]*weights3[2]+ inputs[3]*weights3[3] + bias3]

##OUTPUTs
print(output)
