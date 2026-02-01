import pandas as pd

file_path = r"C:/Users/ASUS/OneDrive/Desktop/sem-6/DMW/Practical-3/employees.csv"
df = pd.read_csv(file_path)

df.columns = df.columns.str.strip().str.lower()

print("\nDataset Loaded Successfully\n")

print("1) Total Employees:", len(df))

print("\n2) Total Departments:")
print(df["department_id"].nunique())

print("\n3) Maximum Salary in each Department:")
print(df.groupby("department_id")["salary"].max())

print("\n4) Employee with Minimum Salary:")
print(df.loc[df["salary"].idxmin()])

print("\n5) Total Salary in each Department:")
print(df.groupby("department_id")["salary"].sum())

print("\n6) Total Managers:")
print(df[df["job_id"].str.contains("man", case=False)].shape[0])

print("\n7) Number of Employees in each Department:")
print(df.groupby("department_id").size())

print("\n8) Maximum Salary in Organization:")
print(df["salary"].max())

print("\n9) Employees with Job ID = SA_MAN:")
print(df[df["job_id"] == "sa_man"])

print("\n10) Average Salary in each Department:")
print(df.groupby("department_id")["salary"].mean())

print("\n11) Employees Working Under Each Manager:")
print(df.groupby("manager_id").size())

print("\n12) Employee with Maximum Commission:")
print(df.loc[df["commission_pct"].idxmax()][["first_name", "last_name"]])

print("\n13) Designation-wise Maximum Salary:")
print(df.groupby("job_id")["salary"].max())

print("\n14) Designation-wise Total Salary:")
print(df.groupby("job_id")["salary"].sum())
