for j in range (1,101):
  if j>1:
      for num in range (2,j):
          if (j%num)==0:
              break
      else:
              print(j)
