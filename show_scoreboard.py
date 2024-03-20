from displaying_characters import display_chars

def display_scoreboard(game, draw, scoreboard):

    placements = scoreboard.get_placement_ranging(game,1,5)
    place = 1
    for score in placements:
        y_cords = 6*(place-1)
        displaying_charas(str(place)+" "+ str(score),y_cords, 1,draw)
        place = place+1
