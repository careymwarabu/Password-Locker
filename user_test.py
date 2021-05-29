import unittest # Importing the unittest module
from user import User # Importing the contact class

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    # Items up here .......

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("CareyMwarabu","Mwarabu","carey@gmail.com") # create contact object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.username,"CareyMwarabu")
        self.assertEqual(self.new_user.password,"Mwarabu")
        self.assertEqual(self.new_user.email,"carey@gmail.com")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.user_list),1)

    # Items up here...

    def test_save_multiple_user(self):
            '''
            test_save_multiple_user to check if we can save multiple user
            objects to our user_list
            '''
            self.new_user.save_user()
            test_user = User("test_user","user0000","test@user.com") # new user
            test_user.save_user()
            self.assertEqual(len(User.user_list),2)

    # setup and class creation up here
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list = []

# other test cases here
    def test_save_multiple_user(self):
            '''
            test_save_multiple_user to check if we can save multiple user
            objects to our user_list
            '''
            self.new_user.save_user()
            test_user = User("test_user","user0000","test@user.com") # new user
            test_user.save_user()
            self.assertEqual(len(User.user_list),2)

    def delete_user(self):

        '''
        delete_user method deletes a saved user from the user_list
        '''

        User.user_list.remove(self)

    def test_find_user_by_username(self):
        '''
        test to check if we can find a user by username and display information
        '''

        self.new_user.save_user()
        test_user = User("test_user","user0000","test@user.com") # new user
        test_user.save_user()

        found_user = User.find_by_username("test_user")

        self.assertEqual(found_user.email,test_user.email)

    def test_user_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the user.
        '''

        self.new_user.save_user()
        test_user = User("test_user","user0000","test@user.com") # new user
        test_user.save_user()

        user_exists = User.user_exist("test_user","user0000")

        self.assertTrue(user_exists)

    def test_display_all_Users(self):
        '''
        method that returns a list of all users saved
        '''

        self.assertEqual(User.display_users(),User.user_list)



if __name__ == '__main__':
    unittest.main()