import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Generate synthetic data for annual salaries (in USD) for three locations and two employee types
np.random.seed(0)  # For reproducibility
num_samples_per_location = 100
min_salary = 50000
max_salary = 120000

# Generate salary data for three locations: New York, San Francisco, and Chicago
salaries_ny = np.random.randint(min_salary, max_salary, size=num_samples_per_location)
salaries_sf = np.random.randint(min_salary + 10000, max_salary + 10000, size=num_samples_per_location)
salaries_chi = np.random.randint(min_salary - 10000, max_salary - 10000, size=num_samples_per_location)

# Generate employee type data (0 for full-time, 1 for part-time)
employee_types = np.random.randint(2, size=num_samples_per_location)

# Generate age data between 22 and 65
ages = np.random.randint(22, 66, size=num_samples_per_location)

# Create a DataFrame to store the data
data = pd.DataFrame({'Location': np.repeat(['New York', 'San Francisco', 'Chicago'], num_samples_per_location),
                     'Employee_Type': np.tile(['Full-Time', 'Part-Time'], num_samples_per_location),
                     'Age': ages,
                     'Salary (USD)': np.concatenate([salaries_ny, salaries_sf, salaries_chi]),
                     })

# Create box plots to visualize salary distribution by location and employee type
plt.figure(figsize=(12, 8))
plt.xticks(rotation=45)
boxplot = sns.boxplot(x='Location', y='Salary (USD)', hue='Employee_Type', data=data, showfliers=False)
plt.xlabel('Location')
plt.ylabel('Annual Salary (USD)')
plt.title('Salary Distribution by Location and Employee Type for Data Modeling Analysts')
plt.grid(True)
plt.show()
