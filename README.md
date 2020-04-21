# Polynomial equation solver

![Alt Text](https://media2.giphy.com/media/9cpXRPjZuo6pq/giphy.gif?cid=ecf05e474ac62853aba498f4c88ac857ff07c383d3b2efd0&rid=giphy.gif)

## ⚙️ Requirements 

- Python 3.6 (or higher)


## 👨‍💻 Installation 

`git clone https://github.com/jeremie-gauthier/ComputorV1.git`

## ✍️ Usage 

At the root of the project: `python3 -m computor <equation> [options]`

**Examples:**

`python -m computor "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0 + 1 * X^1" -v`

`python -m computor "5 + 4x - 9.3x^2 = 1 + x"`

### Accepted Formats

By default, the only pattern accepted is the following:

- {coef} \* X^{pow} (+|- {coef} \* X^{pow} ...) = {coef} \* X^{pow} (+|- {coef} \* X^{pow} ...)

🏆 But my program also accepts equation written in natural form.

See below the same equation written with the two different syntaxes.

**Examples:**

_Default syntax:_

`5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0 + 1 * X^1`

_Enhanced syntax:_

`5 + 4x - 9.3x^2 = 1 + x`

### Options

Available options:

- ```-v``` Get intermediate stages in the resolution of the equation

### Unit tests

This program comes with its own unit tests module.

Start these tests is as simple as `python -m computor.tests [options]`

**Options:**

The following tests are available:

- format
- result

You can enumerate them in options to only start the desired ones.

⚠️ Please note that the default behaviour is to start them all, so you don't need to specify all if you want all tests to execute.

## 🚀 Bonus part 

- Intermediate stages can be viewed when reducing the form or computing the delta
- An irreducible form of the fraction is given whenever it is possible
- The program includes its own unit tests module
- Equation can be written in natural form _(`5 + 42x = 0` instead of `5 * X^0 + 42 * X^1 = 0 * X^0`)_
- The reduced form of the equation is given in its natural form
- Nice feedbacks in case of syntax error, targeting the error the way compilators do
