# mkminutes
Generate new minutes for use with devops.tex

## Setting up mkminutes:

- make `config.py` with:
```python
MEMBERS=[]
SECRETARY=
CHAIRMAN=
```

- clone `git@github.com:DevOps-Utrecht/devops.tex`
- link `devops.tex/devops_minutes.cls` and `devops.tex/devops_typography.cls` from your `TEXMFHOME/tex/latex/comonstuff` directory.
    - You can find `TEXMFHOME` by typing `kpsewhich -var-value=TEXMFHOME` (default is `~/texmf`)
- run `./mkminutes`
