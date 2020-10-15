def step_of_alg(word, alg):
    for command in alg:
        if command[0] in word:
            word = word.replace(command[0], command[2], 1)
            if command[1] == "->.":
                return word, False
            else:
                return word, True
    return word, False

def alg_ap(word, alg):
    flag = True
    counter = 0
    while flag and counter <= 10000000:
        word, flag = step_of_alg(word, alg)
        counter += 1
    return word
