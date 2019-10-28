# IMAGE MAGIC
https://ctflearn.com/problems/89

### Problem
It looks like someone messed up my picture! Can anyone reorganize the pixels? The python module PIL (Python Imaging Library) might be useful! https://mega.nz/#!OKxByZyT!vaabCJRG5D9zAUp7drTekcA5pszu67r_TbQMtxEzqGE 

### Hints:
- I think whoever messed up my image took every column of pixels and put them side by side. 
- I think the width of the image was 304 before they messed with it.

### install
- prerequisites
```sh
$ brew install pipenv
```

- dependency install
```sh
$ pipenv install
```

### Solution
```sh
$ pipenv run python ctf.py
```