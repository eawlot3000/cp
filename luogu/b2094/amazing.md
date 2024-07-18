The issue you are encountering is due to trying to print the variable `a` outside the loop. The variable `a` only exists within the scope of the loop, so it will not be available outside of it. To fix this, you need to print the list `a` inside the loop. Here is the corrected code using only the `del` statement:

```python
n = int(input())
for i in range(n):
  a = list(map(int, input().split()))
  del a[a.index(max(a))]  # Delete the item at the index of the maximum value
  print(a)  # Print the modified list inside the loop
```

### Explanation:
1. `del a[a.index(max(a))]`: This line finds the index of the maximum value in the list `a` and deletes the element at that index.
2. `print(a)`: This line prints the modified list inside the loop, ensuring that you see the result after each iteration.

Now, the code will correctly remove the maximum value from the list `a` for each iteration and print the modified list immediately after.


--------





The reason you encounter an error when trying to print `a` outside the loop is because the variable `a` only exists within the scope of the loop iteration. Each iteration of the loop creates a new `a`, which is not accessible outside the loop. To understand this better, let's review the behavior step by step.

Here is your original code with an explanation:

```python
n = int(input())  # Read the number of iterations
for i in range(n):
  a = list(map(int, input().split()))  # Read the input list for each iteration
  del a[a.index(max(a))]  # Delete the maximum value in the list
  print(a)  # Print the modified list inside the loop
```

### Explanation:
1. `n = int(input())`: This reads the number of iterations.
2. `for i in range(n):`: This starts a loop that will run `n` times.
3. `a = list(map(int, input().split()))`: This reads a list of integers from input for each iteration.
4. `del a[a.index(max(a))]`: This finds and deletes the maximum value in the list `a`.
5. `print(a)`: This prints the modified list `a` inside the loop.

If you want to collect all the modified lists and print them at the end, you can store them in another list. Here is how you can do that:

```python
n = int(input())
results = []  # Initialize an empty list to store results

for i in range(n):
  a = list(map(int, input().split()))  # Read the input list for each iteration
  del a[a.index(max(a))]  # Delete the maximum value in the list
  results.append(a)  # Store the modified list in results

for result in results:
  print(result)  # Print each modified list at the end
```

### Explanation:
1. `results = []`: This initializes an empty list to store the modified lists.
2. Inside the loop, the modified list `a` is appended to the `results` list.
3. After the loop, each modified list stored in `results` is printed.

This way, you can print all the modified lists at the end of the program.




--------







To print the list `a` outside the loop and ensure that it contains the final modified state of the list from the last iteration, you can initialize `a` before the loop and only print it after the loop completes. Here's how you can do it:

```python
n = int(input())
a = None  # Initialize a variable to store the final list

for i in range(n):
  a = list(map(int, input().split()))  # Read the input list for each iteration
  del a[a.index(max(a))]  # Delete the maximum value in the list

print(a)  # Print the modified list after the loop
```

### Explanation:
1. `a = None`: Initialize `a` outside the loop to ensure it exists after the loop completes.
2. Inside the loop, `a` is assigned a new list for each iteration, and the maximum value is deleted.
3. After the loop, `print(a)` prints the final modified list from the last iteration.

This way, the code will print the modified list `a` after all iterations are completed.
