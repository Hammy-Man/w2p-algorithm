# get a string of 0's and 1's 
# parse said string, zeros are occupied urinals, 1's are unoccupied urinals
inputp = input("input str \n")
#check validity of string
left = " "
i = -1
while i < len(inputp) -1:
  i += 1
  if inputp[i] == "#":
    continue
  elif inputp[i] == "-":
    continue
  else:
    print("invalid string")
    exit(1)
i= -1
while i < len(inputp) -2:
  i +=1    # if the spots before and after are open, return the middle of those two spors pos in the string + 1
  if inputp[i] == "-":
    if inputp[i-1] == "-":
      if inputp[i+1]  == "-":
        print(i+1)
      else:
        continue
    else: 
      continue
  else:
    left = "#"
    continue
if inputp[len(inputp) -1] == "-":
  print(len(inputp)) ## out of index range ?