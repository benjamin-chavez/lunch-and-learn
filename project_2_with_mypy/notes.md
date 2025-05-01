17  Notes.md
 16
 15 Dynamic vs Static Typing:
 14  - What is static typing, through the lens of dynamic typing
 13  - Software is about tradeoffs, what are the tradeoffs?
 12     - Speed, or at lease initial speed
 11     - ... no other cons?
 10
  9     Pros:
  8     - As the codebase grows, it is easier for the team to maintain quick feature development and stay
  7
  6 ## Example 1a:
  5     - What is wrong with this code?
  4
  3 ```py
  2
  1 def my_func(loan_id):
18      return loan_id
  1
  2 # output: my_func(loan_id): 42424242
  3
  4
  5 def my_func2(loan_id):
  6     return loan_id + 5
  7
  8
  9 if __name__ == "__main__":
 10     loan_id = "42424242"
 11
 12     my_func(loan_id)
 13     my_func2(loan_id)
 14
 15 ```
 16     - We do not have enough information about my_func()
 17     - my_func2(loan_id) attempts to add the number/integer 5 to a string. THe error is only caught at runtime:
Notes.md [+]                                                                                                        18,19          Top
-- INSERT --
