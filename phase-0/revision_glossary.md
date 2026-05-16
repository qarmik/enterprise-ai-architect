# Session 7 Revision Glossary

## Core workflow terms

- **GitHub Codespaces**: A cloud-based development environment where code, files, and terminal access run in a remote workspace.
- **Repository (repo)**: The project folder tracked by Git.
- **Branch**: A line of development inside a repository, such as `main`.
- **Commit**: A saved snapshot of code changes in Git.
- **Push**: Sending local commits to the remote GitHub repository.
- **CI workflow**: Automated checks that run on GitHub when code is pushed or a pull request is opened.

## Python terms

- **Python 3.12.1**: The exact Python version used locally in the Codespace.
- **Script**: A Python file that can be executed from the terminal.
- **Shebang**: The first line, such as `#!/usr/bin/env python3`, that tells the system which interpreter should run the file.
- **Function**: A named block of reusable code that performs one task.
- **Entry point**: The code that starts execution when the file is run directly, usually:
  ```python
  if __name__ == "__main__":
      main()
  ```
- **Argparse**: Python’s built-in module for reading command-line arguments.
- **Logging**: A structured way to print runtime information, warnings, or errors.
- **Path**: A file-system location, handled cleanly in Python using `pathlib.Path`.

## CSV and file terms

- **CSV**: A plain text file format that stores tabular data using commas.
- **Header row**: The first row in a CSV file, which defines the column names.
- **Row**: One record in the CSV file.
- **DictReader**: A Python CSV helper that reads each row as a dictionary using the header names as keys.
- **Filename mismatch**: A bug caused when the filename used in the command does not exactly match the real file name.
- **Relative path**: A file path written relative to the current working directory, such as `phase-0/sample_transactions.csv`.

## Transaction analysis terms

- **Transaction**: One banking event recorded in the CSV file.
- **Transaction type**: The category of a transaction, such as `CREDIT`, `DEBIT`, or `TRANSFER`.
- **Status**: Whether a transaction is `SUCCESS` or `FAILED`.
- **Processing time**: The time taken for a transaction to be processed, measured in milliseconds.
- **Failure rate**: The percentage of failed transactions out of the total number of transactions.
- **Percentile**: A value in sorted data used to show how high or low a result is compared with others.
- **p50**: The 50th percentile, often used as a rough median.
- **p95**: The 95th percentile, used to show slower cases near the high end.
- **p99**: The 99th percentile, used to show extreme slow cases.
- **Top transaction type**: The most frequently occurring transaction type in the data.

## Python error terms

- **SyntaxError**: An error caused by invalid Python syntax, such as an unnecessary colon.
- **IndentationError**: An error caused by inconsistent spacing or tabs in Python code.
- **AttributeError**: An error caused by trying to use an attribute or method name that does not exist.
- **NameError**: An error caused by using a name that has not been defined or imported.
- **FileNotFoundError**: An error raised when Python cannot find the file at the given path.
- **ValueError**: An error raised when a function gets a valid type of input but an invalid value, such as an empty transaction list.

## Testing terms

- **pytest**: The Python testing framework used in this project.
- **Test file**: A file that contains functions to check whether code behaves correctly.
- **Test case**: One individual check inside the test file.
- **Assertion**: A condition that must be true for the test to pass.
- **`pytest.raises()`**: A helper used to verify that a specific error is raised.
- **Local test run**: Running tests in the Codespaces terminal before relying on CI.
- **6 passed**: A result meaning all six tests executed successfully.

## Git and shell terms

- **`git add`**: Stages file changes so they are included in the next commit.
- **`git commit -m`**: Creates a commit with a message.
- **`git push origin main`**: Pushes commits to the `main` branch on GitHub.
- **`mv`**: A Linux command used to rename or move files.
- **`ls`**: A Linux command used to list files and directories.
- **Shell prompt**: The line where commands are typed in the terminal.
- **`>` prompt**: A shell continuation prompt showing that a command is incomplete, often because quotes were not closed.
- **Quote mismatch**: A shell error condition caused when a command starts a quoted string and never closes it.

## CI and workflow terms

- **GitHub Actions**: GitHub’s automation system for running workflows such as tests.
- **Workflow file**: A YAML file inside `.github/workflows/` that defines CI steps.
- **YAML**: A configuration format used by GitHub Actions workflows.
- **`actions/setup-python`**: A GitHub Action that installs the chosen Python version in CI.
- **Install dependencies**: The CI step that installs required Python packages.
- **`python -m pytest`**: A reliable way to run pytest through the active Python interpreter.
- **PATH**: An environment setting that tells the shell where executable commands can be found.
- **Exit code 1**: A failure status returned by a command or CI step.

## Debugging terms

- **Debugging**: The process of finding and fixing errors in code or commands.
- **Typo**: A small spelling mistake that can break code or commands.
- **Import**: A Python statement that brings in code from a module.
- **Missing import**: A bug where code uses something that was never imported.
- **Scope**: The region where a variable or imported name is available.
- **Mismatch**: A general problem where two things that must match do not, such as names, paths, or indentation.

## Key Session 7 lessons

- Small mismatches can cause large blockers.
- Exact filenames matter.
- Exact spelling matters in Python and Git.
- Consistent indentation matters in Python.
- A test may fail not because the main program is broken, but because the test itself is incomplete.
- Running tests locally before pushing helps isolate problems faster.