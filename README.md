# Compound Interest Calculator

Welcome to the **Compound Interest Calculator**! This is a simple Python program that calculates the compound interest based on user input.

This project was built to practice working with:
- Python's `input()` function for user interaction.
- Loops and conditionals for validating input.
- Basic arithmetic operations to compute compound interest.

## Features

- Prompts the user to input the principle amount, interest rate, and time.
- Ensures that the principle, interest rate, and time are non-negative using loops.
- Calculates and displays the compound interest after validating the input.

## How it works:

1. The program asks for the **principle amount**, and will keep asking until a valid (non-negative) number is entered.
2. It then asks for the **interest rate** and ensures it is non-negative.
3. Finally, it asks for the **time (in years)** and ensures that it is also non-negative.
4. Once valid inputs are provided, the program calculates the **compound interest** using the formula:

   \[
   A = P \left(1 + \frac{r}{100}\right)^t
   \]

   where:
   - \( P \) is the principle amount,
   - \( r \) is the interest rate,
   - \( t \) is the time in years.

5. The result is displayed as the total compound interest over the given time period.

Example Output:
```bash
Enter the principle amount: 1000
Enter the interest rate: 5
Enter the time (in years): 10
The compound interest in 10.0 years, with 5.0% interest is 1628.894626777442
