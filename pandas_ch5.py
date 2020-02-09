import pandas as pd 

df = pd.DataFrame([10, 20, 30, 40],
	columns=['numbers'],
	index=['a', 'b', 'c', 'd']) 


print(f"df :\n {df}")

print("\n")

print(f"df.index : {df.index}")

print("\n")

print(f"df.columns : {df.columns}")

print("\n")

print(f"df.loc['c'] : {df.loc['c']}")
