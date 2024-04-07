player_signs = ["X", "O"]
current_player_turn = player_signs[0]

def render_grid(grid):
    print("---------")
    for grid_row in grid:
        _grid_row = [' ' if g == '_' else g for g in grid_row]
        print("| " + " ".join(_grid_row) + " |")
    print("---------")


def analyze_game(grid):
    rows = grid
    cols = [list(col) for col in zip(*grid)]
    diagonals = [[grid[i][i] for i in range(3)], [grid[i][2 - i] for i in range(3)]]

    x_wins = any(line == ['X', 'X', 'X'] for line in rows + cols + diagonals)
    o_wins = any(line == ['O', 'O', 'O'] for line in rows + cols + diagonals)

    if x_wins:
        return "X wins"

    if o_wins:
        return "O wins"
    if any('_' in row for row in grid):
        return "Game not finished"

    return ""

def is_no_more_cell(grid):
    fill_count = 0
    total_cell = 0
    for row in grid:
        for cell in row:
            total_cell += 1
            if cell in player_signs:
                fill_count += 1

    return fill_count == total_cell


game_grid = [[" ", " ", " ", ], [" ", " ", " ", ], [" ", " ", " ", ]]

render_grid(game_grid)

while True:

    user_input = [num for num in input().split()]

    if len(user_input) != 2:
        continue

    if not user_input[0].isnumeric() or not user_input[1].isnumeric():
        print("You should enter numbers!")
        continue

    row = int(user_input[0]) - 1
    col = int(user_input[1]) - 1

    if row > len(game_grid) - 1:
        print("Coordinates should be from 1 to 3!")
        continue

    if col > len(game_grid[row]) - 1:
        print("Coordinates should be from 1 to 3!")
        continue

    current_value = game_grid[row][col]

    if current_value in player_signs:
        print("This cell is occupied! Choose another one!")
        continue

    game_grid[row][col] = current_player_turn
    current_player_turn = player_signs[0] if current_player_turn == player_signs[1] else player_signs[1]
    render_grid(game_grid)

    result = analyze_game(game_grid)

    if "win" in result:
        print(result)
        break

    if is_no_more_cell(game_grid):
        print("Draw")
        break
