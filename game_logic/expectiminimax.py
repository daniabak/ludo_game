import math

class Expectiminimax:
    def __init__(self, depth):
        self.depth = depth 

    

    def max_move(self, board, depth, player):
        """
        تابع مسؤول عن تحركات Max Player.
        """
        if depth == 0 or board.check_win()==True:
            return board.evaluate_board(board, player)

        max_eval = -math.inf
        for dice_value in range(1, 7):  
            next_states = board.next_state(dice_value,  False)
            for state in next_states:
                eval = self.min_move(state[0], depth - 1, player)
                max_eval = max(max_eval, eval)
        return max_eval

    def min_move(self, board, depth, player):
        
        if depth == 0 or board.check_win() == True:
            return board.evaluate_board(board, player)

        total_eval = 0
        for dice_value in range(1, 7):
            next_states = board.next_state(dice_value, False)
            if not next_states:
                continue
            probability = 1 / 6 
            for state in next_states:
                eval = self.max_move(state[0], depth - 1, player)
                total_eval += probability * eval
        return total_eval

    def get_best_move(self, board, player, dice_value):
    
      best_move_index = None
      best_value = -math.inf

      next_states = board.next_state(dice_value,  False)

      for index, state in enumerate(next_states):
            move_value = self.max_move(state[0], self.depth - 1, player)
            if move_value > best_value:
                  best_value = move_value
                  best_move_index = state[1]

      return best_move_index

