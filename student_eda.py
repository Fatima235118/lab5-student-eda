import pandas as pd
import matplotlib.pyplot as plt

# --------------------------------------------------
# 1. Create student dataset with 12 students
# --------------------------------------------------

data = {
    "StudentID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    "Gender": [
        "Female", "Male", "Female", "Male", "Female", "Male",
        "Female", "Male", "Female", "Male", "Female", "Female"
    ],
    "StudyHours": [5, 3, 6, 4, 7, 2, 5, 6, 8, 3, 4, 7],
    "Attendance(%)": [90, 82, 95, 78, 92, 75, 88, 85, 96, 80, 87, 91],
    "Marks": [85, 68, 90, 65, 92, 60, None, 72, 95, None, 75, 88]
}

df = pd.DataFrame(data)

# Add one exact duplicate row
df = pd.concat([df, df.iloc[[4]]], ignore_index=True)

# Save dataset as CSV
df.to_csv("student_performance.csv", index=False)

print("Student dataset created successfully.")
print()

# --------------------------------------------------
# 2. Load CSV using pd.read_csv()
# --------------------------------------------------

df = pd.read_csv("student_performance.csv")

print("Shape:", df.shape)
print()

print("Data Information:")
df.info()
print()

# --------------------------------------------------
# 3. Missing values and duplicate rows
# --------------------------------------------------

print("Missing values per column:")
print(df.isnull().sum())
print()

print("Duplicate rows:", df.duplicated().sum())
print()

# --------------------------------------------------
# 4. Drop duplicate and fill missing Marks with median
# --------------------------------------------------

df = df.drop_duplicates()

marks_median = df["Marks"].median()
df["Marks"] = df["Marks"].fillna(marks_median)

print("After cleaning:", df.shape)
print("Marks median used for filling:", marks_median)
print()

# --------------------------------------------------
# 5. Histogram of Marks
# --------------------------------------------------

plt.figure(figsize=(8, 5))
plt.hist(df["Marks"], bins=6, edgecolor="black")
plt.title("Distribution of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig("marks_histogram.png")
plt.show()

# --------------------------------------------------
# 6. Boxplot of Marks
# --------------------------------------------------

plt.figure(figsize=(7, 5))
plt.boxplot(df["Marks"])
plt.title("Boxplot of Student Marks")
plt.ylabel("Marks")
plt.tight_layout()
plt.savefig("marks_boxplot.png")
plt.show()

# --------------------------------------------------
# 7. Scatter plot: StudyHours vs Marks
# --------------------------------------------------

plt.figure(figsize=(8, 5))
plt.scatter(df["StudyHours"], df["Marks"])
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.grid(True)
plt.tight_layout()
plt.savefig("studyhours_vs_marks.png")
plt.show()

# --------------------------------------------------
# 8. Full numeric correlation matrix
# --------------------------------------------------

print("Correlation matrix:")
print(df[["StudyHours", "Attendance(%)", "Marks"]].corr())
print()

# --------------------------------------------------
# 9. Gender-wise average Marks and Attendance
# --------------------------------------------------

gender_analysis = df.groupby("Gender")[["Marks", "Attendance(%)"]].mean()

print("Average Marks and Attendance by Gender:")
print(gender_analysis)
print()

print("Saved marks_histogram.png, marks_boxplot.png, studyhours_vs_marks.png")