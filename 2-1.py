def kvadrat (s = list):
    if ((s[0][0] + s[0][1] + s[0][2]) ==(s[1][0] + s[1][1] + s[1][2])
                        and (s[0][0] + s[0][1] + s[0][2]) == (s[2][0] + s[2][1] + s[2][2])
                        and (s[0][0] + s[0][1] + s[0][2]) == (s[0][0] + s[1][1] + s[2][2])
                        and (s[0][0] + s[0][1] + s[0][2]) == (s[2][0] + s[1][1] + s[0][2])
                        and (s[0][0] + s[0][1] + s[0][2]) == (s[0][0] + s[1][0] + s[2][0])
                        and (s[0][0] + s[0][1] + s[0][2]) == (s[0][1] + s[1][1] + s[2][1])
                        and (s[0][0] + s[0][1] + s[0][2]) == (s[0][2] + s[1][2] + s[2][2])):
        print("Этот квадрат магический")
    else:
        print("Этот квадрат не магический")
