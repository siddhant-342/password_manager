import pandas as pd
import sys
import pyperclip 
def load_passwords_df():# To load the dataset containing passwords
    df = pd.read_csv('E:/Python-Workspace/Projects/password_manager/passwords.csv',usecols=['name','username','password'])
    return df

def save_passwords_df(df):# To update dataset
    df.to_csv(path_or_buf='E:/Python-Workspace/Projects/password_manager/passwords.csv',columns=['name', 'username', 'password'])

def _change(length):# To change password
    df = load_passwords_df()
    names = df['name'].to_numpy()
    if length < 3:
        print('Select a name from the list below: ')
        for i in range(len(names)):
            print('->',names[i])
        name = input('\nEnter the name: ')
        while name.strip()  == '':
            name = input('Please enter a valid name: ')

    else:
        name = sys.argv[2]
        if name not in names:
            print('Select a name from the following list: ')
            for i in range(len(names)):
                print('->',names[i])
            name = input('Enter the name: ')
            while name.strip() == '':
                name = input('Please enter a valid name: ')


    while name.strip() not in names:
        name  = input('\nPlease select a name from the above list: ')
    if length < 4:
        password = input('Please enter the new password: ')
        while password.strip() == '':
            password = input('Please enter a valid password: ')
    else:
        password = sys.argv[3]
            
    df.loc[df[df['name'] == name].index, 'password'] = password.strip()
    save_passwords_df(df)
    if length < 4:
        print('Password changed successfully ')
        print('Press enter to exit')
        x = input()




def _set(length):# To set new data
    df = load_passwords_df()
    if length < 3:
        name = input('Enter name: ')
        while name.strip() == '':
            name = input('Please enter a valid name: ')
        # print('\n')
    else:
        name = sys.argv[2]

    if name.strip() in df['name'].to_numpy():
        
        while 1:
            ask = input('Name already present. Do you really want to reset credentials ? (y/n): ')
            if ask in ['y','Y','Yes','yes','YES',1,'1']:
                df.drop([df[df['name'] == name.strip()].index[0]], inplace=True)
                break
                
            elif ask in ['n','N', 'No','no','NO',0,'0']:
                sys.exit()
            else:
                print('Invalid input')

    if length < 4:
    
        username = input('Enter username: ')
        while username.strip() == '':
            username = input('Please enter a valid usename: ')
        
            #ask = input('Name already present. Do you really want to reset credentials')
        # print('\n')
    else:
        username = sys.argv[3]
    if length < 5:
        password = input('Enter password: ')
        while password.strip() == '':
            password = input('Please enter a valid password: ')
        # print('\n')
    else:
        password = sys.argv[4]

    df2 = pd.DataFrame([[name.strip(),username.strip(),password.strip()]], columns=['name', 'username', 'password'])
    df = df.append(df2,ignore_index=True)
    df.sort_values(by=['name'], ascending=True,inplace=True)
    df.reset_index(inplace=True, drop=False)
    save_passwords_df(df)
    if length < 5:
        print('Credentials set as:\nname:',name.strip(),'\nusername:',username.strip(),'\npassword:',password.strip())
        x = input('Press enter to exit')





def _del(length):# To delete data
    df = load_passwords_df()
    names = df['name'].to_numpy()
    if length < 3:
        print('Select a name from list below to delete: ')
        for i in range(len(names)):
            print('->',names[i])
        name = input('\nEnter the name: ')
        while name.strip() == '':
            name = input('Please enter a valid name: ')
        # print('\n')
    else:
        name = sys.argv[2]
        if name not in names:
            print('Select a name from the following list: ')
            for i in range(len(names)):
                print('->',names[i])
            name = input('Enter the name: ')
            while name.strip() == '':
                name = input('Please enter a valid name: ')

    if name.strip() in df['name'].to_numpy():
        df.drop([df[df['name'] == name.strip()].index[0]], inplace=True)
        save_passwords_df(df)
        if length<3:
            print('Data successfully deleted.\nPress enter to exit.')
            x = input()
    else:
        print('Name not found in dataset.\nPress enter to exit.')
        x = input()    



def _username(length):# To get usename 
    df = load_passwords_df()
    names = df['name'].to_numpy()
    if length < 3:
        print('Select a name from the following list: ')
        for i in range(len(names)):
            print('->',names[i])
        name = input('Enter the name: ')
        while name.strip() == '':
            name = input('Please enter a valid name: ')
        # print('\n')
    else:
        name = sys.argv[2]
        if name not in names:
            print('Select a name from the following list: ')
            for i in range(len(names)):
                print('->',names[i])
            name = input('Enter the name: ')
            while name.strip() == '':
                name = input('Please enter a valid name: ')


    while name.strip() not in names:
        name = input('Please select a name from the above list: ')
        
        
    username = list(df[df['name'] == name.strip()]['username'])[0]
    pyperclip.copy(username)
    if length<3:
        print('username ('+username+') successfully copied to clipboard.\nPress enter to exit.')
        x = input()


def _password(length): # To get your password
    df = load_passwords_df()
    names = df['name'].to_numpy()
    if length < 3:
        print('Select a name from the following list: ')
        for i in range(len(names)):
            print('->',names[i])
        name = input('Enter the name: ')
        while name.strip() == '':
            name = input('Please enter a valid name: ')
        # print('\n')
    else:
        name = sys.argv[2]
        if name not in names:
            print('Select a name from the following list: ')
            for i in range(len(names)):
                print('->',names[i])
            name = input('Enter the name: ')
            while name.strip() == '':
                name = input('Please enter a valid name: ')


    while name.strip() not in df['name'].to_numpy():
        
            name = input('Please select a name from the above list: ')
              
    password = list(df[df['name'] == name.strip()]['password'])[0]
    pyperclip.copy(password)
    if length<3:
        print('Password for selected name successfully copied to clipboard.\nPress enter to exit.')
        x = input()



def _info(length):
    df = load_passwords_df()
    names = df['name'].to_numpy()
    if length < 3:
        print('Select a name from the following list:')
        for i in range(len(names)):
            print('->',names[i])
        name = input('Enter name: ')
        
        while name.strip() == '':
            name = input('Please enter a valid name: ')
        # print('\n')
    else:
        name = sys.argv[2]
        if name not in names:
            print('Select a name from the following list: ')
            for i in range(len(names)):
                print('->',names[i])
            name = input('Enter the name: ')
            while name.strip() == '':
                name = input('Please enter a valid name: ')
    while name.strip() not in df['name'].to_numpy():
        name = input('Please select a name from the above list: ')
        
    info = df[df['name'] == name.strip()].to_numpy()
    print('\nNAME:', info[0,0],'\nUSERNAME:', info[0,1], '\nPASSWORD', info[0,2])
    
    print('Press enter to exit.')
    x = input()


def _info_all():
    df = load_passwords_df()
    print(df)
    x = input('Press enter to exit.')

def _else():
    df = load_passwords_df()
    name = sys.argv[1]
    names = df['name'].to_numpy()
    if name in names:
        password = list(df[df['name'] == name.strip()]['password'])[0]
        pyperclip.copy(password)
        sys.exit()
    while name not in names:
        print('Name not found in dataset.\nPlease select a name from below:')
        for i in range(len(names)):
            print('->',names[i])
        name = input('Enter name: ')
        name = name.strip()
        print('\n')

    password = list(df[df['name'] == name.strip()]['password'])[0]
    pyperclip.copy(password)
    print('Password for selected name successfully copied to clipboard.\nPress enter to exit.')
    x = input()



