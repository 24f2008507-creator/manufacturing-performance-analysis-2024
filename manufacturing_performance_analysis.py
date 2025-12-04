import matplotlib.pyplot as plt

# Quarterly equipment efficiency data for 2024
quarters = ["Q1", "Q2", "Q3", "Q4"]
efficiency = [69.72, 74.38, 76.2, 76.97]
industry_target = 90

# Basic analysis
average_efficiency = sum(efficiency) / len(efficiency)
print(f"Average equipment efficiency (2024): {average_efficiency:.2f}")
print(f"Industry target efficiency: {industry_target}")

# Calculate gap to target per quarter
gaps = [industry_target - x for x in efficiency]
print("Gap to target per quarter:")
for q, e, g in zip(quarters, efficiency, gaps):
    print(f"  {q}: efficiency={e:.2f}, gap={g:.2f} points")

# Trend direction
if efficiency[-1] > efficiency[0]:
    print("Trend: Overall improvement across the year, but still below target.")
else:
    print("Trend: No improvement across the year, and still below target.")

# Visualization: line chart with benchmark
# PR update to include .py file in changes

plt.figure(figsize=(8, 5))
plt.plot(quarters, efficiency, marker="o", label="Equipment Efficiency (2024)")
plt.axhline(y=industry_target, linestyle="--", label="Industry Target (90)")
plt.ylim(60, 95)
plt.xlabel("Quarter")
plt.ylabel("Efficiency Rate")
plt.title("2024 Quarterly Equipment Efficiency vs Industry Target")
plt.legend()
plt.tight_layout()
plt.savefig("efficiency_trend_vs_target.png", dpi=120)
# plt.show()  # Uncomment to view interactively
