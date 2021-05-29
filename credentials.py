class Credential:
    """
    Class that generates new instances of users
    """

    credential_list = [] # Empty user list

    def __init__(self,social_media,account,password):

         # docstring removed for simplicity

        self.social = social_media
        self.account = account
        self.password = password
        
     # Init method up here
    def save_credential(self):

        '''
        save_credential method saves credential objects into cresdential_list
        '''

        Credential.credential_list.append(self)

    def delete_credential(self):

        '''
        delete_credential method deletes a saved credential from the credential_list
        '''

        Credential.credential_list.remove(self)

    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credentials list
        '''
        return cls.credential_list