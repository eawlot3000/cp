#### python浮点数舍入round()方式总结

###### ROUND HALF EVEN
round half even也被称为银行家舍入法，这种舍入方法的规则是：如果数字与两边（相同位数）的数字相等，就向偶数方向舍入，如果不相等，就是就近舍入。（
Round to nearest with ties going to nearest even integer. ）

python内置的round函数，采用的就是ROUND HALF
EVEN舍入方法（清楚了哈，round函数不是在做四舍五入）：

```python
>>> round(1.2222,0)
1.0
>>> round(1.9999,0)
2.0
>>> round(1.265,2)
1.26
>>> round(1.275,2)
1.27
>>> round(1.285,2)
1.28
>>> round(1.235,2)
1.24
>>> round(-1.235,2)
-1.24
>>> round(-1.265,2)
-1.26
>>> round(-1.285,2)
-1.28
```

