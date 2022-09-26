So far, everything done above is still in local repository, if we want to push our content to a
remote repository for collaboration, we will need to harness the power of `git remote`.

!!! Info "Read More"
    Visit [Atlassian's git remote tutorial](https://www.atlassian.com/git/tutorials/syncing
    /git-remote) for more details.

## Generic Git Remote Workflow 

To add a remote to our local repository, we first need to create a remote repository.

For our purpose we will be using GitHub. Follow [the steps here](https://docs.github.com/en/get-started/quickstart/create-a-repo)
to create a new repository on GitHub.

Once the remote repository is created, we will copy the URL for the remote repository. In this tutorial,
we will only focus on the HTTPS URL.

```bash title="git remote add" linenums="1"
~/gaohn/git_tutorial $ git remote add <remote name> <remote url>
```

where `<remote name>` is the name of the remote repository and `<remote url>` is the URL of the remote repository.

After creating a remote repository on GitHub, we call that remote repository `origin`. 
Therefore, our `<remote name>` is `origin` and the `<remote url>` is the HTTPS URL of the remote repository.

```bash title="git remote add" linenums="1"
~/gaohn/git_tutorial $ git remote add origin https://github.com/reigHns92/git-tutorial.git
```


!!! tip
    I often encounter permission denied error when pushing to remote when I have two github accounts
    on the same local machine, one solution is to use SSH, the other is the one listed below:

    1. Create a [personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) 
       for the second account and **[tick all access](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)**. 
    
    2. Add the remote origin for the second account.
    ```bash
    git remote add <remote name> <remote url>
    git remote set-url <remote name> <https://[token]@github.com/[username]/[repository_name]>
    ```
    
    3. Push the changes to the second account and a prompt opens for you to key in token access.

## Useful Git Remote Commands

```bash title="git remote commands" linenums="1"
~/gaohn/git_tutorial $ git remote -v                            # (1)
~/gaohn/git_tutorial $ git remote rm <remote name>              # (2)
~/gaohn/git_tutorial $ git remote rename <old name> <new name>  # (3)
```

1. List all the remote repositories that are added to our local repository.
2. Remove a remote repository from our local repository.
3. Rename a remote repository.