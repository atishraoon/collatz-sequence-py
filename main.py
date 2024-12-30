import matplotlib.pyplot as plt
import numpy as np
import json
import sys

def draw_collatz(data):
    """Function to plot the Collatz sequences for multiple numbers."""
    for number, (x, y) in data.items():
        plt.plot(x, y, label=f"Collatz sequence for {number}", linestyle="-")
    plt.xlabel("Steps")
    plt.ylabel("Values")
    plt.title("Collatz Sequences for Multiple Numbers")
    plt.legend()
    plt.show()

def collatz_sequence(n):
    """Function to generate the Collatz sequence for a single number."""
    steps = 1
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps += 1
        sequence.append(n)

    # Generate x-axis values corresponding to the steps
    counts = list(range(steps))
    return counts, sequence

if __name__ == "__main__":
    # Ask user for the range of numbers to plot
    try:
        start = int(input("Enter the start of the range: "))
        end = int(input("Enter the end of the range: "))
        if start <= 0 or end < start:
            raise ValueError("Invalid range. Ensure start > 0 and end >= start.")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    # Generate Collatz sequences for the specified range
    data = {}
    json_data = {"collatz_sequence": []}

    for i in range(start, end + 1):
        x, y = collatz_sequence(i)
        data[i] = (np.array(x), np.array(y))

        # Append the sequence details to the JSON object
        json_data["collatz_sequence"].append({
            "value": i,
            "counts": x,
            "resultent": y
        })

    # Check if JSON export is requested via command-line arguments
    if len(sys.argv) > 1 and sys.argv[1] == 'json':
        with open("collatz_sequences.json", "w") as json_file:
            json.dump(json_data, json_file, indent=4)
        print("Collatz sequences saved to 'collatz_sequences.json'.")

    # Draw the plot for all sequences
    draw_collatz(data)
