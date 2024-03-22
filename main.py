stdform = input('Enter a number in scientific notation: ')
stdform = stdform.strip()

# Type your code below
check = 0
mantissa = ''
exponent = ''
if "x10^" in stdform:
  mantissa = stdform.split("x10^")[0]
  exponent = stdform.split("x10^")[1]
  check += 0
  if mantissa.count(".") > 1:
    check += 1
  elif exponent.count(".") > 0:
    check += 1
  elif not mantissa.replace(".",'').replace("-","").isdigit():
    check += 1
  elif not exponent.replace("-","").isdigit():
    check += 1
else:
  check += 1

if check == 0:
  print(f"This number in E notation is {mantissa}E{exponent}.")
else:
  print("Error converting to scientific E notation.")
  
    
    