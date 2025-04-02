import matplotlib.pyplot as plt
import numpy as np

def generate_line(a, c, x_min, x_max):
    x = np.linspace(x_min, x_max, 100)
    y = a * x + c
    return x, y

def generate_scatter(a, c, x_min, x_max, num_points, noise_level):
    x = np.random.uniform(x_min, x_max, num_points)
    y = a * x + c + np.random.normal(0, noise_level, num_points)
    return x, y

def save_scatter_to_file(x, y, filename):
    np.savetxt(filename, np.column_stack((x, y)), header="x y", comments="")

def main():
    a = float(input("Enter the value of a: "))
    c = float(input("Enter the value of c: "))
    x_min = float(input("Enter the minimum value of x: "))
    x_max = float(input("Enter the maximum value of x: "))
    num_points = int(input("Enter the number of scatter points: "))
    noise_level = float(input("Enter the noise level (standard deviation): "))
    filename = input("Enter the filename to save the scatter points: ")

    x_line, y_line = generate_line(a, c, x_min, x_max)
    x_scatter, y_scatter = generate_scatter(a, c, x_min, x_max, num_points, noise_level)

    plt.plot(x_line, y_line, label=f"y = {a}x + {c}")
    plt.scatter(x_scatter, y_scatter, label="Scatter points", alpha=0.5)
    plt.title(f"Line y = {a}x + {c} with scatter points")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    plt.legend()
    plt.show()

    save_scatter_to_file(x_scatter, y_scatter, filename)
    print(f"Scatter points saved to {filename}")

if __name__ == "__main__":
    main()
