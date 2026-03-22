# AI Mini Project: Fake News Detection System

# Function to detect whether news is real or fake
def detect_news(text):
    fake_keywords = ["win", "money", "lottery", "offer", "click", "free"]

    for word in fake_keywords:
        if word in text.lower():
            return "FAKE News"
    
    return "REAL News"


# Function to display menu
def show_menu():
    print("\n===== Fake News Detection System =====")
    print("1. Check News")
    print("2. About Project")
    print("3. Exit")


# Function to show about info
def about():
    print("\nThis is a simple AI mini project.")
    print("It detects whether a news message is REAL or FAKE using keywords.")


# Main program
while True:
    show_menu()
    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        user_input = input("\nEnter news message: ")
        result = detect_news(user_input)
        print("Result:", result)

    elif choice == "2":
        about()

    elif choice == "3":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")
