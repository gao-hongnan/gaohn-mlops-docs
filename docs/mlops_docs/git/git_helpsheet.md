# Helpsheet

## Tips

```bash title="rebase onto upstream/dev" linenums="1"
$ git checkout main
$ git delete -D <branch-name>
$ git checkout <branch-name>
```

This solves the issues of sometimes having the local repo between two computers
not fully updating properly using `git pull` or `git fetch`. Make sure the 
`<branch-name>` in question is fully up to date on the remote repo first
before deleting it locally.