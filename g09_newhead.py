import os
from git import Repo

# rorepo is a Repo instance pointing to the git-python repository.
# For all you know, the first argument to Repo is a path to the repository
# you want to work with
repo = Repo(os.getcwd())

new_branch = repo.create_head('feature')
print(type(new_branch))
print(new_branch)

commit = new_branch.set_commit('HEAD~1')
print(type(commit))
print(commit)



