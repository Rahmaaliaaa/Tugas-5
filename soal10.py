length = 5
for i in range (5):
    for J in range (length):
        if i % 2 == 0 :
            if J %2 == 0:
                print ("2", end = "")
            else :
                print ("3", end = "")
        else : 
            if J %2 == 1:
                print("2", end = "")
            else : 
                print("3", end = "")

    length -= 1
    print()                            
