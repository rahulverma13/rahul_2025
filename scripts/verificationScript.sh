#!/bin/bash

# Display versions of specified tools and packages

echo "Version Information:"

# Homebrew
echo -n "Homebrew: "
brew --version | head -n 1

# Ruby
echo -n "Ruby: "
ruby -v

# Bundler
echo -n "Bundler: "
bundle -v

# Python
echo -n "Python: "
python --version

# mdless
echo -n "mdless: "
mdless --version

# Core Jupyter packages
echo "Core Jupyter Packages:"

# IPython
echo -n "IPython: "
python -c 'import IPython; print(IPython.__version__)'

# ipykernel
echo -n "ipykernel: "
python -c 'import ipykernel; print(ipykernel.__version__)'

# ipywidgets
echo -n "ipywidgets: "
python -c 'import ipywidgets; print(ipywidgets.__version__)'

# jupyter_client
echo -n "jupyter_client: "
python -c 'import jupyter_client; print(jupyter_client.__version__)'

# jupyter_server
echo -n "jupyter_server: "
python -c 'import jupyter_server; print(jupyter_server.__version__)'

# jupyterlab
echo -n "jupyterlab: "
python -c 'import jupyterlab; print(jupyterlab.__version__)'

# nbclient
echo -n "nbclient: "
python -c 'import nbclient; print(nbclient.__version__)'

# nbconvert
echo -n "nbconvert: "
python -c 'import nbconvert; print(nbconvert.__version__)'

# nbformat
echo -n "nbformat: "
python -c 'import nbformat; print(nbformat.__version__)'

# notebook
echo -n "notebook: "
python -c 'import notebook; print(notebook.__version__)'

# Project directory information
echo "Project Directory Information:"

# List project directory
echo -n "Project Directory: "
pwd

# Project name (assuming the project name is the directory name)
project_name=rahul_2025
echo -n "Project Name: $project_name"

# GitHub repo name (assuming the directory is a git repo)
if [ -d ".git" ]; then
    echo -n "GitHub Repo Name: rahul_2025"
    repo_url=$(git config --get remote.origin.url)
    if [[ $repo_url =~ ^https://github.com/([^/]+)/([^/]+)\.git$ ]]; then
        echo "${BASH_REMATCH[2]}"
    else
        echo "Not a GitHub repository or URL format is unexpected."
    fi
else
    echo "Not a Git repository."
fi

