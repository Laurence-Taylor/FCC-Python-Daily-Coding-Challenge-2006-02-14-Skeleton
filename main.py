def get_difficulty(track):
    doble_turn = ['R', 'L']
    pos_ant = track[0]
    difficulty = 0
    for i in range(1,len(track)):
        if pos_ant != track[i]:
            if pos_ant in doble_turn and track[i] in doble_turn:
                difficulty += 15
            else:
                difficulty += 5
        pos_ant = track[i]
    print(difficulty)
    if 0 <= difficulty <= 100:
        return "Easy"
    elif 101 <= difficulty <= 200:
        return "Medium"
    else:
        return "Hard"

if __name__ == '__main__':
    print(get_difficulty("SRSLSRSLSRRSLSRSRSLSRLSRSR"))
    #print()
    #print(get_difficulty("LLRSLRLRSLLRLRSLRRLRSRLLS"))
    #print()
    #print(get_difficulty("SRRRRLSLLRLRSSRLSRL"))