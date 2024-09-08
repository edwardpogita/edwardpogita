def relationship_choice():
    print("You have an important decision to make:")
    print("Do you want to break up or stay together?")
    print("a) Break up")
    print("b) Stay together")
    
    choice = input("Your choice (a/b): ").lower()
    
    if choice == "a":
        print( "🖕🖕🖕🖕🖕🖕🖕🖕🖕🖕🖕")
        follow_up = input("Follow-up question: Bakit mo'ko iniignore?, nakakasakit kana. Your answer: ")
        print(f"Your response: {follow_up}")

# Run the relationship_choice function
