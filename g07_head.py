import os
from git import Repo

# rorepo is a Repo instance pointing to the git-python repository.
# For all you know, the first argument to Repo is a path to the repository
# you want to work with
repo = Repo(os.getcwd())

print('repo.head')
print(type(repo.head))
print(repo.head)

print('repo.head.name')
print(type(repo.head.name))
print(repo.head.name)

print()

print('repo.head.ref')
print(type(repo.head.ref))
print(repo.head.ref)

print('repo.head.ref.name')
print(type(repo.head.ref.name))
print(repo.head.ref.name)

print()

print('repo.heads.main')
print(type(repo.heads.main))
print(repo.heads.main)

print('repo.heads["main"]')
print(type(repo.heads['main']))
print(repo.heads['main'])

print('repo.heads[0]')
print(type(repo.heads[0]))
print(repo.heads[0])
