df_encoded = pd.get_dummies(df, drop_first=True)
print("Encoded dataset shape:", df_encoded.shape)
