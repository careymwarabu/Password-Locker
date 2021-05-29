import unittest # Importing the unittest module
from credentials import Credential # Importing the contact class

class TestCredential(unittest.TestCase):

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
        self.new_credential = Credential("twitter","Carey","mwarabu0") # create credential object

    def test_save_credential(self):
        '''
        test_save_credential test case to test if the credential object is saved into
         the credential list
        '''
        self.new_credential.save_credential() # saving the new credential
        self.assertEqual(len(Credential.credential_list),1)

    def test_save_multiple_credential(self):
            '''
            test_save_multiple_credential to check if we can save multiple credential
            objects to our credential_list
            '''
            self.new_credential.save_credential()
            new_user = Credential("instagram","Mwarabu","0000") # new credential
            new_user.save_credential()
            self.assertEqual(len(Credential.credential_list),2)

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credential.credential_list = []

    def delete_credential(self):

        '''
        delete_credential method deletes a saved credential from the credential list
        '''

        Credential.credential_list.remove(self)


    def test_display_user_credential(self):
        '''
        method that returns a list of user credential saved
        '''

        self.assertEqual(Credential.display_credentials(),Credential.credential_list)

if __name__ == '__main__':
    unittest.main()

