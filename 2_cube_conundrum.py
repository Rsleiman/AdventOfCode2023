max_balls = {"red":12, "green":13, "blue":14}

with open("cube_conundrum.txt") as file:
    txt = file.read()

lines = txt.split("\n")
output = []
for line in lines:
    # Extract game_id
    game_id = int(line.split(":")[0].split(" ")[1])
    # Extract subgames
    game = line.split(":")[1].split(";")
    # set possible to True
    possible = True


    for subgame in game:
    
        for colour in max_balls.keys():
            pos = subgame.find(colour)
            if pos == -1: # If colour ball not drawn in subgame
                continue
            else:
                num = int(subgame[pos-3:pos-1]) # Extracts the number of balls of said colour extracted in subgame
                if num > max_balls[colour]: # Check if this number is too high given the number of balls claimed to be in the bag
                    possible = False
                    break

        if not possible:    # Saves time by not looping over any more subgames in game if one subgame is found to not be possible
            break

    if possible:
        output.append(game_id)
        
ans = sum(output)

print(ans)



#     # Reset total_balls dict to compare at the end with 
#     total_balls = {"red":0, "green":0, "blue":0}
#     for subgame in game:
#         for colour in max_balls.keys():
#             pos = subgame.find(colour)
#             if pos == -1:
#                 continue
#             else:
#                 # print(pos, , subgame)
#                 num = int(subgame[pos-3:pos-1])
#                 print(num)
#                 total_balls[colour] += num

#     possible = True
#     for colour, max_num in max_balls.items():
#         if total_balls[colour] > max_balls[colour]:
#             possible = False
#             break
    
#     if possible:
#         output.append(game_id)



            


# print(subgames)



    # if possible:
