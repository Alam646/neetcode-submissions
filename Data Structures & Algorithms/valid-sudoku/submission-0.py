class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        dupes = {}


        #checking each row
        for row in range(len(board)):
            dupes["row"] = []
            for col in range(len(board)):
                if board[row][col] != ".":
                    if board[row][col] in dupes["row"]:
                        return False
                    else:
                        dupes["row"].append(board[row][col])
                else:
                    continue


        #checking each col
        for row in range(len(board)):
            dupes["col"] = []
            for col in range(len(board)):
                if board[col][row] != ".":
                    if board[col][row] in dupes["col"]:
                        return False
                    else:
                        dupes["col"].append(board[col][row])
                else:
                    continue

        #checking each box (3x3)
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] == ".":
                    continue
                if (row//3 , col//3) not in dupes:
                    dupes[(row//3 , col//3)] = []
                    if board[row][col] in dupes[(row//3 , col//3)]:
                        print(board[row][col])
                        print(dupes[(row//3 , col//3)])
                        return False
                    else:
                        dupes[(row//3 , col//3)].append(board[row][col])
                else:
                    if board[row][col] in dupes[(row//3 , col//3)]:
                        print(board[row][col])
                        print(dupes[(row//3 , col//3)])
                        return False
                    else:
                        dupes[(row//3 , col//3)].append(board[row][col])
        
        return True








