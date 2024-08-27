import matplotlib.pyplot as plt
import time
import random

def generate_live_data():
    while True:
        data = [random.randint(10, 50) for _ in range(10)]
        yield data
        time.sleep(1)  # Adjust the sleep time based on your data update frequency

def update_barplot(data):
    plt.clf()  # Clear the previous plot
    plt.bar(range(len(data)), data)
    plt.xlabel("Data Points")
    plt.ylabel("Values")
    plt.title("Live Data Barplot")
    plt.draw()
    plt.pause(0.001)  # Short pause for visualization

# Create the initial barplot
data = next(generate_live_data())
update_barplot(data)

# Continuously update the barplot with new data
for new_data in generate_live_data():
    update_barplot(new_data)
