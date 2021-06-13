import random

class Snake:
    def __init__(self, snake_count, snake_locations):
        self.snake_count = snake_count
        self.snake_locations = snake_locations
        # """
        #     snake_location = {
        #                         "snake_id" : [start_pos, end_pos]
        #                      }
        # """

    def player_position_snake_bite(self, player_location):
        for snake in self.snake_locations:
            if player_location == self.snake_locations[snake][0]:
                return True, self.snake_locations[snake][1]
        return False, player_location

    def check_snake_at_player_location(self, player_location):
        for snake in self.snake_locations:
            if player_location == self.snake_locations[snake][0]:
                return True
        return False


class Ladder:
    def __init__(self, ladder_count, ladder_locations):
        self.ladder_count = ladder_count
        self.ladder_locations = ladder_locations

        # """
        #             ladder_location = {
        #                                 "ladder_id" : [start_pos, end_pos]
        #                              }
        #         """

    def check_ladder_at_player_location(self, player_location):
        for ladder in self.ladder_locations:
            if self.ladder_locations[ladder][0] == player_location:
                return True
        return False

    def player_location_ladder_climb(self, player_location):
        for ladder in self.ladder_locations:
            if self.ladder_locations[ladder][0] == player_location:
                return True, self.ladder_locations[ladder][1]
        return False, player_location


class Dice:
    def __init__(self, dice_count=1, dice_face=6):
        self.dice_count = dice_count
        self.dice_face = dice_face
        self.start_throw = 1
        self.last_throw = self.dice_face * self.dice_count

    def get_throw_number(self):
        return random.randint(self.start_throw, self.last_throw)

class Board:
    def __init__(self, start_pos=1, end_pos=100):
        self.start = start_pos
        self.last = end_pos

    def check_win(self, player_location):
        if player_location == self.last:
            return True
        else:
            return False


class Player:
    def __init__(self, player_count, player):
        self.player_count = player_count
        self.player = player

    def get_player_start_location(self, player_name):
        if self.player.get(player_name, None).get("start_pos", None):
            return self.player.get(player_name, None).get("start_pos", None)
        return 0

    def get_all_players(self):
        player_list = []
        for player in self.player:
            if self.player.get(player, None):
                player_list.append(self.player.get(player, None))
        return player_list


class SetupGame:
    def __init__(self,snake, ladder, dice, board, player):
        self.snake = snake
        self.ladder = ladder
        self.dice = dice
        self.board = board
        self.player = player
        self.win = False

    def play(self):
        currPosition = {}
        response = []
        player_service = Player(len(self.player), self.player)
        roll_service = Dice(self.dice.get("dice_count", 1), self.dice.get("dice_face", 6))
        players = player_service.get_all_players()
        snake_service = Snake(len(self.snake), self.snake)
        ladder_service = Ladder(len(self.ladder), self.ladder)
        board_service = Board(self.board.get("start_location",1),self.board.get("end_location", 100))
        while not self.win:
            for player in players:
                if player not in currPosition:
                    currPosition[player] = player_service.get_player_start_location(player)
                else:
                    currPosition[player] = currPosition[player] + roll_service.get_throw_number()
                    is_snake_bite, currPosition[player] = snake_service.player_position_snake_bite(currPosition[player])
                    is_ladder_climb, currPosition[player] = ladder_service.player_location_ladder_climb(currPosition[player])
                response.append("{} moved to {}".format(player, currPosition[player]))
                if board_service.check_win(currPosition[player]):
                    response.append("{} won".format(player))
                    self.win = True
                    break
        return response

