import numpy as np


# owner, non owner -> 0, 1

# RAW - FEATURE ENGINEERING - MODEL TRAINING - EVALUATION


import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder, MinMaxScaler


df = pd.DataFrame({
    # "dept" : ["sales", "hr", "it", "sales", "hr"],
    # "level" : ["junior", "senior", "mid", "senior", "junior"],
    "salary" : [50000, 80000, 60000, 75000, 55000, 1000000],
})


# le = LabelEncoder()
# df["level_encoded"] = le.fit_transform(df["level"])

# print(df['level_encoded'].unique())
# print(df['level_encoded'].values)

# ohe = OneHotEncoder(sparse_output=False)
# dept_encoded = ohe.fit_transform(df[["dept"]])
# dept_encoded_df = pd.DataFrame(dept_encoded, columns=ohe.get_feature_names_out(["dept"]))
# df = pd.concat([df, dept_encoded_df], axis=1)

# # print(df)

# # X = df.drop(["dept", "level", "salary"], axis=1)
# # y = df["salary"]

# scaler = StandardScaler()
# df["salary_scaled"] = scaler.fit_transform(df[["salary"]]) 

# scaler_mm = MinMaxScaler()
# df["salary_scaled_mm"] = scaler_mm.fit_transform(df[["salary"]])

#Handling Outliers

Q1 = df["salary"].quantile(0.25)
Q3 = df["salary"].quantile(0.75)
IQR = Q3 - Q1

outlier_threshold_low = Q1 - 1.5 * IQR
outlier_threshold_high = Q3 + 1.5 * IQR

print("Outlier thresholds:", outlier_threshold_low, outlier_threshold_high)

outliers = df[(df["salary"] < outlier_threshold_low) | (df["salary"] > outlier_threshold_high)]
print("Outliers in salary column:")
print(outliers)

df = pd.DataFrame({
    "age" : np.random.randint(0, 15, 1000),
})

df["age_group"] = pd.cut(df["age"], 
                         bins=[0, 3, 6, 10, 15, np.inf], 
                         labels=["beginner", "intermediate", "advanced", "senior", "supersenior"])

df["age_quartiles"] = pd.qcut(df["age"], q=4, labels=["Q1", "Q2", "Q3", "Q4"])
print(df)