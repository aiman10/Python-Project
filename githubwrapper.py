import asyncio
from github import Github

class GithubController():

    def __init__(self, token):
        self.client = Github(token)
    
    def get_contents(self, filename):
        repo = self.client.get_user().get_repo("bot-control")
        try:
            result =  repo.get_contents(filename)
            return result.decoded_content.decode('utf-8')
        except:
            return None
    def post_contents(self, filename, contents):
        repo = self.client.get_user().get_repo("bot-control")
        repo.create_file(filename, "", contents)
