import sys
import passwords_utils as utils
import pandas as pd

length = len(sys.argv)
if length < 2:
    commands = ['set','change','del','username','password','info','info_all','quit']
    print('Select a command from the following:')
    for i in range(len(commands)):
        print('->',commands[i])

    comm = input('Enter command: ')

    while comm not in commands:
        comm = input('Please Select a command from the above list:')


    if comm == 'set':
            utils._set(length)

    elif comm == 'change':
            utils._change(length)

    elif comm == 'del':
            utils._del(length)

    elif comm == 'username':
            utils._username(length)
        
    elif comm == 'password':
            utils._password(length)

    elif comm == 'info':
            utils._info(length)

    elif comm == 'info_all':
            utils._info_all()

    elif comm == 'quit':
            sys.exit()

    else:
            print('Command not recognized.')    
    
    # sys.exit()

elif sys.argv[1] == '_change':
    utils._change(length)

elif sys.argv[1] == '_set':
    utils._set(length)

elif sys.argv[1] == '_del':
    utils._del(length)    
        

elif sys.argv[1] == '_username':
    utils._username(length)


elif sys.argv[1] == '_password':
    utils._password(length)

elif sys.argv[1] == '_info':
    utils._info(length)


elif sys.argv[1] == '_info_all':
    utils._info_all()


else:
    utils._else()
