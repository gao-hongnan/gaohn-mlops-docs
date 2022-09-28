<div align="center">
<h1>MLOps Documentation</a></h1>
by Hongnan Gao
Sep, 2022
<br>
</div>


<h4 align="center">
  <a href="https://gao-hongnan.github.io/gaohn-mlops-docs/mlops_docs/git/introduction/">Git</a>
  <span> · </span>
  <a href="https://gao-hongnan.github.io/gaohn-mlops-docs/mlops_docs/developing/general_workflow/">General Workflow</a>
</h4>

This is the documentation for various MLOps concepts.

## Contributing

Fork the repository and make changes as you like. When you think your changes are ready to 
be merged, open a pull request.

This documentation is developed on [MkDocs](https://www.mkdocs.org/). If you are not familiar with MkDocs,
markdown syntax is also supported.

```bash
$ git clone https://github.com/gao-hongnan/gaohn-mlops-docs.git gaohn_mlops_docs
$ cd gaohn_mlops_docs
$ python -m venv <venv_name> && <venv_name>\Scripts\activate 
(venv_name) $ python -m pip install --upgrade pip setuptools wheel
(venv_name) $  pip install -r requirements.txt
(venv_name) $  mkdocs serve
```