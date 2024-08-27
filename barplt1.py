import matplotlib.pyplot as plt

# Sample data (adjust as needed)
team_members = ['Submitted', 'Active', 'Viewed', 'NotViewed', 'Meeting to be held']

performance_points = [47, 14, 24, 23, 1]  # Adjust values
colors=['skyblue','green','lightgreen','yellow','cyan']

# Create the barplot
plt.figure(figsize=(12, 6))
plt.bar(team_members, performance_points, color=colors)
plt.xlabel("Categories",color='red',fontsize=16)
plt.ylabel("Proposals", color='cyan',fontsize=16)
plt.title("Proposal and Response",color='blue')

# Show the chart
plt.show()