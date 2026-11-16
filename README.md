# Calculator

This is a Python 3 calculator that runs from the terminal. 

## What does it do?
It will perform basic mathematical operations: add, substract, multiply and divide. It will also display the result.

## How to run

- Run `./run.sh` from your terminal. Ensure that the file has permissions to be ran as a program.
- Enter the first operand, then the operator (+, -, *, /), then enter the second operand.
- The program prints out: `Result: [Answer]`.
- To stop the program, press Ctrl+C to trigger a `KeyboardInterrupt`. 

## Prerequisite(s)

Have Python 3 installed on your computer. 

## Testing

To test all the operations, run `./check.sh`. It contains five different tests:

- `test_add()` tests adding, the test `2 + 3` should equal `5`.
- `test_subtract()` tests substracting, the test `5 - 4` should equal `1`.
- `test_multiply()` tests multiplying, the test `6 * 6` should equal `36`.
- `test_divide()` tests dividing, the test `6 / 2` should equal `3`.
- `test_multiplication_by_zero` tests a multiplication by zero, `0 * 0` should equal `0`.

### Exit statuses

Run `echo $?` to show the exit status of the test. The output can be:

`0` - no tests failed
`1` - at least one test failed
`5` - no tests were collected
