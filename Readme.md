# Augmented Assignment (or compound assignment)

An augmented assignment is generally used to replace a statement where an operator takes a variable as one of its arguments and then assigns the result back to the same variable.

A simple example is x += 1 which is expanded to x = x + (1). Similar constructions are often available for various binary operators.

```python
augmented_assignment_stmt: target augop expression_list
augop:           "+=" | "-=" | "*=" | "/=" | "%=" | "**="
               | ">>=" | "<<=" | "&=" | "^=" | "|="
target:          identifier | "(" target_list ")" | "[" target_list "]"
               | attributeref | subscription | slicing
```
An augmented assignment expression like x += 1 can be rewritten as x = x + 1 to achieve a similar, but not exactly equal effect. 
In the augmented version, x is only evaluated once. Also, when possible, the actual operation is performed in-place, 
meaning that rather than creating a new object and assigning that to the target, the old object is modified instead.
