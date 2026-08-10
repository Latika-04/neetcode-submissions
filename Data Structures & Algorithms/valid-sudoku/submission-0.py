class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Check rows
        for r in range(9):
            seen = set()
            for c in range(9):
                value = board[r][c]

                if value == ".":
                    continue

                if value in seen:
                    return False

                seen.add(value)

        # Check columns
        for c in range(9):
            seen = set()
            for r in range(9):
                value = board[r][c]

                if value == ".":
                    continue

                if value in seen:
                    return False

                seen.add(value)

        # Check 3x3 boxes
        for box_row in [0, 3, 6]:
            for box_col in [0, 3, 6]:
                seen = set()

                for r in range(box_row, box_row + 3):
                    for c in range(box_col, box_col + 3):
                        value = board[r][c]

                        if value == ".":
                            continue

                        if value in seen:
                            return False

                        seen.add(value)

        return True
        