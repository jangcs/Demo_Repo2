import os
from git import Repo

# rorepo is a Repo instance pointing to the git-python repository.
# For all you know, the first argument to Repo is a path to the repository
# you want to work with
repo = Repo(os.getcwd())
assert not repo.bare


reader = repo.config_reader()             # get a config reader for read-only access
print(type(reader))
#print(dir(reader))
with repo.config_writer() as writer:       # get a config writer to change configuration
	print(type(writer))

print(repo.untracked_files)

