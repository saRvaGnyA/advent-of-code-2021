import numpy as np

order_file = open('in1.txt', 'r')
order1 = order_file.read().split(',')
order_file.close()
order = []
for ord in order1:
    order.append(int(ord))
# print(order)

boards_file = open('in2.txt', 'r')
boards_in = boards_file.read().split('\n')
boards_file.close()

boards = []

for i in range(0, len(boards_in), 6):
    a = np.array([[boards_in[i].split()], [boards_in[i+1].split()], [boards_in[i+2].split()],
                  [boards_in[i+3].split()], [boards_in[i+4].split()]], dtype=int).reshape(5, 5)
    boards.append(a)

# print(boards)

positions = np.full_like(boards, fill_value=False, dtype=bool)
# print(positions)

the_board = []
the_positions = []
flag = True
iter = 0

for i in range(len(order)):

    # for in is immutable in python
    # for board, position in zip(boards, positions):
    #     for no_arr, pos_arr in zip(board, position):
    #         for no, pos in zip(no_arr, pos_arr):
    #             if(no == order[i]):
    #                 pos = True

    if(flag):
        for board_no in range(len(boards)):
            for arr_no in range(5):
                for no in range(5):
                    if(order[i] == boards[board_no][arr_no][no]):
                        positions[board_no][arr_no][no] = True

        for board_no in range(len(boards)):
            for arr_no in range(5):
                count_row = 0
                count_col = 0
                for no in range(5):
                    if(positions[board_no][arr_no][no] == True):
                        count_row += 1
                    if(positions[board_no][no][arr_no] == True):
                        count_col += 1
                if(count_row == 5 or count_col == 5):
                    the_board.append(boards[board_no])
                    the_positions.append(positions[board_no])
                    iter = order[i]
                    flag = False


print(the_board, the_positions)
sum = 0
for b_row, p_row in zip(the_board[0], the_positions[0]):
    for b, p in zip(b_row, p_row):
        if not p:
            sum += b
print(sum * iter)
