import json

class Scoreboard:
    
    def __init__(self):
        self.board={}

    def sort_all(self):
        """
        Sorts the entire scoreboard
        """
        for i in self.board.keys():
            temp = self.board[i]
            temp = sorted(temp, key=lambda x:int(x[1]), reverse=True)
            self.board[i] = temp

    def sort(self, game):
        """
        Sorts the scores of the given game
        Input
        (str) game: game name, whose scoreboard should be soted
        """
        
        if game not in self.board.keys():
            print("No such game found")
            return
    
        temp = self.board[game]
        temp = sorted(temp, key=lambda x:int(x[1]), reverse=True)
        self.board[game] = temp
    
    def add_entry(self, game, name, score):
        """
        Add a entry to the scoreboard
        Input
        (str) game: name of the game
        (str) name: player name, which will be saved
        (int) score: score, which will be saved
        """
        if game not in self.board.keys():
            self.board[game] = []
        self.board[game].append([name,score])
        self.sort(game)

    def remove_entry(self, game, name, score):
        """
        Removes a entry of the scoreboard
        Input
        (str) game: name of the game
        (str) name: player name
        (int) score: score
        """
        if game not in self.board.keys():
            print("No game found")
            return
        
        temp = self.board[game]
        if [name, score] not in temp:
            print("Entry not found")
            return
        
        temp.remove([name, score])
        self.board[game] = temp
    
    def remove_place(self, game, place):
        """
        Removes a entry of the scoreboard by the given place
        Input
        (str) game: name of the game
        (int) place: place whose entry is deleted
        """
        if game not in self.board.keys():
            print("No game found")
            return
        
        temp = self.board[game]
        place = place-1
        if place > len(temp):
            print("Place out of bounds")
            return
        
        del temp[place]
        self.board[game] = temp 

    def get_name_and_score(self,game,place):
        """
        Returns thse score of the given game and place
        Input
        (str) game: game name
        (int) place: scoreboard placement number starting with 1
        Output
        [(str),(int)]: list of [name, score], where name is the player name 
        and score the points scored during the game
        """
        place = place-1
        if len(self.board[game]) >= place:
            return self.board[game][place]
        
        print("Out of bounds")
        return (0,0)

    def get_number_of_entries(self,game):
        """
        Returns the number of entries of the specified game
        Input
        (string) game: game name
        Output
        (int) Number of different entries of the specified game
        """
        if type(game) != str:
            print("var 'game' has to be a from type str")
            return
        if game not in self.board.keys():
            return 0
        
        return len(self.board[game])
    
    def get_placement_ranging(self, game, start, stop):
        """
        Returns the entries for the specified placement range
        Input
        (str) game: game, whose entries shouldbe returned
        Output
        list of lists
        """
        result=[]
        start = start-1
        if start > stop:
            temp = start
            start = stop
            stop = temp
        
        if start < 0:
            print("Range out of Bounds")
            return
        if game not in self.board.keys():
            print("No game entries")
            return

        stop = min(len(self.board[game]),stop)
        for i in range(start,stop):
            result.append(self.board[game][i])
        
        return result

    def get_all_game_entries(self, game):
        """
        Retunrs all enries of the specified game
        Input
        (str) game: game, whose entries are being returned
        Output
        list of lists
        """
        if game not in self.board.keys():
            print("No such game found")
            return []

        return self.board[game]

    def get_all_entries(self):
        """
        Returns all entries saved in the scoreboard as a list
        Output
        list of lists
        """
        result = []
        for game in self.board.keys():
            result = result + self.get_all_game_entries(game)

        return result    

    def write_to_file(self, filename):
        """
        Saves the scoreboard as a json file
        Input
        (str) filename: the json file to be saved to e.g. test.json
        """
        with open(filename, "w+") as output_file:
            json.dump(self.board, output_file)


    def read_from_file(self, filename):
        """
        Loads the scoreboard from a json file
        Input
        (str) filename: the json file to be loaded from e.g. test.json
        """
        with open(filename) as input_file:
            self.board = json.load(input_file)

    def get_games(self):
        return self.board.keys()