i=1
while i <= 9:
    j = 1
    while j<=9:
        number = i*j
        if number %6 == 0:
            print('##',end='\t')
        elif number %2 == 0:
            print("**",end = '\t')
        elif number %3 == 0:
            print("@@",end='\t')

        else:
            print(number,end='\t')
        j += 1
    i += 1
    print('')