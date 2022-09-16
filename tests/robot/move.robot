***Settings***
Documentation    I want to move my character. If they attempt to move past a boundary, the move results in no change in position.
Test Template    Move Character
Library          MoveLibrary.py

***Test Cases***                 StartingX  StartingY  Direction  EndingX  EndingY
Move in middle of board          5          5          n          5        6
Move in middle of board          9          6          e          10       6
Move in middle of board          6          5          s          6        4
Move in middle of board          3          2          w          2        2
Move on edge of the board        8          10         n          8        10
Move on edge of the board        1          7          w          1        7
Move on edge of the board        10         8          e          10       8
Move on edge of the board        6          1          s          6        1      

***Keywords***
Move character
    [Arguments]      ${startingX}   ${startingY}  ${direction}   ${endingX}   ${endingY}
    Initialize character position with  ${startingX}    ${startingY}
    Move in direction                   ${direction}
    Character position should be       ${endingX}   ${endingY}