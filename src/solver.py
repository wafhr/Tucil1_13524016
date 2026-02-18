import os
total_cases = 0

def isValid(queen_pos, color_list, N):
    """
    Validasi ratu dengan aturan:
    - Satu queen pada tiap daerah warna
    - Tidak ada queen yang saling berdekatan baik vertikal, horizontal, maupun diagonal
    """
    used_colors = set()
    for r in range(N):
        c = queen_pos[r]
        color = color_list[r][c]
        if color in used_colors:
            return False
        used_colors.add(color)
        if r > 0:
            prev_c = queen_pos[r-1]
            if abs(c-prev_c) <= 1:
                return False

    return True

def placeQueens(board, color_list, N, live_update=None, queen_pos=None, available_pos=None):
    """
    Meletakkan berbagai kemungkinan ratu pada baris dan kolom berbeda
    """
    global total_cases
    if queen_pos == None:
        queen_pos = []
        total_cases = 0
    if available_pos == None:
        available_pos = list(range(N))
    
    if len(queen_pos) == N:
        total_cases += 1
        if live_update:
            for r in range(N):
                for c in range(N):
                    board[r][c] = '.'
            for r in range(N):
                board[r][queen_pos[r]] = '#'
            live_update(board,total_cases)
        if isValid(queen_pos, color_list, N):
            for r in range(N):
                for c in range(N):
                    board[r][c] = '.'
            for r in range(N):
                board[r][queen_pos[r]] = '#'
            return True
        return False
    
    for row in range(len(available_pos)):
        col = available_pos[row]
        next_pos = queen_pos + [col]
        next_available = available_pos[:row] + available_pos[row+1:]
        if placeQueens(board, color_list, N, live_update,next_pos,next_available):
            return True
    return False

def readFile(path):
    """ 
    Membaca konten file txt
    Mengembalikan tuple -> (colorList, N)
    colorList: 2D List berisi region warna
    N: Ukuran grid
    """
    if not os.path.exists(path):
        return None, 0
    color_list = []
    with open(path) as f:
        for line in f:
            noSpace = line.strip()
            if noSpace:
                color_list.append(list(noSpace))
    N = len(color_list)
    if N == 0:
        return None, 0
    for i in range(N):
        if len(color_list[i]) != N:
            return None, 0
    
    return color_list, N

def copyBoard(color_list):
    """
    Membuat salinan colorList untuk menyimpan pencarian solusi
    """
    board = []
    for row in color_list:
        board.append(row.copy())
    return board