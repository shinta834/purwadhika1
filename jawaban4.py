def hollow_triangle(x):
    col = x + 11
    for i in range (1,x+1):
        for j in range (1,col+1):
            if i == x or i+j == x+1 or i+j == x+2 or j-i == x or j-i == x+1:
                print ('*',end='')
            else:
                print (end=' ')
        print()

row= 10
hollow_triangle(row)
'''
            ***
           ** **  
          **   **
         **     **
        **       **
       **         **
      **           **
     **             **
    **               **
   *********************
'''