def question(prompt, options):
    while True:
        answer = input(prompt).lower().strip()
        if answer in options:
            return answer
        else:
            print("Invalid choice. Please select a valid option.")

def play_game():
    print("Welcome to 'Shadows of Destiny: A Keyblade's Dilemma'!\n")
    print("You find yourself in Radiant Star, a world of light and darkness. Xehanort of Organization XIII offers you power and knowledge, but a choice lies ahead.\n")

    play = question("Would you like to play? (yes/no): ", ["yes", "no"])
    if play == "no":
        return

    choice1 = question("\nYou awaken in Radiant Star. Join Organization XIII or stick with your friends? (join/friends): ", ["join", "friends"])
    
    if choice1 == "join":
        choice2 = question("\nYou have joined the organization. But doubts emerge. Investigate or ignore? (investigate/ignore): ", ["investigate", "ignore"])
        
        if choice2 == "investigate":
            choice3 = question("\nYou eavesdrop on high-ranking members and hear them talking about 'collecting hearts'. You hesitate and think to yourself-go deeper or stop? (deeper/stop): ", ["deeper", "stop"])
            
        elif choice2 == "ignore":
            choice3 = question("\nYou suppress your doubts and continue to believe what you're doing is right. Will you go for a drink or go keyblade training? (drink/training): ", ["drink", "training"])

    elif choice1 == "friends":
        choice2 = question("\nYou remain loyal to your friends. Will you play video games or go train? (games/train): ", ["games", "train"])

        if choice2 == "games":
            choice3 = question("\nThe sun is setting and you've been playing Super Smash Bros for hours. Do you go home or go for a night stroll before heading home? (home/stroll): ", ["home", "stroll"])

        elif choice2 == "train":
            choice3 = question("\nYou go do some battle training. You're worn out and can barely walk. Do you call a taxi or bike home? (taxi/bike): ", ["taxi", "bike"])

    ending_choice = question("\nYour journey in Radiant Star comes to an end. Content with your path or wish to explore different outcomes? (content/explore): ", ["content", "explore"])

    if ending_choice == "content":
        print("\nYour time has come to an end.")
    elif ending_choice == "explore":
        print("\nYou decide to revisit Radiant Star, exploring different choices and writing your own destiny.")
play_game()