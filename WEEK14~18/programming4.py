def solution(program, flag_rules, commands):
    # answer = []
    # return answer
    flag_num = len(flag_rules)
    command_num = len(commands)

    answer = [False for _ in range(command_num)]


    flag_rules_parse = [0 for _ in range(flag_num)]
    for i in range(flag_num):
        flag_rules_parse[i] = flag_rules[i].split(' ')
    print("flag_rules_parse is : ",flag_rules_parse)

    command_parse = [0 for _ in range(command_num)]
    for i in range(command_num):
        command_parse[i] = commands[i].split(' ')
    # print(command_parse)

    for i in range(len(command_parse)):
        if command_parse[i][0] == program:
            answer[i] = True
    # print(flag)


    print("command_parse is : " , command_parse)
    # print(answer)
    flag_command = []
    for s in range(flag_num):
        flag_command.append(flag_rules_parse[s][0])


    for i in range(len(answer)):
        if answer[i] == False:
            continue
        elif len(command_parse[i]) == 1 and answer[i] == True:
            continue

        # for j in range(1, len(command_parse)):
        print(len(command_parse[i]))
        print(flag_command)

        if command_parse[i][1] not in flag_command:
            answer[i] = False
            print(answer)
            return

        j = 1
        while j <= len(command_parse[i]):
            # print(1)
            if command_parse[i][j] in flag_command:
                answer[i] = True
                for k in range(len(flag_rules_parse)):
                    # print(j)
                    if command_parse[i][j] == flag_rules_parse[k][0]:
                        if flag_rules_parse[k][1] == 'STRING':
                            if command_parse[i][j+1].isalpha(): 
                                answer[i] = True
                                j += 2
                                break

                        elif flag_rules_parse[k][1] == 'NUMBER':
                            if command_parse[i][j+1].isdigit():
                                answer[i] = True
                                j += 2
                                break
                            
                        elif flag_rules_parse[k][1] == 'NULL':
                            if j+1 >= len(command_parse[i]):
                                print(answer)
                                return                               
                            for e in range(len(flag_rules_parse)):
                                if command_parse[i][j+1] == flag_rules_parse[e][0]:
                                    answer[i] = True
                                    j += 1
                                    break
                            break
            else:
                answer[i] = False
                break
    
    print(answer)










# program = "line"
# flag_rules = ["-s STRING", "-n NUMBER", "-e NULL"]
# commands = ["line -n 100 -s hi -e", "lien -s Bye"]
# # answer = [True, False]


program = "line"
flag_rules = ["-s STRING", "-n NUMBER", "-e NULL"]
commands = ["line -s 123 -n HI", "line fun"]
# answer = [False, False]

solution(program, flag_rules, commands)