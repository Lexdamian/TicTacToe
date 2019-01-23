board = [
  0, 1, 2,
  3, 4, 5,
  6, 7, 8  
]

xIsNext = True
winner = False

def draw():
  print(board[0], board[1], board[2])
  print(board[3], board[4], board[5])
  print(board[6], board[7], board[8])
  print()

def isWinner():
  if board[0] == board[1] and board[0] == board[2]:
    return True
  if board[3] == board[4] and board[0] == board[5]:
    return True
  if board[6] == board[7] and board[6] == board[8]:
    return True
  if board[0] == board[3] and board[0] == board[6]:
    return True
  if board[1] == board[4] and board[1] == board[7]:
    return True
  if board[2] == board[5] and board[2] == board[8]:
    return True
  if board[0] == board[4] and board[0] == board[8]:
    return True
  if board[2] == board[4] and board[2] == board[6]:
    return True

# 1. X va incepe
# 2. X alege un index din array
# 3. verifici daca valoarea de la index este libera
# 4. randul lui O
# 5. verifica castigator dupa fiecare mutare
# 6. reia pana la final
# 7. determine winner 

# Start
draw()

while(not winner):
  if xIsNext: 
    player = 'X' 
  else:
    player = 'O'

  print('It\'s ', player, '\'s turn')
  index = int(input("Choose position: "))
  # print('index=>', index)
  type(index)

  if type(board[index]) is not int:
    print('Choose another postion!')
    continue
    
  board[index] = player

  draw()

  if isWinner():
    winner = True
    print('Winner is ', player)

  xIsNext = not xIsNext

