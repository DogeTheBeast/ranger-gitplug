gitplug
=======

git plugin for ranger file manager.

*This project is a fork of [ranger-gitplug](https://github.com/ywwa/ranger-gitplug) with a bit more command support*

Feel free to create issues for any bugs.

#### Install:
```
git clone https://github.com/yonghie/ranger-gitplug
cd ranger-gitplug
make install
```

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
- [x] ```:git push```
- [x] ```:git remote```
- [ ] ```:git pull```
- [ ] ```:git checkout```
- [ ] ```:git reset```
- [ ] ```:git fetch```
- [x] ```:git diff ```
