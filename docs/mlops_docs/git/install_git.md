## Installation and Configuration

### Installing Git

We have to ensure that we have Git installed on our machine. 
Different operating systems have different ways of installing Git.
The following command downloads Git to macOS:

```bash title="install git" linenums="1"
~/gaohn $ brew install git # (1)
```

1. Use Homebrew to install git manager.

Once Git is installed, we can check the version of Git we have installed:

```bash title="check git version" linenums="1"
~/gaohn $ git --version 
```

!!! info "Read More"
    Visit [Atlassian's Install Git Tutorial](https://www.atlassian.com/git/tutorials/install-git)
    for more information on installing Git.

---

### Configure Name and Email

In your terminal, configure your **Git username** and **email** using the following commands: 

```bash title="configure git" linenums="1"
~/gaohn $ git config --global user.name <your name>
~/gaohn $ git config --global user.email <your email>
```

replacing `<your name>` with your own name, and set the `user.email` to the email address you used to sign up for GitHub.

These details will be associated with any commits that you create!

!!! note
    This step is particularly important if you are working with multiple git accounts.
    This is because setting the config globally will affect your commits.
    
    For example, if I have two git accounts called `a1` and `a2` with emails
    `a1@gmail.com` and `a2@gmail.com` respectively. If I set my global config
    of the `user.email` to `a1@gmail.com`, then any commits made by `a2` will
    be credited to `a1` as contributor.

!!! info "Read More"
    Visit [Atlassian's Configuring Git Tutorial](https://www.atlassian.com/git/tutorials/setting-up-a
    -repository/git-config) for more details.


