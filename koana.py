def reflect_point(px, py, x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    a = dy
    b = -dx
    c = dx * y1 - dy * x1

    d = (a * px + b * py + c) / (a ** 2 + b ** 2) ** 0.5

    reflected_x = px - 2 * d * a / (a ** 2 + b ** 2) ** 0.5
    reflected_y = py - 2 * d * b / (a ** 2 + b ** 2) ** 0.5

    return reflected_x, reflected_y


def folded_corners(area, folding_line):
    import math

    side_length = math.sqrt(area)

    corners = [
        (0, 0),
        (0, side_length),
        (side_length, side_length),
        (side_length, 0)
    ]

    x1, y1, x2, y2 = folding_line

    new_corners = []

    for corner in corners:
        cx, cy = corner

        if cx < min(x1, x2) or cx > max(x1, x2) or cy < min(y1, y2) or cy > max(y1, y2):
            new_corners.append(corner)
        else:
            reflected_x, reflected_y = reflect_point(cx, cy, x1, y1, x2, y2)
            new_corners.append((reflected_x, reflected_y))

    all_corners = set(new_corners + corners)

    sorted_corners = sorted(all_corners)

    return sorted_corners


area = int(input())
folding_line = list(map(int, input().strip().split()))

result = folded_corners(area, folding_line)
for x, y in result:
    print(f"{x:.2f} {y:.2f}")