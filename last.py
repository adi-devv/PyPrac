import math


def get_intersection(x1, y1, x2, y2, x3, y3, x4, y4):
    denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if denom == 0:
        return None
    x = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / denom
    y = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / denom
    return (x, y)


def calculate_voltage(wires):
    intersections = {}
    total_voltage = 0
    for i in range(len(wires)):
        x1, y1, x2, y2 = wires[i]
        for j in range(i + 1, len(wires)):
            x3, y3, x4, y4 = wires[j]
            intersection = get_intersection(x1, y1, x2, y2, x3, y3, x4, y4)
            if intersection:
                x, y = intersection
                min_cells = min(abs(x1 - x), abs(x2 - x), abs(y1 - y), abs(y2 - y))
                voltage = min_cells * (i + 1)
                if (x, y) not in intersections:
                    intersections[(x, y)] = voltage
                else:
                    intersections[(x, y)] += voltage
                total_voltage += voltage
    return intersections, total_voltage


def main():
    N = int(input())
    wires = []
    for _ in range(N):
        wires.append(list(map(int, input().split())))

    animals = {}
    animal_line = input().split()
    for animal in animal_line:
        name, threshold = animal.split(':')
        animals[name] = int(threshold)

    touched_animal = input().strip()

    intersections, total_voltage = calculate_voltage(wires)
    animal_threshold = animals[touched_animal]

    if total_voltage >= animal_threshold:
        print("Yes")
    else:
        print("No")

    num_dead = sum(1 for threshold in animals.values() if total_voltage >= threshold)
    print(f"{num_dead / len(animals):.2f}")


if __name__ == "__main__":
    main()
