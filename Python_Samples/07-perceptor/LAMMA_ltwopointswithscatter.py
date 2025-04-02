import matplotlib.pyplot as plt
import numpy as np

def generate_scatter_around_point(x, y, num_points, noise_level):
    x_scatter = np.random.normal(x, noise_level, num_points)
    y_scatter = np.random.normal(y, noise_level, num_points)
    return x_scatter, y_scatter

def save_points_to_file(x1, y1, x2, y2, x_scatter1, y_scatter1, x_scatter2, y_scatter2, filename):
    with open(filename, 'w') as f:
        f.write("Center points:\n")
        f.write(f"{x1} {y1}\n")
        f.write(f"{x2} {y2}\n\n")
        f.write("Scatter points around ({}, {}):\n".format(x1, y1))
        for i in range(len(x_scatter1)):
            f.write(f"{x_scatter1[i]} {y_scatter1[i]}\n")
        f.write("\nScatter points around ({}, {}):\n".format(x2, y2))
        for i in range(len(x_scatter2)):
            f.write(f"{x_scatter2[i]} {y_scatter2[i]}\n")

def save_points_to_file_numpy(x1, y1, x2, y2, x_scatter1, y_scatter1, x_scatter2, y_scatter2, filename):
    center_points = np.array([[x1, y1], [x2, y2]])
    scatter_points1 = np.column_stack((x_scatter1, y_scatter1))
    scatter_points2 = np.column_stack((x_scatter2, y_scatter2))

    np.savetxt(filename, np.vstack((center_points, scatter_points1, scatter_points2)), header="x y", comments="")

def main():
    x1 = float(input("Enter the x-coordinate of the first point: "))
    y1 = float(input("Enter the y-coordinate of the first point: "))
    x2 = float(input("Enter the x-coordinate of the second point: "))
    y2 = float(input("Enter the y-coordinate of the second point: "))

    num_points = int(input("Enter the number of scatter points around each point: "))
    noise_level = float(input("Enter the noise level (standard deviation): "))
    filename = input("Enter the filename to save the points: ")

    x_scatter1, y_scatter1 = generate_scatter_around_point(x1, y1, num_points, noise_level)
    x_scatter2, y_scatter2 = generate_scatter_around_point(x2, y2, num_points, noise_level)

    plt.scatter(x_scatter1, y_scatter1, label=f"Scatter around ({x1}, {y1})", alpha=0.5)
    plt.scatter(x_scatter2, y_scatter2, label=f"Scatter around ({x2}, {y2})", alpha=0.5)
    plt.scatter([x1, x2], [y1, y2], marker='x', color='black', label="Center points", s=100)
    plt.title("Scatter around two points")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    plt.legend()
    plt.show()

    save_points_to_file_numpy(x1, y1, x2, y2, x_scatter1, y_scatter1, x_scatter2, y_scatter2, filename)
    print(f"Points saved to {filename}")

if __name__ == "__main__":
    main()
