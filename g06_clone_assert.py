import os
from git import Repo

# rorepo is a Repo instance pointing to the git-python repository.
# For all you know, the first argument to Repo is a path to the repository
# you want to work with
repo = Repo(os.getcwd())
assert not repo.bare


cloned_repo = repo.clone(os.path.join('/home/jangcs/GitPython', 'cloned'))
assert cloned_repo.__class__ is Repo     # clone an existing repository
#assert Repo.init(os.path.join('/home/jangcs/GitPython', 'cloned')).__class__ is Repo

print(cloned_repo.working_tree_dir) 
assert os.path.isdir(cloned_repo.working_tree_dir)                   # directory with your work files
print(cloned_repo.git_dir) 
assert cloned_repo.git_dir.startswith(cloned_repo.working_tree_dir)  # directory containing the git repository

