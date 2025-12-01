import matplotlib.pyplot as plt
import numpy as np

# --- 1. Line Chart ---
plt.figure(figsize=(8, 5)) # Optional: set figure size
x = np.linspace(0, 10, 100) # 100 evenly spaced points from 0 to 10
y = np.sin(x)
plt.plot(x, y, label='sin(x) function', color='blue', linestyle='--')
plt.title('Simple Line Chart')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.legend() # Show the label for the line
plt.grid(True) # Add a grid
plt.show()

# --- 2. Bar Chart ---
plt.figure(figsize=(8, 5))
categories = ['A', 'B', 'C', 'D', 'E']
values = [23, 45, 56, 12, 39]
plt.bar(categories, values, color=['skyblue', 'lightcoral', 'lightgreen', 'orange', 'plum'])
plt.title('Simple Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()

# --- 3. Scatter Plot ---
plt.figure(figsize=(8, 5))
np.random.seed(42) # for reproducibility
x_scatter = np.random.rand(50) * 10
y_scatter = np.random.rand(50) * 10
colors = np.random.rand(50) # for different colors for each point
sizes = np.random.rand(50) * 500 # for different sizes for each point
plt.scatter(x_scatter, y_scatter, c=colors, s=sizes, alpha=0.7, cmap='viridis')
plt.title('Simple Scatter Plot')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.colorbar(label='Color intensity') # Show color scale
plt.show()

# --- 4. Histogram ---
plt.figure(figsize=(8, 5))
data_hist = np.random.randn(1000) # 1000 random numbers from a standard normal distribution
plt.hist(data_hist, bins=30, color='teal', edgecolor='black', alpha=0.7)
plt.title('Simple Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# --- 5. Pie Chart ---
plt.figure(figsize=(7, 7)) # Pie charts often look better with a square aspect ratio
sizes_pie = [15, 30, 45, 10]
labels_pie = ['Apples', 'Bananas', 'Cherries', 'Dates']
colors_pie = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0, 0.1, 0, 0) # "explode" the 2nd slice (Bananas)

plt.pie(sizes_pie, explode=explode, labels=labels_pie, colors=colors_pie,
        autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Simple Pie Chart')
plt.show()

# --- 6. Box Plot ---
plt.figure(figsize=(8, 5))
data_box = [np.random.normal(0, std, 100) for std in range(1, 4)]
# This creates 3 datasets:
# - 100 points from N(0, 1)
# - 100 points from N(0, 2)
# - 100 points from N(0, 3)

plt.boxplot(data_box, patch_artist=True,  # fill with color
            boxprops=dict(facecolor='lightblue', medianprops=dict(color='red')))
plt.xticks([1, 2, 3], ['Dataset 1', 'Dataset 2', 'Dataset 3'])
plt.title('Simple Box Plot')
plt.ylabel('Values')
plt.grid(axis='y', linestyle='--', alpha=0.7) # Add horizontal grid lines
plt.show()