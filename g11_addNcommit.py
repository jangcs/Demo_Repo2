import os
import git
from git import Repo

# rorepo is a Repo instance pointing to the git-python repository.
# For all you know, the first argument to Repo is a path to the repository
# you want to work with
print("Connecting Repository")
repo = Repo(os.getcwd())


file_name1="test_commitP.tst"

#open(file_name1, "wb").close()

print("Add files...")
#repo.index.add([file_name1, file_name2])
repo.index.add([file_name1])

commit_msg="2 files added #P"
print("Commit : " + commit_msg)
repo.index.commit(commit_msg)


tag_name="Tag1.P"
print("Create tag : " + tag_name)
tag_ref9=git.refs.tag.TagReference(repo, git.refs.tag.TagReference.list_items(repo)[-1].path)
tag_ref9.create(repo, tag_name)

origin = repo.remotes.origin
print("Push to master")
origin.push('HEAD:master')
print("Push tag : " + tag_name)
origin.push(tag_name)


