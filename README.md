# Polynomial equation solver

## Usage

````
git clone https://github.com/jeremie-gauthier/ComputorV1.git
cd ComputorV1
python -m computor <equation> <options?>```

**Format accepted:**

{coef} \* X^{pow} (+|- {coef} \* X^{pow} ...) = {coef} \* X^{pow} (+|- {coef} \* X^{pow} ...)

**e.g.:**

5 \* X^0 + 4 \* X^1 - 9.3 \* X^2 = 1 \* X^0


## Bonus part

- Intermediate stages can be viewed when reducing the form or computing the delta
- An irreducible form of the fraction is given whenever it is possible
- The program includes its own unit tests module
- Equation can be written in natural form (e.g.: "5 + 42x = 0" instead of "5 \* X^0 + 42 \* X^1 = 0 \* X^0")
- The reduced form of the equation is given in its natural form
````
