dispersion = df_encoded.std() / df_encoded.mean()
dispersion_table = dispersion.reset_index()
dispersion_table.columns = ['Feature', 'Dispersion Ratio']
dispersion_table = dispersion_table.sort_values(by='Dispersion Ratio', ascending=False)

print("\n  Top variables by Dispersion Ratio:")
display(dispersion_table.head(10))

# Plot Dispersion Ratios
plt.figure(figsize=(8,5))
sns.barplot(y='Feature', x='Dispersion Ratio', data=dispersion_table.head(10))
plt.title("Top 10 Features by Dispersion Ratio")
plt.tight_layout()
plt.show()
