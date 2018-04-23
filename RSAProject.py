quit = 1

while quit != 2:
    print("Encrypt, Decrypt, or Exit?")
    answer=input("----->")
    if answer == ("Exit") or ('Exit') or ('exit') or ('exit'):
        quit += 1
        print
        print ("Exiting...")
        print
    if answer == ("Encrypt") or ('Encrypt') or ('encrypt') or ("encrypt"):
        e = 0
        answer=input("----->")
        print
        print ("Please enter your /e/ value:")
        print
        if answer != 0:
            print
            print ("Please enter your /n/ value:")
            print
    if answer == ("Decrypt") or ('Decrypt') or ('decrypt') or ("decrypt"):
        print
        print ("Please enter your // value:")
        print