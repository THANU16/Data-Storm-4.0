import numpy as np
import matplotlib.pyplot as plt

# Generate synthetic data for annual salaries (in USD)
np.random.seed(0)  # For reproducibility
num_samples = 100
min_salary = 50000
max_salary = 120000
salaries = np.random.randint(min_salary, max_salary, size=num_samples)

# Create a histogram to visualize the salary distribution
plt.figure(figsize=(10, 6))
plt.hist(salaries, bins=15, edgecolor='k', alpha=0.7)
plt.xlabel('Annual Salary (USD)')
plt.ylabel('Number of Data Modeling Analysts')
plt.title('Salary Distribution for Data Modeling Analysts')
plt.grid(True)
plt.show()
