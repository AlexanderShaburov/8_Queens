
import copy, datetime,sys
from chess_module import storage

if __name__ == '__main__':
    print('[INFO]: Incorrect module call.')
    sys.exit()

def tag_attack(number, letter, board):
    #puts queen on board ans tags all attacked fiealds and return board
    for row in range(8):
        for col in range(8):
            if (row == number or #on same colomn
                col == letter or #on same row
                row + col == number + letter or #on negative diag. line
                row - col == number - letter): #on positive diag. line
                board[row][col] = True #tag board as attacked
    return board

def rebuild_game_board(queens) -> list[list]:
    #restore board with current queens from queens
    board = [[False for _ in range(8)] for _ in range(8)] #empty board
    for queen in queens: 
        #tag attacked fields for every queen
        board = tag_attack(queen[0], queen[1], board)
    return board
        
# exclude attaked rows and columns from search erea
def define_search_zone(queens):
    letters = list(range(8))
    numbers = list(range(8))
    for queen in queens:
        letters.remove(queen[0])
        numbers.remove(queen[1])
    return letters, numbers


def put_next_queen(queens: list[list]):   

    # Create game board with all fields under attack taged
    game_board = rebuild_game_board(queens)
    #define search erea by excluding all rows and cols alrady taken by queens
    letters_range, numbers_range = define_search_zone(queens)
    #find not attacked field for next queen
    for letter in letters_range:
        for number in numbers_range:
            #check if the field under attack
            if game_board[letter][number]: continue #continue search
            # add new queen to queens list
            queens.append([letter, number])
            #check if set lenth < 8 go to recurtion, else we got full solusion
            if len(queens) < 8: put_next_queen(copy.deepcopy(queens))
            #add to depository
            else: storage.save_queens(queens)
            #anyway if we come from recurtion or just found full solution
            #remove last queen from silution
            del queens[-1]
            #contione search
            continue
        pass
    #when all variants checked return to previos level
    else: return 




def start():
    queens = []
    start_time = datetime.datetime.now()
    #find all solutions
    put_next_queen(queens)
    #from all solutions select independent ones
    storage.clear_solutions()
    
    print(storage.solutions_cleared)
    print(len(storage.solutions_cleared))
   
    print('[INFO]: Program duration is: ', datetime.datetime.now() - start_time)





