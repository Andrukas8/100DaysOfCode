import random
rock = '''
       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
'''

paper = '''
           ___..__
  __..--""" ._ __.'
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          """"----' 
'''

scissors = '''
               _  
      _       /<) 
     (>\     / / 
      \ \   / /  
       \ \ / /   
        \ V / Y-.
       /|     ` |
      | |       |
      |         |
      \         /
       |       | 
       |       | 
'''

joke = '''
                        _      USE 1, 2, 3        _
                       |_|                       |_|
                       | |         /^^^\         | |
                      _| |_      (| "o" |)      _| |_
                    _| | | | _    (_---_)    _ | | | |_
                   | | | | |' |    _| |_    | `| | | | |
                   |          |   /     \   |          |
                    \        /  / /(. .)\ \  \        /
                      \    /  / /  | . |  \ \  \    /
                        \  \/ /    ||Y||    \ \/  /
                         \__/      || ||      \__/
                                   () ()
                                   || ||
                                  ooO Ooo  
'''

player_move = int(input("Your move: 1 for Rock, 2 for Paper 3 for Scissors\n"))

computer_move = random.randint(1, 3)

print("Player move:")
if player_move == 1:
    print(rock)
elif player_move == 2:
    print(paper)
elif player_move == 3:
    print(scissors)
else:
    print(joke)


print("Computer move:")
if computer_move == 1:
    print(rock)
elif computer_move == 2:
    print(paper)
elif computer_move == 3:
    print(scissors)


if player_move == 1:
    if computer_move == 1:
        print("Draw")
    elif computer_move == 2:
        print("Computer wins")
    elif computer_move == 3:
        print("Player wins")

elif player_move == 2:
    if computer_move == 1:
        print("Player wins")
    elif computer_move == 2:
        print("Draw")
    elif computer_move == 3:
        print("Computer wins")


elif player_move == 3:
    if computer_move == 1:
        print("Computer wins")
    elif computer_move == 2:
        print("Player wins")
    elif computer_move == 3:
        print("Draw")
else:
    print("Player made an incorrect move")
