The [documentation on merging vs rebasing](https://www.atlassian.com/git/tutorials/merging-vs-rebasing)
written by Atlassian is a great resource for understanding the differences between the two approaches.

!!! Tip
    If you intend to use `git rebase` instead of `git merge`, then the below is a very generic
    workflow that you can follow.

    ```bash title="git rebase workflow" 
    $ git checkout feature
    $ git checkout -b temp-branch
    $ git rebase -i dev
    $ git checkout feature
    $ git merge temp-branch
    ```

    The workflow assumes that you have a `dev` branch that is in sync with the upstream `dev` branch.
    You are working on a feature branch called `feature` and after you have done developing, you
    want to check that your changes are compatible with the latest changes in the `dev` branch.
    You can then use interactive rebase to rebase your feature branch on top of the `dev` branch.

    I created a `temp-branch` to make sure that I don't mess up my history in the `feature` branch
    if anything goes wrong.