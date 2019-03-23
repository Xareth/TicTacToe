# TicTacToe
By Xareth 2019*
<h2>Machine Learning by Beginner</h2>
<p>This is my 1st program created in python and uploaded to GitHub. 
I have decided to create something fancy enough to be admired and simple 
enough to show beginners that it is possible to create usefull programs in the 
 beginning of their carriers</p>
 
<h2>What this program can do?</h2>
It is a simple Tic Tac Toe game. In order to turn on vs ai mode you have to 
change code a bit. Right now it is prepared to teach AI. However, if you 
want to play with it, just change function human_player_move(), variable choice
to int(input('write your choice from 1-9'))

<h2>How to use it?</h2>
Just run main.py, and your AI will start learning. If you want to see how your AI
works without any knowledge, just delete data in files 'wins.csv' and 'loses.csv.
Then, ai will start from the beginning. <br><br>
In order to reset score, just change 'score.csv' file: (you can copy it from below) <br>
games<br>
0<br>
wins<br>
0<br>
loses<br>
0<br>
win ratio<br>
0<br>

<h2>How does it work?</h2>
<p>main.py - is a file where TicTacToe game is programmed. In the main function 
there is direct reference to ai.py<br></p>
<p>ai.py - is a file where all ai functions are writen </p>
<p>win / loses csv - are the files where Ai is storing it's knowledge. When deleted
AI is starting to learn from the beginnig.</p> 
<p>score.csv is the file which you can look in to see the current statistics of the
ai</p>
