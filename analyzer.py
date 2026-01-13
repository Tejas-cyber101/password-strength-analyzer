import re

def analyze_password(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters")

    # Uppercase check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters")

    # Lowercase check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters")

    # Number check
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add numbers")

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add special characters")

    return score, feedback

def strength_label(score):
    if score <= 2:
        return "Weak"
    elif score == 3 or score == 4:
        return "Medium"
    else:
        return "Strong"

if __name__ == "__main__":
    password = input("Enter a password to analyze: ")

    score, feedback = analyze_password(password)
    strength = strength_label(score)

    print(f"\nPassword Strength: {strength}")

    if feedback:
        print("Suggestions to improve:")
        for item in feedback:
            print(f"- {item}")
    else:
        print("Great! Your password is strong.")
