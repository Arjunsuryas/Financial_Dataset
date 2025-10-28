X = df_encoded.drop(columns=['charges'])
y = df_encoded['charges']
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
