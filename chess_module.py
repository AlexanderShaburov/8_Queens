import sys
if __name__ == '__main__': 
    print('[INFO]: Incorrect module call.')
    sys.exit()
    
    
class Chess():
    def __init__(self) -> None:
        self.board = set()
        self.solutions = set()
        self.solutions_cleared = set()
  
    def clear_solutions(self):
        '''
        Check all found solutions for dependency, delete all derivatives and
        save independent solutions to: self.solution_cleared
        '''
        while 0 < len(self.solutions):#while we check and clear all solutions
            next_solution = self.solutions.pop()
            self.board = next_solution
            for _ in range(3):
                self.turn_90()
                self.look_and_clear()
            self.board = next_solution
            self.flip_horizontal()
            self.look_and_clear()
            for _ in range(3):
                self.turn_90()
                self.look_and_clear()
            self.solutions_cleared.add(next_solution)            
        pass
    
    def look_and_clear(self):
        if self.board in self.solutions:
            self.solutions.remove(self.board)
        return
    
    def save_queens(self, queens:list[list]):
        '''
        Save obtained solution to storage self.solutions
        '''
        self.board = set()
        #convrt list[list] to set(tuples)
        for queen in queens: self.board.add(tuple((queen[0], queen[1])))
        #save solution
        self.solutions.add(frozenset(self.board))
        pass
           
    def flip_horizontal(self):
        '''
        Flip solution saved in self.board horizontal.
        '''
        new_board = set()
        for queen in self.board:
            new_board.add((queen[0], 7 - queen[1]))
        self.board = new_board
        
    def turn_90(self):
        '''
        Turn solution saved in self.board on 90 degrees clockwise
        '''
        new_board = set()
        for queen in self.board:
            new_board.add((7 - queen[1], queen[0]))
        self.board = new_board


        
    
storage = Chess()
