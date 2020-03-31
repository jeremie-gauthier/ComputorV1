def expr_reducer(func):
    def reduce_form(coefs):
        reduced = map(sum, zip(*coefs))
        return func(reduced)

    return reduce_form


def verbose_solution(func):
    def messenger(*args, **kwargs):
        s = func(*args, **kwargs)()
        if s["delta"] < 0:
            message = "Discriminant is strictly negative, there is no solution"
        elif s["delta"] == 0:
            message = f"Discriminant is equal to zero, the only solution is:\n\
                \r{s['result']}"

        else:
            message = f"Discriminant is strictly positive, the two solutions are:\n\
                    \rS1 = {s['result'][0]: .6f}\nS2 = {s['result'][1]: .6f}"
        return {**s, "message": message}

    return messenger


@expr_reducer
@verbose_solution
def solver(coefs):
    def get_delta(a, b, c):
        return b ** 2 - 4 * a * c

    def second_degree():
        c, b, a = coefs
        delta = get_delta(a, b, c)
        if delta < 0:
            result = None
        elif delta == 0:
            result = -b / 2 * a
        else:
            s1 = (-b - delta ** 0.5) / (2 * a)
            s2 = (-b + delta ** 0.5) / (2 * a)
            result = (s1, s2)
        return {"delta": delta, "result": result}

    return second_degree
