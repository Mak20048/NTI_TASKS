import numpy as np
sales =np.random.uniform(100, 500, size=(4,7))
sales =np.where(sales>300, 0, sales*1.10 ,sales)
sales =np.where(sales<200, 0, sales*0.95 ,sales)
weekend = sales[:, -2:]
weekend_average = np.mean(weekend)
print(sales)
print("average weekend sales:", weekend_average)
