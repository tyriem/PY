### AUTHOR: TMRM   
### PROJECT:INTRO TO PYTHON - BANK ACCOUNT
### VER: 1.0
### DATE: 05-21-2020

##Declare CALLs


##Declare/Input VALs & STRINGs


raw_balance = input("Input The Account Balance: ")
balance = int(raw_balance.replace("$",""))


##CALCs
if balance < 0:
   print("Your Balance Is Below 0, Add Funds Now Or You Will Be Charged A Penalty")

elif balance == 0:
   print("Your Balance Is Equal to 0, Add Funds Soon")

else:
   print("Your Balance Is 0 Or Above")

