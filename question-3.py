p = input('Enter the number of rows')
q = int(p)
for i in range(q):     
    for j in range (0, (q -i - 1)): 
      print(' ', end = ' ') 
for k in range(0, 2 * i + 1):       
  print('*', end = "")
  
  print()  