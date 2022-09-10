## How Branch Works

!!! Quote
    A branch represents an independent line of development. Branches serve as an abstraction for the edit/stage/commit process. You can think of them as a way to request a brand new working directory, staging area, and project history. New commits are recorded in the history for the current branch, which results in a fork in the history of the project.

    The `git branch` command lets you create, list, rename, and delete branches. It doesn’t let you switch between branches or put a forked history back together again. For this reason, `git branch` is tightly integrated with the `git checkout` and `git merge` commands.


## Creating New Branch

You can create a new branch using the following command:

```bash title="git branch" linenums="1"
~/gaohn/git_tutorial $ git branch <branch-name>
```

The new branch that gets created will be the reference to the current state of your repository.

This ***does not*** switch you to the new branch. To switch to the new branch, use the `git checkout` 
or `git switch` command.

For our purpose we create a dummy branch which we will delete later:

```bash title="git branch" linenums="1"
~/gaohn/git_tutorial $ git branch dummy
```

!!! note
    It's a good idea to create a **development** branch where you can work on improving your code, adding new experimental features, and similar. After development and testing these new features to make sure they don't have any bugs and that they can be used, you can merge them to the master branch.

## Listing Branches

To list all the branches in your repository, use the following command:

=== "List Git Branches"

    ```bash title="git branch" linenums="1"
    ~/gaohn/git_tutorial $ git branch --list
    ```

=== "Outputs"

    ```bash title="git branch" linenums="1"
    dummy
    * git-fetch
    master
    ```

This will list all the branches in your repository. The branch that you are currently on will be marked with an asterisk.

## Delete Branches

To delete a branch, you can run the following command:

```bash title="git branch -d" linenums="1"
~/gaohn/git_tutorial $ git branch -d <branch-name>
```

and in our case our `<branch-name>` is `dummy` and running the above command will tell us
`Deleted branch dummy (was f3d4f25).`

## Switching Branches

To switch to a different branch, you use the **git checkout** command:

```bash title="git checkout" linenums="1"
~/gaohn/git_tutorial $ git checkout <branch-name>
```

With that, you switch to a different isolated timeline of your project by changing branches.

!!! note
    For example, you could be working on different features in your code and have a separate branch for each feature. When you switch to a branch, you can commit code changes which only affect that particular branch. Then, you can switch to another branch to work on a different feature, which won't be affected by the changes and commits made from the previous branch.

To create a new branch and change to it at the same time, you can use the `-b` flag:

```bash title="git checkout -b" linenums="1"
~/gaohn/git_tutorial $ git checkout -b <branch-name>
```

In our example, let us create a new branch called `git-branch` and switch to it:

```bash title="git checkout -b" linenums="1"
~/gaohn/git_tutorial $ git checkout -b git-branch
```

and let's push this branch to remote:

```bash title="git push" linenums="1"
~/gaohn/git_tutorial $ git push -u origin git-branch
```


