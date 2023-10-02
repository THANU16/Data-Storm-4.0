import numpy as np
import matplotlib.pyplot as plt

# Generate synthetic data for annual salaries (in USD), employee type, age, location, and company
np.random.seed(0)  # For reproducibility
num_samples_per_location = 100
min_salary = 50000
max_salary = 120000
locations = ['New York', 'San Francisco', 'Chicago']
employee_types = ['Full-Time', 'Part-Time', 'Contractor']
age_groups = ['18-30', '31-45', '46-60', '61+']
companies = ['Company A', 'Company B', 'Company C']

# Generate salary, employee type, age, location, and company data
salaries = np.random.randint(min_salary, max_salary, size=num_samples_per_location * len(locations) * len(companies))
employee_data = np.random.choice(employee_types, size=num_samples_per_location * len(locations) * len(companies))
age_data = np.random.choice(age_groups, size=num_samples_per_location * len(locations) * len(companies))
location_data = np.repeat(locations, num_samples_per_location * len(companies))
company_data = np.tile(np.repeat(companies, num_samples_per_location), len(locations))

# Create a box plot to visualize salary distribution by company, employee type, age group, and location
fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(16, 12), sharey=True)

for i, location in enumerate(locations):
    for j, company in enumerate(companies):
        ax = axes[i, j]
        location_mask = (location_data == location)
        company_mask = (company_data == company)
        data = [salaries[location_mask & company_mask & (employee_data == emp_type) & (age_data == age_group)]
                for emp_type in employee_types for age_group in age_groups]
        labels = [f'{emp_type}, {age_group}' for emp_type in employee_types for age_group in age_groups]

        ax.boxplot(data, labels=labels)
        ax.set_xlabel('Employee Type and Age Group')
        ax.set_title(f'Salary Distribution at {company} in {location}')

axes[0, 0].set_ylabel('Annual Salary (USD)')
plt.suptitle('Salary Distribution by Company, Employee Type, Age Group, and Location for Data Modeling Analysts', y=1.02)
plt.tight_layout()
plt.show()
