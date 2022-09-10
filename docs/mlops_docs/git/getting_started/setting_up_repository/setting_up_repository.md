We will closely follow the [Atlassian's Getting Started Tutorial](https://www.atlassian.com/git/tutorials/setting-up-a-repository).

As stated in their tutorial, this section's high level overview:

- Initializing a new Git repo
- Cloning an existing Git repo
- Committing a modified version of a file to the repo
- Configuring a Git repo for remote collaboration
- Common Git version control commands

## Initialize an Entirely New Repository: `git init`

To create a new repo, you'll use the `git init` command;
this a one-time command you use during the initial setup of a new repo. 

Executing this command will create a new `.git` subdirectory in your current working directory. 

This will also create a new `main/master` branch. 

```bash title="initialize a new repo" linenums="1"
~/gaohn              $ mkdir {git_tutorial}
~/gaohn              $ cd {git_tutorial}
~/gaohn/git_tutorial $ git init

> Initialized empty Git repository in /Users/gaohn/git_tutorial/.git/
```

This command will generate a hidden `.git` directory for your project, where Git stores all internal tracking data for the current repository.

```bash
~/gaohn/git_tutorial $ ls -a
```

!!! info "Read More"
    Visit the [Atlassian's git init tutorial](https://www.atlassian.com/
    git/tutorials/setting-up-a-repository/git-init) for more details.

---

## Initialize a Repository from an Existing Project: `git clone`

If a project has already been set up in a ***remote repository***, the clone command is the most 
common way for users to obtain a local development clone. 

Like `git init`, cloning is generally a one-time operation. Once a developer has obtained a working 
copy, all version control operations are managed through their local repository.

```bash title="clone a repo" linenums="1"
~/gaohn $ git clone <repo url>
```

For example, I have a repository stored on GitHub called [https://github.com/ghnreigns/
github-test.git](https://github.com/ghnreigns/github-test.git) and I can clone it to my 
local machine by filling `<repo url>` with the url of the repository.

```bash title="clone a repo" linenums="1"
~/gaohn $ git clone https://github.com/ghnreigns/github-test.git

> Cloning into 'github-test'...
> remote: Enumerating objects: 6, done.
> remote: Counting objects: 100% (6/6), done.
> remote: Compressing objects: 100% (2/2), done.
> remote: Total 6 (delta 0), reused 0 (delta 0), pack-reused 0
> Receiving objects: 100% (6/6), done.
```

Then you will see a new directory called `github-test` in your current working directory and 
you do not need to run `git init` on this directory.

These two commands cover the ground of initializing a repository locally.

!!! info "Read More"
    Visit the [Atlassian's git clone tutorial](https://www.atlassian.com/git/tutorials/
    setting-up-a-repository/git-clone) for more details.

## Initialize Remote Repository

Generally stored outside of your isolated local system, usually on a remote server.
It's especially useful when working in teams - this is the place where you can share your project 
code, see other people's code and integrate it into your local version of the project, and also push 
your changes to the remote repository.

For our purpose, we will be using GitHub as our remote repository, you can initialize one following
the [GitHub's tutorial](https://docs.github.com/en/github/getting-started-with-github/create-a-repo).

!!! Tip
    Many people suggest one to first create a remote repository and then clone it to their local
    machine for development, where you need not run `git init` on the local directory.