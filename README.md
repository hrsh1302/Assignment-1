# Assignment 1
## Purpose

This program implements a text-based menu system in Python. The user is presented with four options 
to manage a simple text input buffer:

1. Append text onto the buffer
2. Clear the input buffer
3. Display the input buffer
4. Exit the program

The user selects an option by entering a number from 1 to 4.

## How It Works

- A `menu()` function prints the list of options at the start of every loop iteration.


- The `main()` function holds the program's core loop:
  - **Option 1 (Append):** Prompts the user for text and appends it to `txt_buffer`.
  - **Option 2 (Clear):** Resets `txt_buffer` to an empty string.
  - **Option 3 (Display):** Prints the current buffer contents, or a message if it's blank.
  - **Option 4 (Exit):** Breaks the loop and ends the program.
  - **Any other input:** Triggers an error message and re-displays the menu.

### Invalid Input Handling & Blank Buffer Display
Demonstrates the menu rejecting a non-numeric entry ("Hello"), then showing the blank-buffer message when option 3 is selected before anything has been appended.

![Invalid input and blank buffer](img(1).png)

### Appending and Displaying Text
Shows option 1 being used to append "World" to the buffer, followed by option 3 confirming the buffer now contains `' World'`.

![Append and display](img(2).png)

### Clearing the Buffer and Exiting
Shows option 2 clearing the buffer, followed by option 4 exiting the program cleanly (exit code 0).

![Clear and exit](img(3).png)
