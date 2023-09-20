import requests
import random

# Custom user agent string 
custom_user_agent = "My Library (https://github.com/PrathamVerma999/dad_jokes)"

# Ask the user whether they want a random joke or a topic-based joke
ques = input("Would you like a random joke or would you like to choose a topic? ").strip().lower()

# Function to attempt to convert user input to different data types
def get_type(s):
    try:
        return int(s)
    except ValueError:
        try:
            return str(s)
        except ValueError:
            try:
                return float(s)
            except ValueError:
                try:
                    return bool(s)
                except ValueError:
                    return s

# If the user wants a random joke
if ques == "random":
    url = "https://icanhazdadjoke.com/"
    response = requests.get(
        url,
        headers={"Accept": "application/json"}
    )
    data = response.json()
    print(data["joke"])
    exit()

# If the user wants a topic-based joke
elif ques == "topic":
    url = "https://icanhazdadjoke.com/search"
    topic = input("What topic would you like a joke on? ").strip().lower()
    response = requests.get(
        url,
        headers={"Accept": "application/json"},
        params={"term": topic}
    )
    data = response.json()
    result_list = data["results"]

    # If there are no jokes on the specified topic
    total_jokes = len(result_list)
    if total_jokes == 0:
        print("We don't have jokes on that topic, Sorry!")
        exit()
    
    if total_jokes == 1:
        print(f"The topic {topic} only has one joke:\n")
        joke_dict = result_list[0]
        print(f"• {joke_dict['joke']}")
        exit()

        

    # Ask the user how many jokes they want on the specified topic
    amount = get_type(input(f"The topic {topic} has {total_jokes} jokes. How many jokes would you like? Type 'exit' to stay unhappy.\n"))
    if amount == "exit":
        print("Well, I guess your favorite animal is a bison. Drive safe on the biway!")
        exit()

    # Validate user input for the number of jokes
    while type(amount) != int:
        amount = get_type(input(f"Please enter a number! The topic {topic} has {total_jokes} jokes. How many jokes would you like? Type 'exit' to stay unhappy.\n"))
        if amount == "exit":
            print("You seem like a BMW driver; you gave absolutely no indication of leaving :(")
            exit()

    # Ensure the user-requested number of jokes is within the available range
    while amount > total_jokes:
        amount = get_type(input(f"Oops, that exceeds the amount of jokes we have on {topic}. Please enter a number less than or equal to {total_jokes} or type 'exit' to stay unhappy.\n"))

        if amount == "exit":
            print("Man, is your name Water? I could've sworn you were just right here in my kettle. Well, you will be mist. Okay, Bye-nary now!")
            exit()
        
        # Handle cases where the user doesn't follow instructions
        if type(amount) != int():
            print("YOU REFUSE TO FOLLOW THE GUIDELINES, YOU DESERVE TO STAY DEPRESSED! NO DAD JOKE FOR YOU!")
            exit()

        

    # Shuffle the list of jokes and display the requested number
    shuffled_list = random.sample(result_list, len(result_list))
    final_jokes = shuffled_list[:amount]

    for joke in final_jokes:
        print(f"• {joke['joke']}\n")
