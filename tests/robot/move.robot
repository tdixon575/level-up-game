***Settings***
Documentation: I want to move my character. If they attempt to move past a boundary, the move results in no change in position.
Test Template: Move Character
Library: MoveLibrary.py

***Test Cases***                 StartingX  StartingY  Direction  EndingX  EndingY
Move in middle of board a        5          5          N          5        6
Move in middle of board b        9          6          E          10       6
Move in middle of board c        6          5          S          6        4
Move in middle of board d        3          2          W          2        2
Move on edge of the board e      8          10         N          8        10
Move on edge of the board f      1          7          W          1        7
Move on edge of the board g      10         8          E          10       8
Move on edge of the board h      6          1          S          6        1      

***Keywords***
Move character
[Arguments]      ${startingX}   ${startingY}  ${direction}   ${endingX}   ${endingY}
Initialize character xposition with ${startingX}
Initialize character yposition with ${startingY}
Move in direction                   ${direction}
Character xposition should be       ${endingX}
Character yposition should be       ${endingY}