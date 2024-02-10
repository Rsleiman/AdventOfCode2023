with open("trebuchet.txt") as file:
    txt = file.read()


lines = txt.split("\n")

################
#### PART 1 ####
################
output1 = []
for line in lines:
    num_list = []
    for char in line:
        if char in "123456789":
            num_list.append(char)
    output1.append(int(num_list[0]+(num_list[-1])))

# print(output)

ans1 = sum(output1)

print(ans1)


            
################
#### PART 2 ####
################

output2 = []
word_to_int = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
for line in lines:
    num_list = []
    for i in range(len(line)):
        if line[i] in "123456789":
            num_list.append(line[i])
        else:
            for num in word_to_int.keys():
                if line[i:].startswith(num):
                    num = word_to_int[num]
                    num_list.append(num)
                    break
            

    output2.append(int(str(num_list[0])+str(num_list[-1])))

# for line in output2:
#     print(line)
        
ans2 = sum(output2)

print(ans2)



# Look for first occurence of number or num_word
# Convert into int form and append to output
        
# Do for all occurences? May be possible to only require first and last

# Look for last occurence of number or num_word
# Convert into int form and append to output
