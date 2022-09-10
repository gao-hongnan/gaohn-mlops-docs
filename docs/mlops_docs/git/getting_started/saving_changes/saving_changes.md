Committing is the process in which the changes are *officially* added to the Git repository.

In Git, we can consider **commits** to be checkpoints, or snapshots of your project at its current state.
In other words, we basically save the current version of our code in a commit.
We can create as many commits as we need in the commit history, and we can go back and forth between
commits to see the different revisions of our project code. 
That allows us to efficiently manage our progress and track the project as it gets developed.

Commits are usually created at logical points as we develop our project, usually after adding in 
specific contents, features or modifications (like new functionalities or bug fixes, for example).

## Creating gitignore

Usually, I recommend creating `.gitignore` at this step, because you want to list down files 
that you do not wish git to track. 
This is important because some secret keys should never be pushed to the remote server for people to see. Furthermore, some large files should be kept in a storage as git cannot store too large files.

To ignore files that you don't want to be tracked or added to the staging area, you can create a file called `.gitignore` in your main project folder.

Inside of that file, you can list all the file and folder names that you definitely do not want to track (each ignored file and folder should go to a new line inside the **.gitignore** file).

```bash title="create .gitignore" linenums="1"
~/gaohn/git_tutorial $ touch .gitignore
```

For example, if I have a file called `secrets.py` that contains my secret key, I can add it to the `.gitignore` file.

```bash title="create .gitignore" linenums="1"
~/gaohn/git_tutorial $ touch secrets.py
~/gaohn/git_tutorial $ echo "secrets.py" >> .gitignore
```

!!! Info "Read More"
    Visit the [Atlassian's gitignore tutorial](https://www.atlassian.com/git/tutorials/saving-changes/gitignore) for more details.

## Checking Status: `git status`

While located inside the project folder in our terminal, we can type the following command to check the status of our repository:

```bash title="git status" linenums="1"
~/gaohn/git_tutorial $ git status
```

which will return something like this:

```bash title="git status output" linenums="1"
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .gitignore
        README.md
        secrets.py

nothing added to commit but untracked files present (use "git add" to track)
```

This is a command that is very often used when working with Git.  It shows us which files have been changed, which files are tracked, etc.

We can add the untracked project files using `git add` to the **staging area** based on the information from the `git status` command.

At a later point, `git status` will report any modifications that we made to our tracked files before we decide to add them to the staging area again.

## Adding Files to the Staging Area: `git add`

The `git add` command adds a change in the working directory to the staging area. 

It tells Git that you want to include updates to a particular file in the next commit. 

However, `git add` doesn't really affect the repository in any significant way—changes are not actually
recorded until you run git commit.

In conjunction with these commands, you'll also need git status to view the state of the working directory and the staging area.

Next we will add all our current changes to the staging area:

```bash title="git add all files in cwd" linenums="1"
~/gaohn/git_tutorial $ git add . # (1)
```

1. add all files in the current directory

You can also choose to add specific files to the staging area.

```bash title="git add specific files" linenums="1"
~/gaohn/git_tutorial $ git add <file>
```

!!! Info "Read More"
    Visit the [Atlassian's git add tutorial](https://www.atlassian.com/git/tutorials/saving-changes/git-add) for more details.

## Making commits: `git commit`

A **commit** is a snapshot of our code at a particular time, which we are saving to the commit 
history of our repository. After adding all the files that we want to track to the staging area with
the **`git add`** command, we are ready to make a commit.

To commit the files from the staging area, we use the following command:

```bash title="git commit" linenums="1"
~/gaohn/git_tutorial $ git config --global core.editor "code --wait" # (1)
~/gaohn/git_tutorial $ git commit -a                                 # (2)
```

1. use this code if popup editor does not appear.
2. a pop up editor should appear for you to type the message.

The commit message should be a descriptive summary of the changes that you are committing to the repository. 
For the first commit, I usually type "Initial Commit" as the commit message.

After making the commit, you will see messages like the following:

```bash title="git commit output" linenums="1"
[master (root-commit) 3dccc05] Initial Commit
 3 files changed, 3 insertions(+)
 create mode 100644 .gitignore
 create mode 100644 README.md
 create mode 100644 secrets.py
```

!!! Info "Read More"
    Visit the [Atlassian's git commit tutorial](https://www.atlassian.com/git/tutorials/saving-changes/git-commit) for more details.

### Commit History: `git log`

To see all the commits that were made for our project, you can use the following command:

```bash title="git log" linenums="1"
~/gaohn/git_tutorial $ git log
```

The logs will show details for each commit, like the author name, the generated hash for the commit, date and time of the commit, and the commit message that we provided.

To go back to a previous state of your project code that you committed, you can use the following command:

```bash title="git checkout specific commit" linenums="1"
~/gaohn/git_tutorial $ git checkout <commit_hash>
```

Replace `<commit-hash>` with the actual hash for the specific commit that you want to visit, which is listed with the `git log` command.

To go back to the latest commit (the newest version of our project code), you can type this command:

```bash
~/gaohn/git_tutorial $ git checkout master
```

### Update/Amend Commit

To update the commit message for the latest commit, you can use the following command:

```bash title="git commit --amend" linenums="1"
~/gaohn/git_tutorial $ git commit --amend
```

This is useful if you forgot to add something to the commit message.

!!! Info "Read More"
    There are much more nuance to this and visit the [Atlassian's rewriting history 
    tutorial](https://www.atlassian.com/git/tutorials/rewriting-history#git-commit--amend) for more details
    on how to change committed files.




