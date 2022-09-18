## Test Packages Compatibility

We can use GitHub Actions to test for compatibility on different Operating Systems (OS) such as Windows/Linux.

```yaml title="packages_compatibility.yml" linenums="1"
name: Commit Checks
on: [push, pull_request] 

jobs:
  check_code:
    runs-on: ${{ matrix.os }}
    strategy:
      fail-fast: true 
      matrix:
        os: [ubuntu-latest, windows-latest]
        python-version: [3.7]
    steps: 
      - name: Checkout code 
        uses: actions/checkout@v2 
      - name: Setup Python
        uses: actions/setup-python@v2 
        with:
          python-version: ${{ matrix.python-version }}
          cache: "pip"
      - name: Install dependencies
        run: | 
          python -m pip install --upgrade pip setuptools wheel
          pip install -r requirements.txt
```

- `#!python [Line 10]`: This line tells us that we want to test the installation on both Ubuntu and Windows Latest version.
- `#!python [Line 11]`: This line tells us that we want to test the installation on python version 3.7.
- `#!python [Lines 21-23]`: This line tells us that we will run the installation using `pip` on `requirements.txt` file.