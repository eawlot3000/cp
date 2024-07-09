*to delete the first line and the last line*

now what is .rstrip()

try this:
```python
a = '''
  *
 ***
*****
 ***
  *
'''
print(a)
```


and this:
```python
a = '''
  *
 ***
*****
 ***
  *
'''

a = a[a.find('\n')+1:a.rfind('\n')]

print(a)
```
[workout](https://www.runoob.com/python/att-string-rfind.html)


