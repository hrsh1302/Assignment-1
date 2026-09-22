# Program Name: Assignment1.py
# Course: IT3883/Section 85540
# Student Name: Harash Banga
# Assignment Number: Lab1
# Due Date: 09/07/2025
# Purpose:  Write a Python program that implements a text-based menu.
#           The menu should present the user with the following 4 choices: Append data to the input buffer;
#           Clear the input buffer; Display the input buffer; Exit the program. The user gets to choose the
#           input using numbers 1 to 4.

# List Specific resources used to complete the assignment.

# Menu function called at every iteration
def menu ():
    print("\n=======================================")
    print("Choose a menu option:")
    print("\t[1] Append text onto buffer")
    print("\t[2] Clear the input buffer")
    print("\t[3] Display the input buffer")
    print("\t[4] Exit the program")
    print("=======================================")

# Main
def main():
    txt_buffer = ""

    while True:
        menu()
        menu_option = input("\nEnter your choice (1-4): ").strip()

        # Append mode
        if menu_option == "1":
            new_buffer = input("\nEnter the text to append: ")
            txt_buffer += new_buffer
            print("\n\tEntry saved to the buffer!" )

        # Clearing mode
        elif menu_option == "2":
            txt_buffer = ""
            print("\n\tInput buffer cleared!")

        # Display buffer. If empty, it displays a sentence.
        elif menu_option == "3":
            if txt_buffer == "":
                print("\n\tInput buffer is blank")
            else:
                print("\n\tThe input buffer is: '" + txt_buffer + "' .")

        # Breaks the loop and ends program
        elif menu_option == "4":
            print("\n\tExiting program. Thank you!")
            break

        else :
            print(" Invalid option. Please try again by entering an option from [1] - [4].")

if __name__ == '__main__':
    main()