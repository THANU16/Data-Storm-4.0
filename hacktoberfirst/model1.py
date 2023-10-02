import numpy as np
import matplotlib.pyplot as plt

# Generate synthetic data for annual salaries (in USD) for three locations
np.random.seed(0)  # For reproducibility
num_samples_per_location = 100
min_salary = 50000
max_salary = 120000

# Generate salary data for three locations: New York, San Francisco, and Chicago
salaries_ny = np.random.randint(min_salary, max_salary, size=num_samples_per_location)
salaries_sf = np.random.randint(min_salary + 10000, max_salary + 10000, size=num_samples_per_location)
salaries_chi = np.random.randint(min_salary - 10000, max_salary - 10000, size=num_samples_per_location)

# Create a box plot to visualize the salary distribution by location
data = [salaries_ny, salaries_sf, salaries_chi]
labels = ['New York', 'San Francisco', 'Chicago']

plt.figure(figsize=(10, 6))
plt.boxplot(data, labels=labels)
plt.xlabel('Location')
plt.ylabel('Annual Salary (USD)')
plt.title('Salary Distribution by Location for Data Modeling Analysts')
plt.grid(True)
plt.show()
