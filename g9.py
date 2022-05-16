import os
from git import Repo

def create_git_repository(test_case, bare=False):
    """
    Create a git repository with a ``master`` branch and ``README``.

    :param test_case: The ``TestCase`` calling this.
    """
    directory = '/home/jangcs/GitPython/Working'

    repository = Repo.init(path=directory, bare=bare)

    if not bare:
        repository.index.add(['README'])
        repository.index.commit('Initial commit')
        repository.create_head('master')
    return repository 


create_git_repository('')
