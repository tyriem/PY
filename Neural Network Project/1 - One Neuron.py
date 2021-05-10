### AUTHOR: TMRM   
### PROJECT: Neural Net - One Neuron 
### VER: 1.0
### DATE: 05-24-2020

### Declare CALLs ###



### Declare/Input VALs & STRINGs ###


#UNIQUE INPUTS INTO THE SYSTEM
inputs = [1.2, 5.1, 2.1]
#EVERY UNIQUE INPUT MUST HAVE A UNIQUE WEIGHT TO THEM
weights = [3.1, 2.1, 8.7]
#EVERY UNIQUE NEURON HAS ITS OWN UNIQUE BIAS
bias = 3

### CALCs ###

#ADD UP ALL THE INPUTS * THE WEIGHTS + THE BIAS
# NB WE DO THIS FROM THE BASE INDEX OF 0 then go forward (so this system will work at 0,1,2
output = inputs[0]*weights[0] + inputs[1]*weights[1] + inputs[2]*weights[2] + bias

##OUTPUTs
print(output)
