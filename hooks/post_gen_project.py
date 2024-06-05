"""Cookiecutter hook for post project generation."""


import pathlib
import subprocess
from collections.abc import MutableMapping

_FOLDERS: MutableMapping[str, list[str]] = {
    'data': ['final', 'modified', 'raw'],
    'presentations': [],
    'research': [],
    'results': [],
    'visuals': [],
    'writing': ['active', 'drafts', 'published', 'submission']}
_TRUES: tuple[bool | str] = ('y', True, 'true')


def execute_commands(
    commands: list[str],
    folder: str | pathlib.Path) -> None:
    """Executes all 'commands' using `subprocess.run`.

    Args:
        commands: tuple of a list of str commands.
        folder: path of repository folder.

    """
    # 'shell' must be set to False to use `subprocess` securely. Do NOT change
    # 'shell' to True.
    kwargs = {"cwd": folder, 'shell': False}
    for command in commands:
        subprocess.run(command, **kwargs, check = False)  # noqa: S603

def create_virtual_environment(folder: str | pathlib.Path) -> None:
    """Creates a virtual environment at '.venv' using `subprocess` and `pdm`.

    Args:
        folder: path of repository folder.
    """
    environment_commands = (
        ['pdm', 'install'],
        ['pdm', 'use', '-f', '.venv'])
    execute_commands(commands = environment_commands, folder = folder)

def commit_to_git_subprocess(url: str, folder: str | pathlib.Path) -> None:
    """Initializes and commits repository using `subprocess`.

    Args:
        url: url for GitHub repository with '.git' extension.
        folder: path of repository folder.

    """
    git_commands = (
        ['git', 'init'],
        ['git', 'add', '.'],
        ['git', 'commit', '-m', 'Initial commit'],
        ['git', 'remote', 'add', 'origin', url],
        ['git', 'push', '-u', 'origin', 'main'])
    execute_commands(commands = git_commands, folder = folder)

def build_and_deploy_docs(folder: str | pathlib.Path) -> None:
    """Builds and deploys docs using `subprocess`, `pdm`, and `mkdocs`.

    Args:
        folder: path of repository folder.

    """
    docs_commands = (
        ['pdm', 'run', 'mkdocs', 'build'],
        ['pdm', 'run', 'mkdocs', 'gh-deploy', '--force', '--clean'])
    execute_commands(commands = docs_commands, folder = folder)

def create_folders(folders: MutableMapping[str, list[str]], root: str) -> None:
    """Creates folders on disk.

    This is done through a function rather than the `cookiecutter` template
    because GitHub doesn't sync empty folders. Rather than use the common clunky
    solution of creating `.gitkeep` files in each folder, this template simply
    writes them to disc. The one possible shortcoming to this approach is that
    the created project will not sync folders until they have a file in them.
    However, that makes for a cleaner GitHub repository because unneeded folders
    will not appear there.

    Args:
        folders: keys are names of the outer folder and values are lists of
            subfolders, if applicable.
        root: the `str` name of the root folder from which new folders should be
            created.

    """
    root = pathlib.Path(root)
    for folder, subfolders in folders.items():
        if subfolders:
            for subfolder in subfolders:
                full_path = root.joinpath(folder).joinpath(subfolder)
                full_path.mkdir(parents = True, exist_ok = True)
        else:
            full_path = root.joinpath(folder)
            full_path.mkdir(parents = True, exist_ok = True)

def main() -> None:
    """Executes post repository generation scripts."""
    folder = pathlib.Path.cwd()
    if "{{ cookiecutter.create_virtual_environment }}".lower() in _TRUES:
        create_virtual_environment(folder = folder)
    if "{{ cookiecutter.commit_to_github }}".lower() in _TRUES:
        repo_url = '{{ cookiecutter.url }}'
        git_url = ''.join([repo_url, '.git'])
        commit_to_git_subprocess(url = git_url, folder = folder)
        if "{{ cookiecutter.create_virtual_environment }}".lower() in _TRUES:
            build_and_deploy_docs(folder = folder)
        else:
            print(  # noqa: T201
                'Cannot deploy documentation without creating a virtual '
                'environment')
    create_folders(root = '.', folders = _FOLDERS)

if __name__ == "__main__":
    main()
