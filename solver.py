def expr_reducer(func):
    def reduce_form(numbers):
        degree = len(numbers[0])
        for i in range(degree):
            numbers[0][i] -= numbers[1][i]
            numbers[1][i] = 0.0
        return func(numbers[0], degree)

    return reduce_form


@expr_reducer
def solver(numbers, degree):
    def get_delta():
        return b ** 2 - 4 * a * c

    a, b, c = numbers[::-1]
    delta = get_delta()
    if delta < 0:
        print("Discriminant is strictly negative, there is no solution")
        return None
    elif delta == 0:
        s = -b / 2 * a
        print("Discriminant is equal to zero, the only solution is:")
        print(s)
        return s
    else:
        s1, s2 = ((-b - delta ** 0.5) / (2 * a), (-b + delta ** 0.5) / (2 * a))
        print("Discriminant is strictly positive, the two solutions are:")
        print(f"S1 = {s1: .6f}\nS2 = {s2: .6f}")
        return (s1, s2)
