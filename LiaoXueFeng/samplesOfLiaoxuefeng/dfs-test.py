class DfsTest:
    def exitst(self, board, word):
        if not word:
            return False
        visited = [[False for j in range(0, len(board))] for i in range(0, len(board[0]))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if(word[0] == board[i:j] && dfs(board, word, i,j,0)){
                    return true
                }





