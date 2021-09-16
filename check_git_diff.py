#! /bin/python
import sys
import git
if len(sys.argv) < 2 :
	print("Provide the path for the git directory")
f = open("output_gitCheck.txt", "a")
repo = git.Repo(sys.argv[1])
commits_list = list(repo.iter_commits())
git_repo = repo.git
for i in range(len(commits_list)-1):
	f.write(git_repo.diff(commits_list[i],commits_list[i+1]))
f.close()
