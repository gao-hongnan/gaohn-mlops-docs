!!! Quote "Atlassian Git Fetch"
    The `git fetch` command downloads commits, files, and refs from a remote repository into your local repo. Fetching is what you do when you want to see what everybody else has been working on. It lets you see how the central history has progressed, but it doesn’t force you to actually merge the changes into your repository. Git isolates fetched content from existing local content; it has absolutely no effect on your local development work. Fetched content has to be explicitly checked out using the `git checkout` command. This makes fetching a safe way to review commits before integrating them with your local repository.

    When downloading content from a remote repo, `git pull` and `git fetch` commands are available to accomplish the task. You can consider `git fetch` the 'safe' version of the two commands. It will download the remote content but not update your local repo's working state, leaving your current work intact. git pull is the more aggressive alternative; it will download the remote content for the active local branch and immediately execute git merge to create a merge commit for the new remote content. If you have pending changes in progress this will cause conflicts and kick-off the merge conflict resolution flow.

!!! Info "Read More"
    Visit [Atlassian's git fetch tutorial](https://www.atlassian.com/git/tutorials/syncing/git-fetch)
    for more details.

We will add more content with examples later, for now we will see a simplified example, continuing 
from the previous section [git push](git_push.md).

## Generic Git Fetch Workflow

Let's say I have two local machines A and B. I develop on machine A at home and machine B at work.

So far, commits 1-3 [27378ad, b9d3256, 13e956d] were developed on machine A. 

Subsequently, I went to work and will work on machine B. Let's say I created a new branch 
`git-fetch` on machine B at commit SHA `13e956d`, meaning to say
this branch has a snapshot of the remote repository at commit SHA `13e956d`.
Note that this branch is pushed to the remote repository from **machine B**.

When I get back to machine A, I want to synchronize my local repository with the remote repository
(i.e. I want the branch `git-fetch` created on machine B to be available on machine A).

I can call the command `git fetch origin`:

=== "Git Fetch"
    ```bash title="git fetch" linenums="1"
    ~/gaohn/git_tutorial $ git fetch origin
    ```

=== "Git Fetch Outputs"
    ```bash title="git fetch output" linenums="1"
    From https://github.com/reigHns92/git-tutorial
    * [new branch]      git-fetch  -> origin/git-fetch
    ```

This will "download" the remote repository's `git-fetch` branch to my local repository and I now have
a local branch `git-fetch` that is tracking the remote branch `git-fetch`.
  
To further understand this, let's say I made some changes to the `README.md` on branch `git-fetch`
at commit hash `13e956d` and pushed it to the remote repository from machine B at commit `f3d4f25`.
Consequently, my local repo at machine A will be one commit behind the remote repository at branch `git-fetch`.

=== "Git Fetch"
    ```bash title="git fetch" linenums="1"
    ~/gaohn/git_tutorial $ git fetch origin
    ```

=== "Git Fetch Outputs"
    ```bash title="git fetch output" linenums="1"
    remote: Enumerating objects: 5, done.
    remote: Counting objects: 100% (5/5), done.
    remote: Compressing objects: 100% (3/3), done.
    remote: Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
    Unpacking objects: 100% (3/3), 742 bytes | 123.00 KiB/s, done.
    From https://github.com/reigHns92/git-tutorial
    * branch            git-fetch  -> FETCH_HEAD
    13e956d..f3d4f25  git-fetch  -> origin/git-fetch
    ```

Running `git status` will also show that the local repository at machine A is one commit behind the remote repository at branch `git-fetch`.

To see what commits have been added to the remote origin branch `git-fetch`, you can run a `git log` using `origin/git-fetch` as a filter:  

```bash title="git log" linenums="1"
~/gaohn/git_tutorial $ git log --oneline master..origin/git-fetch
```

which will a message `f3d4f25 (origin/git-fetch) git: update README`.

Finally, you can merge the changes made on `git-fetch` to your local repository at machine A:

=== "Git Merge"
    ```bash title="git merge" linenums="1"
    ~/gaohn/git_tutorial $ git merge origin/git-fetch
    ```

=== "Git Merge Outputs"
    ```bash title="git merge output" linenums="1"
    Updating 13e956d..f3d4f25
    Fast-forward
    README.md | 1 +
    1 file changed, 1 insertion(+)
    ```

Now, you can see that the local repository at machine A is up-to-date with the remote repository 
at branch `git-fetch`.