# Roman Numeral to Integer Converter

This project explains how Roman numerals work and how to convert a Roman numeral string into its corresponding integer value.

---

## Roman Numeral Symbols

Roman numerals are represented using **seven symbols**, each with a fixed value:

| Symbol | Value |
|------:|------:|
| I     | 1     |
| V     | 5     |
| X     | 10    |
| L     | 50    |
| C     | 100   |
| D     | 500   |
| M     | 1000  |

---

## Basic Rules

- Roman numerals are usually written **from largest to smallest**, left to right.
- Values are typically **added together**.

### Examples
- `II` = 2  
- `XII` = 12 → `X (10) + II (2)`  
- `XXVII` = 27 → `XX (20) + V (5) + II (2)`

---

## Subtraction Rule

In some cases, a **smaller numeral placed before a larger numeral** indicates subtraction.

### Valid Subtraction Cases

There are **six** valid subtraction combinations:

- **I** before **V** (5) or **X** (10) → `IV = 4`, `IX = 9`
- **X** before **L** (50) or **C** (100) → `XL = 40`, `XC = 90`
- **C** before **D** (500) or **M** (1000) → `CD = 400`, `CM = 900`

❌ `IIII` is invalid  
✅ `IV` is correct

---

## Conversion Task

**Given a Roman numeral string, convert it into an integer.**

---

## Examples

### Example 1
**Input**
```text
s = "III"
