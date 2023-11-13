import random
import numpy as np
import matplotlib.pyplot as plt

initials = []
for i in range(10000):
    initial = 1000
    for j in range(1000):
        random_number = random.uniform(0, 1)
        if random_number < 0.5:
            initial *= 1.2
        else:
            initial *= 0.82
    initials.append(initial)

initials_array = np.array(initials)

mean_final = np.mean(initials_array)
median_final = np.median(initials_array)
std_dev = np.std(initials_array)
initial_amount = 1000
reward = (mean_final - initial_amount) / initial_amount
risk_reward_ratio = std_dev / reward

more_than_1000_count = np.sum(initials_array > 1000)

print('Percentage of People who made more than they started: ', more_than_1000_count / len(initials) * 100)
print('Mean Final Value: ', mean_final)
print('Median Final Value: ', median_final)
print('Standard Deviation: ', std_dev)
print('Risk Reward Ratio: ', risk_reward_ratio)

initials_array[initials_array > 2000] = 2100

indices = np.arange(len(initials))
values_more_than_1000 = initials_array[initials_array > 1000]
values_less_than_1000 = initials_array[initials_array <= 1000]

indices_more_than_1000 = indices[initials_array > 1000]
indices_less_than_1000 = indices[initials_array <= 1000]

plt.figure(figsize=(15, 7))
plt.scatter(indices_more_than_1000, values_more_than_1000, alpha=0.6, c='green', label='Final > 1000')
plt.scatter(indices_less_than_1000, values_less_than_1000, alpha=0.6, c='blue', label='Final ≤ 1000')
plt.axhline(y=1000, color='r', linestyle='-', label='Initial Value (1000)')

yticks = [0, 500, 1000, 1500, 2000, 2100]
ytick_labels = ['0', '500', '1000', '1500', '2000', '2000+']
plt.yticks(yticks, ytick_labels)

plt.title('Scatter Plot of Final Values')
plt.xlabel('Simulation Run Number')
plt.ylabel('Final Value')
plt.legend()
plt.grid(True)
plt.show()