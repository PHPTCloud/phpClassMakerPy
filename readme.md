# phpClassMakerPy
---

##### Installation (linux)
1. Clone phpClassMaker.py
2. Put file int comfortable directory on your machine (e.g. /etc/customScripts/)
3. Create alias to make simple call of script (optional)
```
alias makeClass='python3 /your/script/path/phpClassMaker.py'
```
4. Create json file which will be association of php class (e. class.json)
```
{
    "name": "MyClass",
    "package": "App",
}
```
5. Run maker script in terminal
```
# using alias
makeClass </your/json/file/path> <your-json-file-name.json>
```
6. Result: int /your/json/file/path you can see your generated php class (GOAL!)

#### Json structure
```
{
    "name": "required",
    "package": "required",
    "extends": "optional",
    "implements": "optional",
    "fields": "optional"
}
```
- name - name of class;
- package - namespace;
- extends - extends from some class;
- implements - implementation through comma;
- fields - fields of class:


```
...
"implements": "UseImplements, ThroughCommaSign "
...
"fields": {
    "private": {
        "nameOfField": "TypeOfField"
    },
    "protected": {...},
    "public": {...},
}
...
```

[Demo video](https://youtu.be/O12VgHHZmEo)
