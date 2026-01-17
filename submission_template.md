# AI Code Review Assignment (Python)

## Candidate
- Name: Deniz Yılmaz
- Approximate time spent: 80 minutes

---

# Task 1 — Average Order Value

## 1) Code Review Findings
### Critical bugs
- The denominator is currently the number of both cancelled and non-cancelled orders. We should take only the non-cancelled ones into account.

### Edge cases & risks
- If the "count" variable is 0, we get a division by 0 error.

### Code quality / design issues
- 

## 2) Proposed Fixes / Improvements
### Summary of changes
- We only count the non-cancelled orders, by incrementing count variable in the main loop.
- If the count is 0 (i.e. there is no non-cancelled orders) in the return statement, we return 0.0.

### Corrected code
See `correct_task1.py`

> Note: The original AI-generated code is preserved in `task1.py`.

 ### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
- Empty input list (to check if the divison works fine).
- List with all orders are cancelled (to check if the return value is correct).


## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of orders. It correctly excludes cancelled orders from the calculation.

### Issues in original explanation
- It is not clearly stated that we should divide the total amount of orders by the number of non-cancelled orders.
- It is not clearly stated what the function will return if the number of values is 0.

### Rewritten explanation
- This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of non-cancelled orders. It correctly excludes cancelled orders from the calculation. It returns 0.0 if there does not exist any non-cancelled orders.

## 4) Final Judgment
- Decision: Request Changes
- Justification: The calculation is incorrect and division by zero is not handled properly.
- Confidence & unknowns: Provided that the inputs are aligned with the assumptions, the code will work correctly.

---

# Task 2 — Count Valid Emails

## 1) Code Review Findings
### Critical bugs
- The code only checks if there is "@" in the string literal. Extra checks for the local and the domain part must be done.

### Edge cases & risks
- Although the new code is implemented based on the general email format, some companies violate this format and use their own systems.
- If the count is 0 (i.e. there is no valid emails) in the return statement, we return 0.0.

### Code quality / design issues
-

## 2) Proposed Fixes / Improvements
### Summary of changes
- In my code, I checked every bulletpoint one after another for all addresses.
- If the number of "@" symbols in the address is one.
- Splits the address into two parts: local and domain.
- If the length of either of the parts is 0.
- I added three regular expressions, two of them handling the local part and one of them handling the domain part.
- If the local parts match any of the two patterns.
- I split the domain into labels, delimeted by '.'.
- If there are less than 2 labels.
- If each label matches pattern.

### Corrected code
See `correct_task2.py`

> Note: The original AI-generated code is preserved in `task2.py`. 


### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
- Empty input list (to check if the divison works fine).
- Input list that includes invalid emails based on the general rules.
- Input list of strings without "@".
- Input list of strings that include characters that are not alpha-numerical.

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation
- There are no issues in the explanation; however, the original code does not do what the explanation says.

### Rewritten explanation
- 

## 4) Final Judgment
- Decision: Reject
- Justification: The implementation only handes one case out of thousands.
- Confidence & unknowns: After the corrections, the implementaion handles a variety of cases properly.

---

# Task 3 — Aggregate Valid Measurements

## 1) Code Review Findings
### Critical bugs
- The code assumes that the elements of the input list of a numerical type. If not, conversion to float will raise error.
- The code divides the sum of the valid measurements by the number of all elements, it should exclude the invalid ones.

### Edge cases & risks
- If the count is 0 (i.e. all values are None) in the return statement, we return 0.0.

### Code quality / design issues
- 

## 2) Proposed Fixes / Improvements
### Summary of changes
- I added a try except block to handle the case where an element is not of a numerical type.
- If the count is 0 (i.e. all values are None) in the return statement, we return 0.0.

### Corrected code
See `correct_task3.py`

> Note: The original AI-generated code is preserved in `task3.py`.

### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?


## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average

### Issues in original explanation
- It is not clearly stated what the function will return if the number of valid measurements is 0.
- It is not clearly stated that input elements are of numerical types.

### Rewritten explanation
- This function calculates the average of valid measurements (which are of numerical types) by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average. It returns 0.0 if all values are missing or there are no values.

## 4) Final Judgment
- Decision: Request Changes
- Justification: Wrong averaging, possibility to division by zero, and risky type-casting.
- Confidence & unknowns: Works fine after the corrections.
