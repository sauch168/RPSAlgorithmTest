"rockpaperscissors.py"
Running the file will tell the user to use a specific move and prompts the user to enter the move that the
opponent made (in this test, the opponent is the CPU at this website: http://www.essentially.net/rsp/play.jsp).

This tests a fairly straightforward algorithm to attempt to win more rock paper scissors games; it takes the
latest short sequence of moves done by the player, and then searches the move history for the same pattern. 
Each time it finds the same sequence, it tallies the move that the computer made in response to that sequence.
The move that the computer made with the highest tally is the most likely move it will make next. Finally, 
the algorithm suggests that the player makes a move that beats the computer's predicted move.

"Rock Paper Scissors.txt" shows the results of playing normally. 
(Draw/Win/Loss is roughly even at 32/35/34.)
"Rock Paper Scissors Algorithm.txt" shows the results of playing with this algorithm.
(Wins happen much more often: D/W/L = 45/94/54.)