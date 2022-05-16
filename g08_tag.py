import os
from git import Repo

# rorepo is a Repo instance pointing to the git-python repository.
# For all you know, the first argument to Repo is a path to the repository
# you want to work with
repo = Repo(os.getcwd())

t = repo.tags['v0.1']
print(type(t))
print(t)

t = repo.tag('refs/tags/v0.2')
print(type(t))
print(t)

h = repo.refs.master
print(type(h))
print(h)

h = repo.heads['master']
print(type(h))
print(h)

r = repo.refs['origin/master']
print(type(r))
print(r)

r = repo.remotes.origin.refs.master
print(type(r))
print(r)
