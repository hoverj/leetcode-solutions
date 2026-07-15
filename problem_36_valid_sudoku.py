from typing import List


class Solution:

    def check3x3(self, row: int, col: int, board: List[List[str]]) -> bool:
        "Provided the top left row/col box checks if a 3x3 is valid"
        seen = set()

        for i in range(3):
            for j in range(3):
                value = board[row + i][col + j]
                if value == ".":
                    continue

                if value in seen:
                    return False

                seen.add(value)

        return True

    def checkRowOrCol(self, start: int, iden: str, board: List[List[str]]) -> bool:
        seen = set()
        if iden == "row":
            values = board[start]
        elif iden == "col":
            values = [board[r][start] for r in range(9)]
        else:
            raise ValueError(f"Iden {iden} not found")

        for value in values:
            if value == ".":
                continue

            if value in seen:
                return False
            seen.add(value)

        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for x in range(9):
            if not self.checkRowOrCol(start=x, iden="row", board=board):
                return False

            if not self.checkRowOrCol(start=x, iden="col", board=board):
                return False

        top_left_squares = [
            (0, 0),
            (0, 3),
            (0, 6),
            (3, 0),
            (6, 0),
            (3, 3),
            (3, 6),
            (6, 3),
            (6, 6),
        ]

        for row, col in top_left_squares:
            if not self.check3x3(row=row, col=col, board=board):
                return False

        return True
