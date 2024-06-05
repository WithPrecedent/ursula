# ursula

<p align="center">
<img src="https://github.com/WithPrecedent/ursula/blob/main/docs/img/ursula_le_guin.png?raw=true" alt="ursula logo" style="width:250px;"/>
</p>

“*A writer is a person who cares what words mean, what they say, how they say it. Writers know words are their way towards truth and freedom, and so they use them with care, with thought, with fear, with delight. By using words well they strengthen their souls. Story-tellers and poets spend their lives learning that skill and art of using words well. And their words make the souls of their readers stronger, brighter, deeper.*”
― Ursula K. Le Guin

| | |
| --- | --- |
| Version | [![PyPI Latest Release](https://img.shields.io/pypi/v/ursula.svg?style=for-the-badge&color=steelblue&label=PyPI&logo=PyPI&logoColor=yellow)](https://pypi.org/project/ursula/) [![GitHub Latest Release](https://img.shields.io/github/v/tag/WithPrecedent/ursula?style=for-the-badge&color=navy&label=GitHub&logo=github)](https://github.com/WithPrecedent/ursula/releases)
| Status | [![Development Status](https://img.shields.io/badge/Development-Active-seagreen?style=for-the-badge&logo=git)](https://www.repostatus.org/#active) [![Project Stability](https://img.shields.io/pypi/status/ursula?style=for-the-badge&logo=pypi&label=Stability&logoColor=yellow)](https://pypi.org/project/ursula/)
| Documentation | [![Hosted By](https://img.shields.io/badge/hosted_by-GitHub_Pages-blue?style=for-the-badge&color=navy&logo=github)](https://withprecedent.github.io/ursula)
| Compatibility | [![Compatible Python Versions](https://img.shields.io/pypi/pyversions/ursula?style=for-the-badge&color=steelblue&label=Python&logo=python&logoColor=yellow)](https://pypi.python.org/pypi/ursula/) [![Linux](https://img.shields.io/badge/Linux-lightseagreen?style=for-the-badge&logo=linux&labelColor=gray&logoColor=white)](https://www.linux.org/) [![MacOS](https://img.shields.io/badge/MacOS-snow?style=for-the-badge&logo=apple&labelColor=gray)](https://www.apple.com/macos/) [![Windows](https://img.shields.io/badge/windows-blue?style=for-the-badge&logo=Windows&labelColor=gray&color=orangered)](https://www.microsoft.com/en-us/windows?r=1)
| Stats | [![PyPI Download Rate (per month)](https://img.shields.io/pypi/dm/ursula?style=for-the-badge&color=steelblue&label=Downloads%20💾&logo=pypi&logoColor=yellow)](https://pypi.org/project/ursula) [![GitHub Stars](https://img.shields.io/github/stars/withprecedent/ursula?style=for-the-badge&color=navy&label=Stars%20⭐&logo=github)](https://github.com/withprecedent/ursula/stargazers) [![GitHub Contributors](https://img.shields.io/github/contributors/withprecedent/ursula?style=for-the-badge&color=navy&label=Contributors%20🙋&logo=github)](https://github.com/withprecedent/ursula/graphs/contributors) [![GitHub Issues](https://img.shields.io/github/issues/withprecedent/ursula?style=for-the-badge&color=navy&label=Issues%20📘&logo=github)](https://github.com/withprecedent/ursula/graphs/contributors) [![GitHub Forks](https://img.shields.io/github/forks/withprecedent/ursula?style=for-the-badge&color=navy&label=Forks%20🍴&logo=github)](https://github.com/withprecedent/ursula/forks) |
| | |

## What is ursula?

`ursula` is an easy-to-use `cookiecutter` template for academic markdown writing
projects that may include code. To see an example repository using this
template, check out
[`ursula_demo`](https://github.com/withprecedent/ursula_demo). The primary goal of
`ursula` is to store all of your materials for a project (writing, code,
presentations, data, images, media, etc.) in one organized location. Any given
project need not use all of the features and aspects of `ursula`, but they are
always there in case a project expands or changes direction.

Out of the box, `ursula` is designed for projects that:

* Write scholarship and make slides using
  [![Markdown](https://img.shields.io/badge/Markdown-deepskyblue?style=flat-square&logo=markdown&labelColor=gray)](https://www.markdownguide.org/)
  (any flavor, including [![Quarto](https://img.shields.io/badge/Quarto-steelblue?style=flat-square&logo=quarto&labelColor=gray)](https://quarto.org/))
* Plan to host your project on [![GitHub](https://img.shields.io/badge/GitHub-navy?style=flat-square&logo=github&labelColor=gray)](https://www.github.com/)
* May include [![Python](https://img.shields.io/badge/Python-steelblue?style=flat-square&logo=python&labelColor=gray)](https://www.python.org/) code[^1]
* Want replication and/or usage documentation automatically created using [![Documentation Tool](https://img.shields.io/badge/MkDocs-magenta?style=flat-square&color=deepskyblue&logo=markdown&labelColor=gray)](https://www.mkdocs.org/)
  with the [![Documentation Theme](https://img.shields.io/badge/Material-magenta?style=flat-square&color=deepskyblue&logo=material-design&logoColor=white&labelColor=gray)](https://squidfunk.github.io/mkdocs-material/) theme
  on [![Documentation Host](https://img.shields.io/badge/GitHub_Pages-blue?style=flat-square&color=navy&logo=github&labelColor=gray)](https://withprecedent.github.io/ursula)

## Why use ursula?

`ursula` is built on top of my general-use `Python` template:  [`snickerdoodle`](https://www.github.com/WithPrecedent/snickerdoodle). You
can read the `readme` for that template to understand its advantages versus
other templates. What `ursula` adds is support for academic writing projects.
This may include articles or books. Presentation slides and notes are also
stored and can use the same resources (images, tables, graphs, etc.) as the
publication.

### Tools

If you include `Python` code in your project, `ursula` includes these modern, stable tools for package construction and
management that do not require any external services or costs:

* Dependency management: [![Dependency Manager](https://img.shields.io/badge/PDM-mediumpurple?style=flat-square&logo=affinity&labelColor=gray)](https://PDM.fming.dev) and [![Dependency Maintainer](https://img.shields.io/badge/dependabot-navy?style=flat-square&logo=dependabot&logoColor=white&labelColor=gray)](https://github.com/dependabot)
* Testing: [![Testing](https://img.shields.io/badge/pytest-steelblue?style=flat-square&logo=pytest&logoolor=white&labelColor=gray)](https://github.com/TezRomacH/python-package-template/blob/master/.pre-commit-config.yaml)
* CI/CD: [![CI](https://img.shields.io/badge/GitHub_Actions-navy?style=flat-square&logo=githubactions&labelColor=gray&logoColor=white)](https://github.com/features/actions)
* Code style:
  [![Linter](https://img.shields.io/endpoint?style=flat-square&url=https://raw.githubusercontent.com/charliermarsh/Ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/Ruff),
  [![Pre-commit](https://img.shields.io/badge/pre--commit-darkolivegreen?style=flat-square&logo=pre-commit&logoColor=white&labelColor=gray)](https://github.com/TezRomacH/python-package-template/blob/master/.pre-commit-config.yaml),
  and [![Editor Settings](https://img.shields.io/badge/Editor_Config-paleturquoise?style=flat-square&logo=editorconfig&labelColor=gray)](https://editorconfig.org/)


### Options

In addition to the included tools above, `ursula` includes several
options in the `cookiecutter` questionnaire that can be automatically applied
as part of the templating process:

* Badge style: [![flat
  style](https://img.shields.io/badge/flat-crimson?style=flat)](https://www.shields.io/),
  [![flat-square
  style](https://img.shields.io/badge/flat--square-orange?style=flat-square)](https://www.shields.io/),
  [![for-the-badge
  style](https://img.shields.io/badge/For--the--badge-blue?style=for-the-badge)](https://www.shields.io/),
  [![plastic
  style](https://img.shields.io/badge/plastic-purple?style=plastic)](https://www.shields.io/),
 or [![social
  style](https://img.shields.io/badge/social-red?style=social)](https://www.shields.io/)
* Push an [initial commit](https://github.com/WithPrecedent/ursula_demo) to GitHub
* Build and deploy [basic documentation](https://withprecedent.github.io/ursula_demo/) to GitHub Pages
* Create a `Python` virtual environment in the repository's ".venv" Folder

## Getting started

### Setup

If you are new to `cookiecutter` or simply want to guarantee that the created repository works as intended, follow the instructions in the [`ursula` tutorial](https://withprecedent.github.io/ursula/tutorial/).

If you are familiar with `cookiecutter` templates, you can go about the
normal construction process. However, if you do not select the optional
automatic setup features in the questionnaire, you should follow the instructions
for manually setting up your [virtual
environment](https://withprecedent.github.io/ursula/tutorial/#Create-Virtual-Environment)
and [deploying your
documentation](https://withprecedent.github.io/ursula/tutorial/#Deploy-Documentation)
in the [`ursula`
tutorial](https://withprecedent.github.io/ursula/tutorial/). It is
especially important to follow the document deployment process for your initial deployment - after that GitHub Actions will automatically update and redeploy the
documentation (and you need not use the manual process again).

### Usage

After your repository is created, you can start coding right away. Every push to GitHub will run any tests in the "tests" folder,
deploy documentation to GitHub Pages, and apply `ruff` for linting and
formatting. For more information about the following topics, just click on the
corresponding hyperlink.

* [Formatting and Linting](https://withprecedent.github.io/ursula/advanced/#formatting-and-linting)
* [GitHub Actions](https://withprecedent.github.io/ursula/advanced/#github-actions)
* [Publishing](https://withprecedent.github.io/ursula/advanced/#publishing)
* [Repository Layout](https://withprecedent.github.io/ursula/advanced/#repository-layout)
* [Versioning](https://withprecedent.github.io/ursula/advanced/#versioning)

## Contributing

Contributors are always welcome and should find `ursula` easy to work
with. The template is highly documented so that users and developers can adapt
or extend`ursula` to work with their projects. So, forking and creating
different template spins is encouraged. If you want to contribute directly to
the project, feel free to grab an [issue](https://github.com/WithPrecedent/ursula/issues) to work on
or make a suggested improvement. If you wish to contribute, please read the
[Contribution Guide](./contributing.md) and [Code of
Conduct](./code_of_conduct.md).

## Similar Projects

These are other `cookiecutter` templates using `pdm` as their dependency manager:

* [cookiecutter-docker-python-pdm](https://github.com/mnako/cookiecutter-docker-python-pdm): uses Docker and `black`.
* [cookie](https://github.com/chris-santiago/cookie): uses `mkdocs` and GitHub Actions, but also adds `conda`, `nox`, `black`, and `pyright`.

If you are interested in going beyond `cookiecutter` (or its forks),
[`copier`](https://github.com/copier-org/copier) is a powerful, newer templating package
and there is a great template that incorporates
several of the tools used in `ursula`:

* [copier-pdm](https://github.com/pdm-project/copier-pdm): includes, among other
 tools, `pdm`,
  `mkdocs`, and `ruff`.

## Acknowledgements

I'd also like to extend a special thanks to [pawamoy](https://github.com/pawamoy) whose excellent `pdm` and `mkdocs` extensions and utlities are incorporated into `ursula`. Some of the scripts, documentation, configuration files, and other CI code were all adapted from pawamoy's repositories.

I would also like to thank the University of Kansas School of Law for tolerating and supporting this law professor's coding efforts, an endeavor which is well outside the typical scholarly activities in the discipline.

## License

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg?style=for-the-badge&color=firebrick&logo=apache)](https://opensource.org/licenses/Apache-2.0)

[^1]: Contributions to add support for other programming languages are welcome.