from github import Github

# First create a Github instance:

# using username and password
#g = Github("rajabade01@gmail.com", "Puja1&raja1")

# or using an access token
g = Github("8b6c700711b3c0efb4a7f7d6f90694dc3ca7213d")

# Github Enterprise with custom hostname
g = Github(base_url="https://https://api.github.com//users//rajabade01//repos", login_or_token="8b6c700711b3c0efb4a7f7d6f90694dc3ca7213d")

# Then play with your Github objects:
for repo in g.get_user().get_repos():
    print(repo.name)