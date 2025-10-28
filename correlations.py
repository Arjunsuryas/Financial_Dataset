corr_matrix = df_encoded.corr()
charges_corr = corr_matrix['charges'].sort_values(key=lambda x: x.abs(), ascending=False)
corr_table = charges_corr.reset_index()
corr_table.columns = ['Feature', 'Correlation with Charges']
display(corr_table.head(15))
