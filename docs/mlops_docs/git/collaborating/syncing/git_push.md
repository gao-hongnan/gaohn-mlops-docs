!!! Quote "Atlassian Git Push"
    The `git push` command is used to upload local repository content to a remote repository. 

    Pushing is how you transfer commits from your local repository to a remote repo. 
    
    It's the counterpart to git fetch, but whereas fetching imports commits to local branches, 
    pushing exports commits to remote branches. Remote branches are configured using the git remote command. 
    
    Pushing has the potential to overwrite changes, caution should be taken when pushing. These issues are discussed below.

!!! Info "Read More"
    Visit [Atlassian's git push tutorial](https://www.atlassian.com/git/tutorials/syncing/git-push) for more details.

## Generic Git Push Workflow

Continuing from the previous section on [git remote](git_remote.md), we will now push our local 
repository to the remote repository.

```bash title="git push" linenums="1"
~/gaohn/git_tutorial $ git push <remote name> <branch name>
```

where `<remote name>` is the name of the remote repository and `<branch name>` is the name of the branch.

In our example, we will be pushing to the `origin` remote repository and the `master`/`main` branch.

=== "Git Push"
    ```bash title="git push" linenums="1"
    ~/gaohn/git_tutorial $ git push origin master
    ```

=== "Git Push Outputs"
    ```bash title="git push output" linenums="1"
    Enumerating objects: 8, done.
    Counting objects: 100% (8/8), done.
    Delta compression using up to 12 threads
    Compressing objects: 100% (4/4), done.
    Writing objects: 100% (8/8), 614 bytes | 614.00 KiB/s, done.
    Total 8 (delta 1), reused 0 (delta 0), pack-reused 0
    remote: Resolving deltas: 100% (1/1), done.
    To https://github.com/reigHns92/git-tutorial.git
    * [new branch]      master -> master
    Branch 'master' set up to track remote branch 'master' from 'origin'.
    ```

This will now push our local repository to the remote repository and can be further confirmed
by `git remote -v`.

## Non-Fast-Forward Push

This terminology was mentioned a few times in Atlassian's Git tutorial.

Basically, if Git detects that the remote repository is ahead of the local repository, it will refuse to push.

This is common, let's see the example:

1. Prior to this section, we pushed our local repository to the remote repository `master` with commit SHA `b9d3256`.
2. Shortly after, my friend Joe synced up with the remote repository at commit SHA `b9d3256` and he updated
`README.md` and pushed with commit SHA `13e956d` to `master`.
3. Now if I run `git push -u origin master` again, Git will detect that the remote repository is ahead of the local repository and refuse to push, giving me the following errors.

    ```bash title="git push" linenums="1"
    To https://github.com/reigHns92/git-tutorial.git
    ! [rejected]        master -> master (fetch first)
    error: failed to push some refs to 'https://github.com/reigHns92/git-tutorial.git'
    hint: Updates were rejected because the remote contains work that you do
    hint: not have locally. This is usually caused by another repository pushing
    hint: to the same ref. You may want to first integrate the remote changes
    hint: (e.g., 'git pull ...') before pushing again.
    hint: See the 'Note about fast-forwards' in 'git push --help' for details
    ```
4. To resolve this, I need to `git pull origin` first and then run `git push -u origin master`.
5. However, this is an over-simplified example because I made an assumption that I did not have any local changes/developments
on at the commit `b9d3256`. If I did, then I may have to resolve merge conflicts, which we will see in future tutorials.