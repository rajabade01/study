import requests

class TestAPI():
    username = 'rajabade01@gmail.com'
    token = '8b6c700711b3c0efb4a7f7d6f90694dc3ca7213d'

    def get_repos(self):
        response = requests.get('https://api.github.com/search/repositories?q=github+api', auth=(self.username,self.token))
        return response

if __name__ == "__main__":
    api = TestAPI()
    res = api.get_repos()
    print("api %s" %res)