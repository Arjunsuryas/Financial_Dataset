# ------------------------------------------------------------
#  Visualization — Predicted vs Actual Charges
# ------------------------------------------------------------
plt.figure(figsize=(7,6))
plt.scatter(y, y_pred_cv, alpha=0.6)
plt.plot([y.min(), y.max()], [y.min(), y.max()], '--', color='black')
plt.xlabel("Actual Charges")
plt.ylabel("Predicted Charges (5-Fold CV)")
plt.title(f"Predicted vs Actual Charges\nR²={overall_r2:.3f}, MAE={overall_mae:.2f}")
plt.tight_layout()
plt.show()
