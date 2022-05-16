import os
from git import Repo

# rorepo is a Repo instance pointing to the git-python repository.
# For all you know, the first argument to Repo is a path to the repository
# you want to work with
repo = Repo(os.getcwd())

active_branch = repo.active_branch
print(type(active_branch))
print(active_branch)
print(active_branch.name)

commit = active_branch.commit
print(type(commit))
print(commit)

