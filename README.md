gitplug
=======

git plugin for ranger file manager.

*This project is a fork of [ranger-gitplug](https://github.com/ywwa/ranger-gitplug) with a bit more command support*

Feel free to create issues for any bugs.

#### Install:

##### Using the MakeFile

For most users, the Makefile script should be enough. Follow the following instructions,

```
git clone https://github.com/yonghie/ranger-gitplug
cd ranger-gitplug
make install
```

##### Manually

Copy the ```gitplug.py``` file into the ranger's ```plugins``` folder. 

#### Working command list:
* ```:git help```
* ```:git init```
* ```:git status```
* ```:git clone <url>```
* ```:git add <file>```
* ```:git rm <file>```
* ```:git restore <file>``` 
* ```:git commit <text>``` 
* ```:git remote add/rm <name> <url>```
* ```:git push```
* ```:git reset [--soft | --hard]```
* ```:git checkout [-b] <branch name>```
* ```:git pull```
* ```:git fetch```
* ```:git diff [branch_name]```

#### TODO:
* [ ] Better visibility for git pull
