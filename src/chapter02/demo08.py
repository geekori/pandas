# DataFrame的向量操作
import pandas as pd

d1 = pd.DataFrame({
    'a':[1,3],
    'b':[4,5]
    })
d2 = pd.DataFrame({
    'a':[4,5],
    'b':[1,2]
    })
print(d1)
print(d2)
print(d1 * d2)
print(d1 / d2)
print(d1 + d2)
print(d1 - d2)
print(d1 ** d2)

