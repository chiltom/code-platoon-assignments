# Features:

## High Level Features:
- Human Player turn.
- Computer Player turn.
- Getting human player input.
- Printing the board for the human player to see.
- Check after every move to see if:
  - Someone won.
  - Cats game.

With computer AI we can do player vs. computer. We'd like it to be smart, but we can start with it being dumb and simple.

## User input:
- User inputs their move for each turn:
      - Maybe we do this by user inputting row and column for their move.
- Ask the user if they want to be "x" or "o".

We want to show the board with the current state of the game.

## Flow of game:
  - Who goes first? Player A.
  - Player A makes their move.
  - Now it's Player B's turn, and player B makes their move.
  - ... and so on ...

## Human Player:
- Need to be able to see the board
- Prompt for their move
  - We need to tell the user how to enter their move

## Computer Player:
- No need to print out board, but needs to be able to know spots available,
  or, needs to know how to generate a move