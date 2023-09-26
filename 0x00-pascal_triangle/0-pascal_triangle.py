def pascal_triangle(n):
    if n <= 0:
        return []

    # Initialize the triangle with the first row containing 1.
    triangle = [[1]]

    # Generate the subsequent rows of the triangle.
    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]  # The first element of each row is always 1.

        # Calculate the middle elements of the row.
        for j in range(1, i):
            new_element = prev_row[j - 1] + prev_row[j]
            new_row.append(new_element)

        new_row.append(1)  # The last element of each row is always 1.

        triangle.append(new_row)

    return triangle
