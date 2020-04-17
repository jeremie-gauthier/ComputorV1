# Polynomial equation solver

## Installation

```git clone https://github.com/jeremie-gauthier/ComputorV1.git```

## Usage

At the root of the project: ```python -m computor <equation> [options]```

### Accepted Formats:

By default, the only pattern accepted is the following:

- {coef} \* X^{pow} (+|- {coef} \* X^{pow} ...) = {coef} \* X^{pow} (+|- {coef} \* X^{pow} ...)

But my program accepts equation written in natural form.

See below the same equation written with the two different syntaxes.

**e.g.:**

_Default syntax:_

- ```5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0 + 1 * X^1```

_Enhanced syntax:_

- ```5 + 4x - 9.3x^2 = 1 + x```

## Bonus part

- Intermediate stages can be viewed when reducing the form or computing the delta
- An irreducible form of the fraction is given whenever it is possible
- The program includes its own unit tests module
- Equation can be written in natural form (e.g.: "5 + 42x = 0" instead of "5 \* X^0 + 42 \* X^1 = 0 \* X^0")
- The reduced form of the equation is given in its natural form
