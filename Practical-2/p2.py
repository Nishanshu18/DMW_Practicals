import pandas as pd

file_path = r"C:/Users/ASUS/OneDrive/Desktop/sem-6/DMW/Practical-2/NBA_2018-19_Season - NBA_2018-19_Season.csv"
df = pd.read_csv(file_path)

print("\nDataset Loaded Successfully\n")

print("1) Average Age:", df["Age"].mean())

print("\n2) Games played by each player:")
print(df[["Player", "Games"]])

print("\n3) Total Teams:", df["Team"].nunique())

print("\n4) Minimum Age:", df["Age"].min())

print("\n5) Maximum Age Player Details:")
print(df[df["Age"] == df["Age"].max()])

print("\n6) Total Games in Eastern Region:")
print(df[df["Conference"] == "Eastern"]["Games"].sum())

print("\n7) Total Regions:", df["Conference"].nunique())

print("\n8) Players from Boston Celtics:")
print(df[df["Team"] == "Boston Celtics"]["Player"])

print("\n9) Total Games in each Division:")
print(df.groupby("Division")["Games"].sum())

print("\n10) Player with Maximum Points:")
print(df.loc[df["Points"].idxmax()])

print("\n11) Player with Lowest Personal Fouls:")
print(df.loc[df["Personal Fouls"].idxmin()])

print("\n12) Player with Highest 3-Point Attempts:")
print(df.loc[df["3-Point Field Goal Attempts"].idxmax()]
      [["Player", "3-Point Field Goal Attempts", "3-Point Field Goal Percentage"]])

print("\n13) Average Points:", df["Points"].mean())

print("\n14) Average Age by Division:")
print(df.groupby("Division")["Age"].mean())

print("\n15) Total Fouls in each Team:")
print(df.groupby("Team")["Personal Fouls"].sum())
