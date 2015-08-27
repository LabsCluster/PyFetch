# PyFetch
This is a fetch tool for web content
# Requirement
This tool require wget tools 
# Very easy using
1.First, you should download ```pyfetch.py``` to your dir.

2.Import PyFetch in your app: 
```python
import pyfetch 
```

3.Using built-in functions!
```python
fetch('http://google.com','index.html')
```
# Advanced functions
## Need Auth
Using ```fetchA()``` instead of ```fetch()```:
```python
fetchA('http://google.com','index.html','username','password')
```
## Need customized User-Agent
Using ```fetchU()``` instead of ```fetch()```:
```python
fetchA('http://google.com','index.html','Chrome 40')
```
