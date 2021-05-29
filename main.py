#!/usr/bin/env python3.6
from user import User
from credentials import Credential

def create_contact(username,password,email):
    '''
    Function to create a new contact
    '''
    new_user = User(username,password,email)
    return new_user

def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()

def find_user(username):
    '''
    Function that finds a user by username and returns the user
    '''
    return User.find_by_username(username)

def check_existing_users(username):
    '''
    Function that check if a user exists with that username and return a Boolean
    '''
    return User.user_exist(username)

def display_users():
    '''
    Function that returns all the saved users
    '''
    return User.display_users()


def automatic_generated_password():
    """
    Function that generates an automatic password for users
    :return:
    """
    generate_password = Credential.automatic_generated_password()
    return generate_password

def main():
     while True:
        print("WELCOME TO PASSWORD LOCKER")
        print("Select an option: \n 1 - Create an account \n 2 - Display available users "
              " \n 3 - Login to your account \n 4 - Exit Python Password Locker")
        print("\n")

        choice = int(input())

        if choice == 1:
           print("*" * 20)
           print("Create an account")
           print("*" * 20)

           print("Enter your username")
           user_name = input()
           print("-" * 10)

           print("Enter your email")
           email = input()
           print("-" * 10)

           print("Enter a new password")
           password = input()
           print("-" * 10)

           save_user(create_user(user_name, password, email))# create and save new user.
           print("-" * 10)

           print(f"{user_name}, you have successfully created an account. You may now login")

        elif choice == 2:
           if display_all_users():
                print("Here is a list of your users")
                print("-" * 20)

                for user in display_all_users():
                    print(f"Username: {user.username}")
                    print(f"Email: {user.email}")

           else:
                print("\n")
                print("You don't seem to have any user saved yet")
                print('\n')

        elif choice == 3:
            print("*" * 20)
            print("Login")
            print("*" * 20)

            print("Enter your username")
            username = input()
            print("-" * 10)

            print("Enter your password")
            password = input()

            verification = check_existing_user(username, password)

            if verification:
                print("\n")
                print(f"{username}, welcome to the password locker")
                print("\n")

            while True:
                    print("-" * 10)
                    print("Select an option: \n 1-Add details to your account \n 2-Display your account details"
                          " \n 3-End Session")
                    print("-" * 10)

                    choice = int(input())

                    if choice == 1:
                        print("-" * 10)
                        print("Add details to your account")

                        print("-" * 10)
                        print("Which social media network are you on?")
                        social = input()

                        print("-" * 10)
                        print(f"What is your {social} account name?")
                        account_name = input()


                        while True:
                            print("-" * 10)
                            print("Select an option: \n 1: Use your own password \n "
                                  "2: Use an auto generated password \n 3: End Session")

                            choice = int(input())


                            if choice == 1:
                                print("-" * 10)
                                print("Please input your passed")
                                password = input()
                                break

                            elif choice == 2:
                                print("-" * 10)
                                password = automatic_generated_password()
                                break

                            elif choice == 3:
                                break

                            else:
                                print("-" * 10)
                                print("Error! Incorrect input, please try again")

                            save_user_details(create_user_details(social, account_name, password))
                            print("\n")
                            print(f"Congratulations {username}, your details have been saved successfully.")
                            print(f"Username: {username}")
                            print(f"Password: {password}")

                    elif choice == 2:
                        if display_user_details(username):
                            print("Input a username")
                            print("-" * 10)

                            for user_details in display_user_details(username):
                                print(f"Social Media : {user_details.social} \n Password: {user_details.password}")
                            else:
                                print("No user details for the given username")

                    elif choice == 3:
                        break

            else:
                print("Sorry, we can't find such a user. Please try again!")

        else:
            print("Goodbye...")
            break

if __name__ == '__main__':
    main()











