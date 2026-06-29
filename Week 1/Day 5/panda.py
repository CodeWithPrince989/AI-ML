import pandas as pd
df = pd.DataFrame({
"Name": ["Alice", "Bob"],
"Cgpa": [9.5, 8.7]
})

# Custom Indexing
s2 = pd.Series([23, 24, 25, 26], index = ["Adam", "Eve", "Charlie", "Bob"])
print(s2["Eve"]) # 24
print(s2["Bob"]) # 26
# Vectorized Operations
s1 = pd.Series([1, 2, 3])
s2 = pd.Series([4, 5, 6])
print(s1 + s2)
# Mutable Values but immutable size
s = pd.Series([1, 2, 3, 4, 5])
s[0] = 100
print(s)
changed_s = s.drop(1)
print(changed_s)
print(s)

# Creating DataFrame in pandas - using dictionary
info = {
"Name" : ["Adam", "Eve", "Bob"],
"Marks" : [78, 99, 85],
"Grade" : ['B', 'O', 'A']
}
df = pd.DataFrame(info)
print(df)
print(type(df))
print(df.index) # row labels
print(df.columns) # column labels
# Creating DataFrom using Numpy array
np_arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
df = pd.DataFrame(np_arr, columns=["Col1", "Col2", "Col3"])
print(df)
# Creating DataFrom using Lists
l = [["Adam", 96], ["Eve", 75], ["Bob", 82], ["Charlie", 92]]
df = pd.DataFrame(l, columns=["Name", "Marks"])
print(df)