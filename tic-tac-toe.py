import numpy as np
def Board(Array) :
    Array = Array.reshape(3, 3)
    print(Array)

Array=np.array([['1', '2', '3'] ,
                ['4','5','6'] ,
                ['7','8','9']
                ])

Array =Array.flatten()
b='start'
print('----> TIC TAC TOE <----')
print('')
Board(Array)
while b=='start':
    x=int(input('Enter A Number(from 1 to 9 ) As In Which Position You Want To Mark X  : '  ))
    Array[x - 1]= 'X'
    Board(Array)
    for i in range(0,2):

      if Array[i]== 'X' and Array[i]==Array[i + 3] and Array[i + 6]==Array[i]:
              b=print(' wins x')
              break
      elif Array[0]== 'X'  and Array[0]==Array[1] and Array[0]==Array[2] :
              b=print('x wins ')
              break
      elif  Array[0]== 'X' and Array[0]==Array[4] and Array[0]==Array[8] :
              b=print('x wins ')
              break
      elif  Array[2]== 'X' and Array[2]==Array[4] and Array[2]==Array[6] :
              b=print('x wins ')
              break
      elif i!=1 and i!=2 and  Array[i + 3]== 'X' and Array[i + 3]==Array[i + 4] and Array[i + 3]==Array[i + 5] :
              b=print(' x wins')
              break
      elif i!=1 and i!=2 and Array[i + 6]== 'X' and Array[i + 6]==Array[i + 7] and Array[i + 6]==Array[i + 8] :
              b=print(' x wins')
              break


    y = int(input('Enter A Number(from 1 to 9 ) As In Which Position You Want To Mark  Y  : ' ))
    Array[y - 1] = 'Y'
    Board(Array)
    for i in range(0, 2):

      if Array[i] == 'Y' and Array[i] == Array[i + 3] and Array[i + 6] == Array[i]:
              b=print('Y wins ')
              break
      elif Array[0] == 'Y' and Array[0] == Array[1] and Array[0] == Array[2]:
              b=print('Y wins ')
              break
      elif Array[0] == 'Y' and Array[0] == Array[4] and Array[0] == Array[8]:
              b=print('Y wins ')
              break
      elif Array[2] == 'Y' and Array[2] == Array[4] and Array[2] == Array[6]:
              b=print('Y wins ')
              break
      elif i != 1 and i != 2 and Array[i + 3] == 'Y' and Array[i + 3] == Array[i + 4] and Array[i + 3] == Array[i + 5]:
              b=print(' Y wins')
              break
      elif i != 1 and i != 2 and Array[i + 6] == 'Y' and Array[i + 6] == Array[i + 7] and Array[i + 6] == Array[i + 8]:
              b=print(' Y wins')
              break

    # if a[0]=='X' and a[0]==a[0] and a[8]==a[0]:
    #     print('x wins ')
    #     break
    # elif a[0]=='X' and a[0]==a[1] and a[2]==a[1]:
    #     print('x wins ')
    #     break
    # elif a[3]=='X' and a[3]==a[4] and a[5]==a[3]:
    #     print('x wins ')
    #     break
    # elif a[6]=='X' and a[6]==a[7] and a[8]==a[6]:
    #     print('x wins ')
    #     break
    # elif a[0]=='X' and a[0]==a[3] and a[6]==a[0]:
    #     print('x wins ')
    #     break
    # elif a[1]=='X' and a[1]==a[4] and a[7]==a[1]:
    #     print('x wins ')
    #     break
    # elif a[2]=='X' and a[2]==a[5] and a[8]==a[2]:
    #     print('x wins ')
    #     break
    # elif a[2]=='X' and a[2]==a[4] and a[6]==a[2]:
    #     print('x wins ')
    #     break


    # y=int(input())
    # a[y-1]='Y'
    # tab(a)
    # if a[0]=='Y' and a[0]==a[4] and a[8]==a[0]:
    #     print('Y wins ')
    #     break
    # elif a[0]=='Y' and a[0]==a[1] and a[2]==a[1]:
    #     print('Y wins ')
    #     break
    # elif a[3]=='Y' and a[3]==a[4] and a[5]==a[3]:
    #     print('Y wins ')
    #     break
    # elif a[6]=='Y' and a[6]==a[7] and a[8]==a[6]:
    #     print('Y wins ')
    #     break
    # elif a[0]=='Y' and a[0]==a[3] and a[6]==a[0]:
    #     print('Y wins ')
    #     break
    # elif a[1]=='Y' and a[1]==a[4] and a[7]==a[1]:
    #     print('Y wins ')
    #     break
    # elif a[2]=='Y' and a[2]==a[5] and a[8]==a[2]:
    #     print('Y wins ')
    #     break
    # elif a[2]=='Y' and a[2]==a[4] and a[6]==a[2]:
    #     print('Y wins ')
    #     break

















