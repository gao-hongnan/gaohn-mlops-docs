<div align="center">
<h1>Git Tutorial (Based on Atlassian)</a></h1>
<br>
</div>

---


A typical workflow

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin <>
git push -u origin master
```








### Git Branches For Personal Projects Guidelines

#### Website and Blogging

Assume that I wrote a notebook named `blog.ipynb` and I want to publish it to my personal blog. Here are the general guidelines.

- Say that I put the notebook `blog.ipynb` in the `notebooks` folder in master branch.
- Then before I publish, I have a collaborator named **Joe** who is also a collaborator of my personal blog (who acts as my editor).
- I will create a new branch named `blog` and push the notebook to the branch.
- Then I will commit the notebook to the branch and create a pull request for **Joe** to review. 
    - If **Joe** approves the pull request, then I will merge the branch to the master branch using `squash and merge` or `merge commit`.
    - If **Joe** proposes some small changes, I will then go my branch `blog` and make the changes locally, and commit them with a pull request for **Joe** again. Once he approved, I will merge the branch to the master branch.
- After the merge, I will delete the branch `blog` as the updates are reflected in the master branch.

The above can be outlined in pseudo code below:

```bash
# Place the notebook `blog.ipynb` in the `notebooks` folder in master branch.
# Create a new branch named `blog` and push the notebook to the branch.
git checkout -b <new-branch-name> blog
git status # to see the status of the current branch.
# Convert the notebook to markdown if needed.
jupyter nbconvert --to markdown mynotebook.ipynb
# Commit the notebook to the branch.
git add .
git commit -a
git push origin branch_name -u
# Go to the pull request link, and select reviewer for review.
# If no changes proposed, merge the branch to master.
# If there are changes proposed, edit the codes in the branch locally and push the changes to the branch for review again. After that go to the same link and click on re-review.
```

After review and approved by the reviewer, you have 3 merge options.

- Squash and Merge: Take all the commits during the review and merge them into one commit. The only downside is you cannot go back to one unique commit but you will see all commit messages tho and changes.
- Create a merge commit: Create a merge commit with the changes from the review. You can use this if you want `git` to track every single commit (messages).

The merge will mean it is updated in master branch also. Then delete the branch if not in use.

---

## Handling Merge Conflicts

...


## Commit Courtesy

!!! tip
    Files that are changed in sync should be committed together. As an example, you made changes to three files, a, b and c, if a and b are related and c is unrelated to both of them, then it is logical to do the following:
    ```bash
    git add a b
    git commit -a "Commit related files"
    git add c
    git commit -a "Commit c file"
    ```

and https://github.com/aisingapore/PeekingDuck/blob/main/CONTRIBUTING.md



## GIT Readme Profile

Instructions [here](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-profile/customizing-your-profile/managing-your-profile-readme) and [template](https://github.com/khuyentran1401/khuyentran1401/blob/master/README.md).