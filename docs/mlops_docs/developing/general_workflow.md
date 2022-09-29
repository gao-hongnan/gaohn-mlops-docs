## Gearing Up For Development

### Set Up Main Directory (IDE)

Let us assume that we are residing in our root folder `~/gaohn` and
we want to create a new project called **YOLO**, we can do as follows:

```bash title="creating main directory" linenums="1"
~/gaohn      $ mkdir YOLO && cd YOLO
~/gaohn/YOLO $ code .                 # (1)
```
            
1.  Open the project directory in Visual Studio Code. To change appropriately if using different IDE.

If you are cloning a repository to your local folder **YOLO**, you can also do:

```bash title="cloning repository" linenums="1"
~/gaohn/YOLO $ git clone https://github.com/gao-hongnan/gaohn-yolov1-pytorch.git .
```

where `.` means cloning to the current directory.

### Set Up Git

The steps to setting up git can be found [here](../git/introduction.md).
Be sure to have a read before proceeding.

### Set Up Virtual Environment

Follow the steps below to set up a virtual environment for your development.

=== "Windows"

    ```bash title="venv" linenums="1"
    ~/gaohn/YOLO        $ python -m venv <venv_name>                               # (1)
    ~/gaohn/YOLO        $ <venv_name>\Scripts\activate                             # (2)
    ~/gaohn/YOLO (venv) $ python -m pip install --upgrade pip setuptools wheel     # (3)
    ```

    1.  Create virtual environment named `venv` in the current directory.
    2.  Activate virtual environment.
    3.  Upgrade pip, setuptools and wheel.

=== "macOS M1"

    ```bash title="venv" linenums="1"
    ~/gaohn/YOLO        $ pip3 install virtualenv 
    ~/gaohn/YOLO        $ virtualenv venv_name>                                          
    ~/gaohn/YOLO        $ source venv_name>\bin\activate
    ~/gaohn/YOLO (venv) $ python3 -m pip install --upgrade pip setuptools wheel
    ```

=== "Linux"

    ```bash title="venv" linenums="1"
    ~/gaohn/YOLO        $ sudo apt install python3.8 python3.8-venv python3-venv 
    ~/gaohn/YOLO        $ python3 -m venv venv_name>                        
    ~/gaohn/YOLO        $ source venv_name>\bin\activate                                 
    ~/gaohn/YOLO (venv) $ python3 -m pip install --upgrade pip setuptools wheel      
    ```

You should see the following directory structure:

```tree title="main directory tree" linenums="1"
YOLO/
└── venv/
```

### Requirements and Setup

### Requirements

!!! note
    For small projects, we can have `requirements.txt` and just run `pip install -r requirements.txt`.
    For larger projects, we can add a `setup.py` file.

    In short, `requirements.txt` specifies the dependencies of your project, and [`setup.py`](https://
    stackoverflow.com/questions/60145069/what-is-the-purpose-of-setup-py) file informs you about the 
    module or package-dependencies you are about to install has been packaged and distributed with
    Distutils, which is the standard for distributing Python Modules. You can skip `setup.py` if you
    are just using `requirements.txt` to install dependencies.

    Refer to [madewithml](https://madewithml.com/courses/mlops/packaging/)'s
    **requirements** and **setup** section for more details.      

```bash title="creating requirements" linenums="1"
~/gaohn/YOLO (venv) $ touch requirements.txt                              
~/gaohn/YOLO (venv) $ pip install -r requirements.txt                          
```

```bash title="insert into requirements.txt" linenums="1"
~/gaohn/YOLO (venv) $ cat > requirements.txt
torch==1.10.0+cu113
torchaudio===0.10.0+cu113
torchvision==0.11.1+cu113
albumentations==1.1.0
matplotlib==3.2.2
pandas==1.3.1
torchinfo==1.7.1
tqdm==4.64.1
wandb==0.12.6
```   
  
!!! Tip
    Something worth taking note is when you download PyTorch Library, 
    there is a dependency link since we are downloading cuda directly, you may execute as such:
  
    ```bash
    ~/gaohn/YOLO (venv) $ pip install -r -f https://download.pytorch.org/whl/torch_stable.html requirements.txt
    ```

### Setup

To use `setup.py` file, we first create a `setup.py` file and add the following:

```bash title="creating setup.py" linenums="1"
~/gaohn/YOLO (venv) $ touch setup.py
```

```bash title="insert into setup.py" linenums="1"
~/gaohn/YOLO (venv) $ cat > setup.py
# Setup installation for the application

from pathlib import Path

from setuptools import setup

BASE_DIR = Path(__file__).parent

# Load packages from requirements.txt
with open(Path(BASE_DIR, "requirements.txt")) as file:
    required_packages = [ln.strip() for ln in file.readlines()]

with open(Path(BASE_DIR, "dev_requirements.txt")) as file:
    dev_packages = [ln.strip() for ln in file.readlines()]

setup(
    name="gaohn-yolov1",
    version="0.1",
    license="MIT",
    description="YOLOv1 Implementation in PyTorch.",
    author="Hongnan G",
    author_email="reighns.sjr.sjh.gr.twt.hrj@gmail.com",
    url="",
    keywords=["machine-learning", "deep-learning", "object-detection"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.8",
    install_requires=[required_packages],
    extras_require={"dev": dev_packages},
    dependency_links=[],
    entry_points={
        "console_scripts": [
            "gaohn_yolo= src.main:app",
        ],
    },
)
```

In `line 11-12`, we are loading the required packages from `requirements.txt`. So instead
of calling `pip install -r requirements.txt`, we can call the below command:

```bash title="installing packages" linenums="1"
~/gaohn/YOLO (venv) $ pip install -e . -f https://download.pytorch.org/whl/torch_stable.html
```

However, if you are using the code repository for further developing, then packages such as
linters, formatters and testing frameworks should be installed as well. In line `line 14-15`,
we specify a variable `dev_packages` to load the packages from `dev_requirements.txt`.

```bash title="creating dev_requirements.txt" linenums="1"
~/gaohn/YOLO (venv) $ python -m pip install -e ".[dev]"     # installs required + dev packages
```
      
You should see the following directory structure:

```tree title="main directory tree" linenums="1"
YOLO/
├── venv/
├── dev_requirements.txt
├── requirements.txt
└── setup.py
```

## Setup Main Directory (IDE) (SEE HERE FOR YOLOV1)

Let us create our main directory for the project:

```bash title="creating main directory" linenums="1"
$ mkdir pkd_exercise_counter
$ cd pkd_exercise_counter
$ code .                      # (1)
```

1.  Open the project directory in Visual Studio Code. To change appropriately if using different IDE.

## Virtual Environment 

Set up a virtual environment in your IDE.

!!! note "Virtual Environment"
    If you are using Linux or Mac, then you may need to install the virtual environment manager. For windows, python comes with a virtual environment manager `venv` installed.

    ```bash title="install venv" linenums="1"
    $ sudo apt install python3.8 python3.8-venv python3-venv  # For Ubuntu
    $ pip3 install virtualenv                                 # For Mac
    ```

You can activate the virtual environment (assuming Windows) as follows:

```bash title="virtual environment windows" linenums="1"
$ python -m venv venv_pkd_exercise_counter                      # (1)
$ .\venv_pkd_exercise_counter\Scripts\activate                  # (2)
(venv) $ python -m pip install --upgrade pip setuptools wheel   # (3)
```

1.  Create virtual environment.
2.  Activate virtual environment.
3.  Upgrade pip.

!!! note
    Although the virtual environment name is `venv_pkd_exercise_counter`, it is too long and I will use `venv` for future references.


You should see the following directory structure:

```tree title="main directory tree" linenums="1"
pkd_exercise_counter/
└── venv_pkd_exercise_counter/
```

## Requirements and Setup

!!! note
    We note that `echo > "filename"` command is used to create a file in Windows. One can use `touch` in other OS such as macOS or even `code` if you are using Visual Studio Code.

```bash title="creating requirements" linenums="1"
(venv) $ echo > setup.py 
(venv) $ echo > requirements.txt 
(venv) $ pip install -e .
```

- `#!bash [Line 1-2]`: [`setup.py`](https://stackoverflow.com/questions/60145069/what-is-the-purpose-of-setup-py) file informs you about the module or package-dependencies you are about to install has been packaged and distributed with Distutils, which is the standard for distributing Python Modules. You can skip `setup.py` if you are just using `requirements.txt` to install dependencies.
- `#!bash [Line 3]`: Installs packages from `requirements.txt`. One can also use commands such as `python -m pip install -e ".[dev]"` to install additional dev packages specified in `setup.py`.

After which we quickly run a verification to see if PeekingDuck is installed correctly.

```bash title="peekingduck verification" linenums="1"
(venv) $ peekingduck --verify_install
```

!!! info
    In my `setup.py`, I specified `python` to be $3.8$ and above. This has been tested on ubuntu latest and windows latest in GitHub Actions.

You should see the following directory structure:

```tree title="main directory tree" linenums="1"
pkd_exercise_counter/
├── venv_pkd_exercise_counter/
├── requirements.txt
└── setup.py
```

## Git

Git is a version control system that is used to track changes to files. It is integral to the development process of any software. Here we initiate our main directory with git.

!!! note
    The commands below may differ depending on personal style and preferences. (i.e. ssh or https)

```bash title="git" linenums="1"
(venv) $ echo > README.md 
(venv) $ echo > .gitignore 
(venv) $ git init
(venv) $ git config --global user.name "Your Name"
(venv) $ git config --global user.email "your@email.com"                               # (1) 
(venv) $ git add .
(venv) $ git commit -a                                                                 # (2)
(venv) $ git remote add origin "your-repo-http"                                        # (3)
(venv) $ git remote set-url origin https://[token]@github.com/[username]/[repository]  # (4)
(venv) $ git push origin master -u                                                     # (5)
```

1.  important to set the email linked to the git account.
2.  write commit message.
3.  add remote origin.
4.  set the remote origin.
5.  push to remote origin.

## Styling and Formatting

We will be using a very popular blend of style and formatting conventions that makes some very opinionated decisions on our behalf (with configurable options)[^styling_made_with_ml].

- [`black`](https://black.readthedocs.io/en/stable/): an in-place reformatter that (mostly) adheres to PEP8.
- [`isort`](https://pycqa.github.io/isort/): sorts and formats import statements inside Python scripts.
- [`flake8`](https://flake8.pycqa.org/en/latest/index.html): a code linter with stylistic conventions that adhere to PEP8.

We also have `pyproject.toml` and `.flake8` to configure our formatter and linter.

```bash title="create pyproject.toml and .flake8" linenums="1"
(venv) $ echo > pyproject.toml
(venv) $ echo > .flake8
```

For example, the configuration for `black` below tells us that our maximum line length should be $79$ characters. We also want to exclude certain file extensions and in particular the **virtual environment** folder we created earlier. 

```toml title="pyproject.toml" linenums="1"
# Black formatting
[tool.black]
line-length = 79
include = '\.pyi?$'
exclude = '''
/(
      \.eggs         # exclude a few common directories in the
    | \.git          # root of the project
    | \.hg
    | \.mypy_cache
    | \.tox
    | _build
    | buck-out
    | build
    | dist
    | venv_*
  )/
'''
```

You can run `black --check` to check if your code is formatted correctly or `black .` to format your code.

[^styling_made_with_ml]: This part is extracted from [madewithml](https://madewithml.com/courses/mlops/styling/).

## Mkdocs

### Mkdocs Setup

We will be using [Mkdocs](https://www.mkdocs.org/) to generate our markdown documentation into a static website.

1. The following requirements are necessary to run `mkdocs`:

    ```txt title="requirements.txt" linenums="1"
    mkdocs                            1.3.0
    mkdocs-material                   8.2.13
    mkdocs-material-extensions        1.0.3
    mkdocstrings                      0.18.1
    ```

2. Initialize default template by calling `mkdocs new .` where `.` refers to the current directory. The `.` can be replaced with a path to your directory as well. Subsequently, a folder `docs` alongside with `mkdocs.yml` file will be created.
   
    ```tree title="mkdocs folder structure" linenums="1" hl_lines="3 4 5"
    pkd_exercise_counter/
    ├── venv_pkd_exercise_counter/
    ├── docs/
    │   └── index.md
    ├── mkdocs.yml
    ├── requirements.txt
    └── setup.py
    ```

3. We can specify the following configurations in `mkdocs.yml`:

    ???+ example "Show/Hide mkdocs.yml"
        ```yml title="mkdocs.yml" linenums="1"
        site_name: Hongnan G. PeekingDuck Exercise Counter
        site_url: ""
        nav:
          - Home: index.md
          - PeekingDuck:
            - Setup: workflows.md
            - Push-up Counter: pushup.md
        theme:
          name: material
          features:
            - content.code.annotate
        markdown_extensions:
          - attr_list
          - md_in_html
          - admonition
          - footnotes
          - pymdownx.highlight
          - pymdownx.inlinehilite
          - pymdownx.superfences
          - pymdownx.snippets
          - pymdownx.details
          - pymdownx.arithmatex:
              generic: true
        extra_javascript:
          - javascript/mathjax.js
          - https://polyfill.io/v3/polyfill.min.js?features=es6
          - https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js
        extra_css:
            - css/extra.css
        plugins:
          - search 
          - mkdocstrings # plugins for mkdocstrings
        ```

    Some of the key features include:

    - [Code block Line Numbering](https://squidfunk.github.io/mkdocs-material/reference/code-blocks/);
    - [Code block Annotations](https://squidfunk.github.io/mkdocs-material/reference/code-blocks/);
    - [MathJax](https://squidfunk.github.io/mkdocs-material/reference/mathjax/).

    One missing feature is the ability to **toggle** code blocks. Two workarounds are provided:

    ??? "Toggle Using Admonition"
        ```bash title="Setting Up"
        mkdir custom_hn_push_up_counter 
        ```

    <details>
    <summary>Toggle Using HTML</summary>
    ```bash title="Setting Up"
    mkdir custom_hn_push_up_counter 
    ```
    </details>

4. We added some custom CSS and JavaScript files. In particular, we added `mathjax.js` for easier latex integration.
5. You can now call `mkdocs serve` to start the server at a local host to view your document.


!!! tip
    To link to a section or header, you can do this: [link to Styling and Formatting by [workflows.md#styling-and-formatting](workflows.md#styling-and-formatting).

### Mkdocstrings

We also can create docstrings as API reference using [Mkdocstrings](https://mkdocstrings.github.io/usage/):

- Install mkdocstrings: `pip install mkdocstrings`
- Place plugings to `mkdocs.yml`:
    ```yml title="mkdocs.yml" linenums="1"
    plugins:
      - search
      - mkdocstrings
    ```
- In `mkdocs.yml`'s navigation tree: 
    ```yml title="mkdocs.yml" linenums="1"
    - API Documentation: 
      - Exercise Counter: api/exercise_counter_api.md
    ```
    For example you have a python file called `exercise_counter.py` and want to render it, create a file named `api/exercise_counter_api.md` and in this markdown file:

    ```md title="api/exercise_counter_api.md" linenums="1"
    ::: custom_hn_exercise_counter.src.custom_nodes.dabble.exercise_counter # package path.
    ```

## Tests

Set up `pytest` for testing codes.

```bash title="Install pytest" linenums="1"
pytest==6.0.2
pytest-cov==2.10.1
```

In general, **Pytest** expects our testing codes to be grouped under a folder called `tests`. We can configure in our `pyproject.toml` file to override this if we wish to ask `pytest` to check from a different directory. After specifying the folder holding the test codes, `pytest` will then look for python scripts starting with `tests_*.py`; we can also change the extensions accordingly if you want `pytest` to look for other kinds of files (extensions)[^testing_made_with_ml].

```bash title="pyproject.toml" linenums="1"
# Pytest
[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = "test_*.py"
```

[^testing_made_with_ml]: This part is extracted from [madewithml](https://madewithml.com/courses/mlops/testing/#pytest).

## CI/CD (GitHub Actions)

The following content is with reference to:

- [MLOps Basics [Week 6]: CI/CD - GitHub Actions](https://www.ravirajag.dev/blog/mlops-github-actions)
- [CI/CD for Machine Learning](https://madewithml.com/courses/mlops/cicd/)

We will be using [GitHub Actions](https://github.com/features/actions) to setup our mini CI/CD.

### Commit Checks

Commit checks is to ensure the following:

- The requirements can be installed on various OS and python versions.
- Ensure code quality and adherence to PEP8 (or other coding standards).
- Ensure tests are passed.

```yaml title="lint_test.yml" linenums="1"
name: Commit Checks                                                                                             # (1)
on: [push, pull_request]                                                                                        # (2)

jobs:                                                                                                           # (3)
  check_code:                                                                                                   # (4)
    runs-on: ${{ matrix.os }}                                                                                   # (5)
    strategy:                                                                                                   # (6)
      fail-fast: false                                                                                          # (7)
      matrix:                                                                                                   # (8)
        os: [ubuntu-latest, windows-latest]                                                                     # (9)
        python-version: [3.8, 3.9]                                                                              # (10)
    steps:                                                                                                      # (11)
      - name: Checkout code                                                                                     # (12)
        uses: actions/checkout@v2                                                                               # (13)
      - name: Setup Python                                                                                      # (14)
        uses: actions/setup-python@v2                                                                           # (15)
        with:                                                                                                   # (16)
          python-version: ${{ matrix.python-version }}                                                          # (17)
          cache: "pip"                                                                                          # (18)
      - name: Install dependencies                                                                              # (19)
        run: |                                                                                                  # (20)
          python -m pip install --upgrade pip setuptools wheel
          pip install -e . 
      - name: Run Black Formatter                                                                               # (21)
        run: black --check .                                                                                    # (22)
      # - name: Run flake8 Linter
      #   run: flake8 . # look at my pyproject.toml file and see if there is a flake8 section, if so, run flake8 on the files in the flake8 section
      - name: Run Pytest                                                                                        # (23)
        run: python -m coverage run --source=custom_hn_exercise_counter -m pytest && python -m coverage report  # (24)
```

1.  This is the name that will show up under the **Actions** tab in GitHub. Typically, we should name it appropriately like how we indicate the subject of an email.
2.  The list here indicates the [workflow will be triggered](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#pull_request) whenever someone directly pushes or submits a PR to the main branch.
3.  Once an event is triggered, a set of **jobs** will run on a [runner](https://github.com/actions/runner). In our example, we will run a job called `check_code` on a runner to check for formatting and linting errors as well as run the `pytest` tests.
4.  This is the name of the job that will run on the runner.
5.  We specify which OS system we want the code to be run on. We can simply say `ubuntu-latest` or `windows-latest` if we just want the code to be tested on a single OS. However, here we want to check if it works on both Ubuntu and Windows, and hence we define `${{ matrix.os }}` where `matrix.os` is `[ubuntu-latest, windows-latest]`. A cartesian product is created for us and the job will run on both OSs.
6.  Strategy is a way to control how the jobs are run. In our example, we want the job to run as fast as possible, so we set `strategy.fail-fast` to `false`.
7.  If one job fails, then the whole workflow will fail, this is not ideal if we want to test multiple jobs, we can set `fail-fast` to `false` to allow the workflow to continue running on the remaining jobs.
8.  Matrix is a way to control how the jobs are run. In our example, we want to run the job on both Python 3.8 and 3.9, so we set `matrix.python-version` to `[3.8, 3.9]`.
9.  This list consists of the OS that the job will run on in cartesian product.
10. This is the python version that the job will run on in cartesian product. We can simply say `3.8` or `3.9` if we just want the code to be tested on a single python version. However, here we want to check if it works on both python 3.8 and python 3.9, and hence we define `${{ matrix.python-version }}` where `matrix.python-version` is `[3.8, 3.9]`. A cartesian product is created for us and the job will run on both python versions.
11. This is a list of dictionaries that defines the steps that will be run.
12. Name is the name of the step that will be run.
13. It is important to specify `@v2` as if unspecified, then the workflow will use the latest version from actions/checkout template, potentially causing libraries to break. The idea here is like your `requirements.txt` idea, if different versions then will break.
14. Setup Python is a step that will be run before the job.
15. Same as above, we specify `@v2` as if unspecified, then the workflow will use the latest version from actions/setup-python template, potentially causing libraries to break.
16. With is a way to pass parameters to the step.
17. This is the python version that the job will run on in cartesian product and if run 1 python version then can define as just say 3.7
18. Cache is a way to control how the libraries are installed.
19. Install dependencies is a step that will be run before the job.
20. `|` is multi-line string that runs the below code, which sets up the libraries from `setup.py` file.
21. Run Black Formatter is a step that will be run before the job.
22. Runs `black` with configurations from `pyproject.toml` file.
23. Run Pytest is a step that will be run before the job.
24. Runs pytest, note that I specified `python -m` to resolve PATH issues.

### Deploy to Website 

The other workflow for this project is to deploy the website built from Mkdocsto gh-pages branch.

??? example "Show/Hide content for deploy_website.yml"
    ```yaml title="deploy_website.yml" linenums="1"
    name: Deploy Website to GitHub Pages

    on: 
      push:
        branches: [master]
        paths: 
          - "docs/**"
          - "mkdocs.yml"
          - ".github/workflows/deploy_website.yml"
      
    permissions: write-all

    jobs:
      deploy:
        runs-on: ubuntu-latest
        name: Deploy Website
        steps:
          - uses: actions/checkout@v2
          - name: Set Up Python
            uses: actions/setup-python@v2
            with:
              python-version: 3.8
              architecture: x64
          - name: Install dependencies
            run: | # this symbol is called a multiline string
              python -m pip install --upgrade pip setuptools wheel
              pip install -e . 

          - name: Build Website
            run: |
              mkdocs build
          - name: Push Built Website to gh-pages Branch
            run: |
              git config --global user.name 'Hongnan G.'
              git config --global user.email 'reighns92@users.noreply.github.com'
              ghp-import \
              --no-jekyll \
              --force \
              --no-history \
              --push \
              --message "Deploying ${{ github.sha }}" \
              site
    ```