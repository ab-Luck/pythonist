import matplotlib.pyplot as plt

# Sample data (adjust as needed)
team_members = ['Mughees', 'Rizwan', 'Vishal', 'Jahanzeb', 'Zain',
                'Abrar', 'Farhan', 'Abdulrehman', 'Haroon', 'Riaz']

performance_points = [100, 80, 40, 70, 45, 90, 95, 75, 50, 100]  # Adjust values

# Define colors for each slice
colors = ['green', 'blue', 'red', 'orange', 'purple', 'yellow', 'cyan', 'magenta', 'black', 'gray']

# Create the pie chart with colors
plt.figure(figsize=(8, 8))
plt.pie(performance_points, labels=team_members, autopct='%1.1f%%', colors=colors)
plt.title("RepTech Team Performance")

# Show the chart
plt.show()