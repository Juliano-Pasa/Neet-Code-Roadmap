from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            currentLine = set([])
            currentCol = set([])
            for j in range(9):
                if board[i][j] != '.' and board[i][j] in currentLine:
                    return False
                currentLine.add(board[i][j])

                if board[j][i] != '.' and board[j][i] in currentCol:
                    return False
                currentCol.add(board[j][i])

        for i in range(3):
            for j in range(3):
                currentSquare = set([])
                for row in range(3):
                    for col in range(3):
                        if board[i*3 + row][j*3 + col] != '.' and board[i*3 + row][j*3 + col] in currentSquare:
                            return False
                        currentSquare.add(board[i*3 + row][j*3 + col])
        return True