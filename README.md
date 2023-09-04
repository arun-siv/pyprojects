[![Build and Test](https://github.com/arun-siv/devops-from-zero/actions/workflows/main.yml/badge.svg)](https://github.com/arun-siv/devops-from-zero/actions/workflows/main.yml)
# devops-from-zero
#### Create all these files
`touch Makefile`

`touch requirements.txt`

`mkdir devopslib`

`touch devopslib/__init__.py`

`touch hello.py`

`touch test_hello.py`

#### Create virtual environment

1. Create a virtual env 
`virtualenv ~/.venv`

2. Source the venv
Edit .bashrc 
`source ~/.venv/bin/activate`

# Project scafolding
* [Makefile](https://github.com/arun-siv/devops-from-zero/blob/main/Makefile)
* [requirements.txt](https://github.com/arun-siv/devops-from-zero/blob/main/requirements.txt)
* [test_library.py](https://github.com/arun-siv/devops-from-zero/blob/main/test_devopslib.py)
* [library](https://github.com/arun-siv/devops-from-zero/tree/main/devopslib)

# References
[Devcontainer dockerfile](https://containers.dev/guide/dockerfile)
This reference talks about how to add a file name Dockerfile
```docker
FROM mcr.microsoft.com/devcontainers/base:ubuntu

```
In the devcontainer specify the reference to Dockerfile
```json
{
    "build": {
        // Path is relataive to the devcontainer.json file.
        "dockerfile": "Dockerfile"
    }
}
```