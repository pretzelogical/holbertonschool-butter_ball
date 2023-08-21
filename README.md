# Butter Ball

The goal of the game is to butter the pancakes until they become 'butter-fied' and dissapear (this game takes places in a universe where 'butter-fied' things cease to exist)

How to play
./play.py or python3 play.py
arrow keys to move the paddle, spacebar to launch the ball

arguments:
./play.py test
draws test lines on the screen to help with positioning
prints collision event info in the console
press 'n' to go to the next rounds

## Program structure:
The game is managed by the `Game` object which in turn manages the paddle, the ball and the array of bricks.

Most of the collision code is in the ball
