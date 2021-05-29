class User:
    """
    Class that generates new instances of users
    """

    user_list = [] # Empty user list

    def __init__(self,username,password,email):

         # docstring removed for simplicity

        self.username = username
        self.password = password
        self.email = email

     # Init method up here
    def save_user(self):

        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self)

    @classmethod
    def find_by_username(cls,username):
        '''
        Method that takes in a username and returns a user that matches that username.

        Args:
            username: Username to search for
        Returns :
            User of person that matches the username.
        '''

        for user in cls.user_list:
            if user.username == username:
                return user

    @classmethod
    def user_exist(cls,username,password):
        '''
        Method that checks if a user exists from the user list.
        Args:
            username: Username to search if it exists
            password: Password to serach if it exists
        Returns :
            Boolean: True or false depending if the user exists
        '''
        for user in cls.user_list:
             if user.username == username and user.password == password:
                return True

        return False

    @classmethod
    def display_users(cls):
        '''
        method that returns the contact list
        '''
        return cls.user_list
  
    

