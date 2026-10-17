import pytest

from problem_04 import candidates, fill_singles

PUZZLE = """
5 3 0 0 7 0 0 0 0
6 0 0 1 9 5 0 0 0
0 9 8 0 0 0 0 6 0
8 0 0 0 6 0 0 0 3
4 0 0 8 0 3 0 0 1
7 0 0 0 2 0 0 0 6
0 6 0 0 0 0 2 8 0
0 0 0 4 1 9 0 0 5
0 0 0 0 8 0 0 7 9
"""

SOLVED = """
5 3 4 6 7 8 9 1 2
6 7 2 1 9 5 3 4 8
1 9 8 3 4 2 5 6 7
8 5 9 7 6 1 4 2 3
4 2 6 8 5 3 7 9 1
7 1 3 9 2 4 8 5 6
9 6 1 5 3 7 2 8 4
2 8 7 4 1 9 6 3 5
3 4 5 2 8 6 1 7 9
"""

# 후보가 하나뿐인 칸이 한 군데도 없는 어려운 퍼즐
HARD = """
8 0 0 0 0 0 0 0 0
0 0 3 6 0 0 0 0 0
0 7 0 0 9 0 2 0 0
0 5 0 0 0 7 0 0 0
0 0 0 0 4 5 7 0 0
0 0 0 1 0 0 0 3 0
0 0 1 0 0 0 0 6 8
0 0 8 5 0 0 0 1 0
0 9 0 0 0 0 4 0 0
"""

# SOLVED 에서 이 네 칸(6 7 / 7 6)을 비우면 서로 바꿔 넣어도 규칙에 맞아
# 후보가 둘씩 남고, 혼자서는 절대 채워지지 않습니다.
SWAP_CELLS = [(0, 3), (0, 4), (3, 3), (3, 4)]


def grid(text):
    return [[int(x) for x in line.split()] for line in text.strip().splitlines()]


@pytest.mark.parametrize(
    "r, c, expected",
    [
        (0, 2, {1, 2, 4}),
        (4, 4, {5}),
        (8, 0, {1, 2, 3}),
        (2, 0, {1, 2}),
        (0, 0, set()),  # 이미 채워진 칸
        (8, 8, set()),
    ],
)
def test_candidates(r, c, expected):
    board = grid(PUZZLE)
    result = candidates(board, r, c)
    assert isinstance(result, set)
    assert result == expected
    assert board == grid(PUZZLE)  # candidates 는 판을 바꾸지 않습니다


def test_candidates_on_empty_board():
    board = [[0] * 9 for _ in range(9)]
    assert candidates(board, 4, 4) == {1, 2, 3, 4, 5, 6, 7, 8, 9}


def test_fill_singles_solves_easy_puzzle():
    board = grid(PUZZLE)
    assert fill_singles(board) == 51
    assert board == grid(SOLVED)


def test_fill_singles_modifies_the_same_board():
    board = grid(PUZZLE)
    same = board
    fill_singles(board)
    assert same == grid(SOLVED)


def test_fill_singles_on_full_board():
    board = grid(SOLVED)
    assert fill_singles(board) == 0
    assert board == grid(SOLVED)


def test_fill_singles_single_blank():
    board = grid(SOLVED)
    board[4][4] = 0
    assert fill_singles(board) == 1
    assert board == grid(SOLVED)


def test_fill_singles_stops_on_hard_puzzle():
    board = grid(HARD)
    assert fill_singles(board) == 0
    assert board == grid(HARD)


def test_fill_singles_leaves_undecidable_cells_blank():
    board = grid(SOLVED)
    for r, c in SWAP_CELLS:
        board[r][c] = 0
    assert fill_singles(board) == 0
    for r, c in SWAP_CELLS:
        assert board[r][c] == 0
        assert candidates(board, r, c) == {6, 7}


def test_fill_singles_fills_what_it_can():
    board = grid(SOLVED)
    for r, c in SWAP_CELLS:
        board[r][c] = 0
    extra = [(8, 8), (4, 4), (0, 8)]
    for r, c in extra:
        board[r][c] = 0
    assert fill_singles(board) == 3
    solved = grid(SOLVED)
    for r, c in extra:
        assert board[r][c] == solved[r][c]
    for r, c in SWAP_CELLS:
        assert board[r][c] == 0
