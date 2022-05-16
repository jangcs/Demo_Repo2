import os
import git
from git import Repo


# rorepo is a Repo instance pointing to the git-python repository.
# For all you know, the first argument to Repo is a path to the repository
# you want to work with
repo = Repo(os.getcwd())

tagName="v2.0"
file_name1="test_v2.0.tst"
commitMsg=file_name1 + " added"

print("Adding file")
open(file_name1, "wb").close()
repo.index.add([file_name1])

print("Commiting msgs")
repo.index.commit(commitMsg)

print("Creating TagReference.")
git.refs.tag.TagReference.create(repo, tagName)

#origin = repo.remotes.origin
remote_origin = repo.remotes[0]   # repo.remotes.origin (=origin)
print("Push to main of remote " + remote_origin.name)

#origin.push('main')
remote_origin.push(repo.active_branch.name)   # main

print("Push tag : " + tagName)
remote_origin.push(tagName)
