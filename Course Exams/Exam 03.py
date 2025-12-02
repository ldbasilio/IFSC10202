# You may use previous assignments, notes, books, or the internet for the exam. However, 
# copying a solution that does not solve the assignment will result in a zero.
# You may NOT consult with another student.
# The exam is due at precisely 11am. At that time, the exam will disappear 
# from Blackboard and you will not be able to submit your work, resulting in a zero.

'''Quite often, children have to settle a dispute using a game called Winners and Losers. 
To play the game:

- One child is chosen as “even” and the other child is chosen as “odd”.
- When a child yells “Ready”, both children hold up a number of fingers on a hand.
- Add up the numbers finger shown by both children,
    - If the sum is even, then the “even” child scores a point
    - If the sum is odd, then the “odd” child scores a point
- The game is played five times, and the child with the most number of points wins the game.


Write a python program that simulates the Winners and Loser game. One player will be the 
“human” which will be “even”. The other player will be the “computer” which will be “odd”.

- Display the Title of the game (10 points) (Hint: use a print statement)
- Play the game for 5 rounds (10 points) (Hint: use a FOR Loop for 5 rounds)
- Display the playing round (Round 1, Round 2, ….) (10 points) (Hint: use a print 
statement with a .format method)
- Prompt the “human” to enter a number between 1 and 5 (10 points) (Hint: use an input 
statement)
- Have the “computer” generate a random number between 1 and 5 (See Unit 5) (10 points)
 (Hint: use randint)
- If the sum of the “human” and “computer” guess is even, then the human wins a point. If 
the sum of the “human” and “computer” guess is odd, then the computer wins a point (20 
points) (Hint: use remainder division by 2 to determine if the number is even or odd. You 
will also need an if...then...else statement and a print statement)
- Display the “human” guess and the “computer” guess (20 points) (Hint: use a print statement
 with a .format method)
- Display whether or not the sum is even or odd (“Sum is Even” or “Sum is Odd” (20 points)
 (Hint: use an if...then...else statement and a print statement)
- Display the “human” score and the “computer” score (20 points) (Hint: use a print statement)
- After 5 plays, display “Human Wins” if the “human” has the most number of points, else 
display “Computer Wins” if the “computer” has the most number of points (20 points) (Hint: 
use an if statement and a print statement)'''

from random import randint
print ("Welcome to the ''Winners and Losers'' game! For this to work, please remember:\n- Human is Even\n- Computer is Odd")

Human = str("Human Guess: ")
Computer = str(" - Computer Guess: ")
scoreX = 0
scoreY = 0

for i in range(1, 6):
    round = 0
    print ("\nRound " + str(i))
    x = int(input("Enter your guess: "))
    y = randint(1, 4)
    total = x + y
    if total % 2 == 0:
        print (Human + str(x) + Computer + str(y))
        print ("Sum is Even")
        scoreX += 1
    else:
        print (Human + str(x) + Computer + str(y))
        print ("Sum is Odd")
        scoreY += 1
    round + 1
    print ("Human Score is: " + str(scoreX) + " - Computer Score is: " + str(scoreY))
if scoreX > scoreY:
        print ("Human wins!")
else:
        print("Computer wins!")