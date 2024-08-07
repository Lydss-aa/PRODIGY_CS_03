import re

def check_password_strength(password):
    # Define the criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'\d', password) is not None
    special_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None
    
    # Check which criteria are met
    criteria_met = [length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria, special_criteria]
    
    # Calculate the strength based on the number of criteria met
    strength = sum(criteria_met)
    
    # Provide feedback
    if strength == 5:
        feedback = "Very Strong"
    elif strength == 4:
        feedback = "Strong"
    elif strength == 3:
        feedback = "Moderate"
    elif strength == 2:
        feedback = "Weak"
    else:
        feedback = "Very Weak"
    
    return feedback, criteria_met

def main():
    password = input("Enter your password: ")
    feedback, criteria_met = check_password_strength(password)
    
    # Display feedback
    print(f"Password Strength: {feedback}")
    print("Criteria Met:")
    print(f"Length >= 8: {'Yes' if criteria_met[0] else 'No'}")
    print(f"Uppercase Letter: {'Yes' if criteria_met[1] else 'No'}")
    print(f"Lowercase Letter: {'Yes' if criteria_met[2] else 'No'}")
    print(f"Digit: {'Yes' if criteria_met[3] else 'No'}")
    print(f"Special Character: {'Yes' if criteria_met[4] else 'No'}")

if __name__ == "__main__":
    main()
