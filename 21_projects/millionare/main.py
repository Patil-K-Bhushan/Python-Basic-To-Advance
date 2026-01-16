import random

questions = [
    {
        "id": 1,
        "question": "What is the capital of India?",
        "options": ["Mumbai", "New Delhi", "Chennai", "Kolkata"],
        "answer": "New Delhi"
    },
    {
        "id": 2,
        "question": "Which planet is known as the Red Planet?",
        "options": ["Venus", "Mars", "Jupiter", "Saturn"],
        "answer": "Mars"
    },
    {
        "id": 3,
        "question": "How many days are there in a leap year?",
        "options": ["365", "366", "364", "360"],
        "answer": "366"
    },
    {
        "id": 4,
        "question": "Which is the largest animal in the world?",
        "options": ["Elephant", "Giraffe", "Blue Whale", "Shark"],
        "answer": "Blue Whale"
    },
    {
        "id": 5,
        "question": "Who wrote the national anthem of India?",
        "options": ["Bankim Chandra Chatterjee", "Rabindranath Tagore", "Sarojini Naidu", "Subhash Chandra Bose"],
        "answer": "Rabindranath Tagore"
    },
    {
        "id": 6,
        "question": "What is the boiling point of water?",
        "options": ["90°C", "100°C", "80°C", "120°C"],
        "answer": "100°C"
    },
    {
        "id": 7,
        "question": "Which organ pumps blood in the human body?",
        "options": ["Brain", "Lungs", "Heart", "Liver"],
        "answer": "Heart"
    },
    {
        "id": 8,
        "question": "How many continents are there in the world?",
        "options": ["5", "6", "7", "8"],
        "answer": "7"
    },
    {
        "id": 9,
        "question": "Which is the national bird of India?",
        "options": ["Eagle", "Sparrow", "Peacock", "Crow"],
        "answer": "Peacock"
    },
    {
        "id": 10,
        "question": "Which gas do plants absorb from the atmosphere?",
        "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"],
        "answer": "Carbon Dioxide"
    },
    {
        "id": 11,
        "question": "Who is known as the Father of the Indian Constitution?",
        "options": ["Mahatma Gandhi", "Jawaharlal Nehru", "B. R. Ambedkar", "Sardar Patel"],
        "answer": "B. R. Ambedkar"
    },
    {
        "id": 12,
        "question": "Which is the smallest prime number?",
        "options": ["0", "1", "2", "3"],
        "answer": "2"
    },
    {
        "id": 13,
        "question": "Which country gifted the Statue of Liberty to the USA?",
        "options": ["Germany", "France", "Canada", "Italy"],
        "answer": "France"
    },
    {
        "id": 14,
        "question": "What does CPU stand for?",
        "options": ["Central Program Unit", "Central Processing Unit", "Control Processing Unit", "Computer Power Unit"],
        "answer": "Central Processing Unit"
    },
    {
        "id": 15,
        "question": "Which blood group is known as the universal donor?",
        "options": ["A", "B", "AB", "O negative"],
        "answer": "O negative"
    },
    {
        "id": 16,
        "question": "Which is the longest river in the world?",
        "options": ["Amazon", "Ganga", "Nile", "Yangtze"],
        "answer": "Nile"
    },
    {
        "id": 17,
        "question": "Which vitamin is produced when skin is exposed to sunlight?",
        "options": ["Vitamin A", "Vitamin B", "Vitamin C", "Vitamin D"],
        "answer": "Vitamin D"
    },
    {
        "id": 18,
        "question": "Who invented the telephone?",
        "options": ["Thomas Edison", "Nikola Tesla", "Alexander Graham Bell", "Albert Einstein"],
        "answer": "Alexander Graham Bell"
    },
    {
        "id": 19,
        "question": "Which is the largest desert in the world?",
        "options": ["Sahara", "Thar", "Kalahari", "Gobi"],
        "answer": "Sahara"
    },
    {
        "id": 20,
        "question": "What is the chemical symbol of gold?",
        "options": ["Ag", "Go", "Au", "Gd"],
        "answer": "Au"
    },
    {
        "id": 21,
        "question": "Which is the hardest natural substance?",
        "options": ["Iron", "Diamond", "Platinum", "Quartz"],
        "answer": "Diamond"
    },
    {
        "id": 22,
        "question": "Who was the first woman Prime Minister of India?",
        "options": ["Pratibha Patil", "Sonia Gandhi", "Indira Gandhi", "Sushma Swaraj"],
        "answer": "Indira Gandhi"
    },
    {
        "id": 23,
        "question": "What is the SI unit of electric current?",
        "options": ["Volt", "Ohm", "Ampere", "Watt"],
        "answer": "Ampere"
    },
    {
        "id": 24,
        "question": "Which part of the brain controls balance?",
        "options": ["Cerebrum", "Cerebellum", "Medulla", "Hypothalamus"],
        "answer": "Cerebellum"
    },
    {
        "id": 25,
        "question": "Which Indian satellite was the first to reach Mars?",
        "options": ["Aryabhata", "Chandrayaan-1", "Mangalyaan", "INSAT-1"],
        "answer": "Mangalyaan"
    },
    {
        "id": 26,
        "question": "Who discovered gravity?",
        "options": ["Galileo Galilei", "Albert Einstein", "Isaac Newton", "Johannes Kepler"],
        "answer": "Isaac Newton"
    },
    {
        "id": 27,
        "question": "Which element has the atomic number 1?",
        "options": ["Helium", "Hydrogen", "Oxygen", "Nitrogen"],
        "answer": "Hydrogen"
    },
    {
        "id": 28,
        "question": "In which year did India get independence?",
        "options": ["1945", "1946", "1947", "1950"],
        "answer": "1947"
    },
    {
        "id": 29,
        "question": "What is the full form of HTTP?",
        "options": ["Hyper Text Transfer Protocol", "High Text Transfer Program", "Hyper Transfer Text Process", "Home Tool Transfer Protocol"],
        "answer": "Hyper Text Transfer Protocol"
    },
    {
        "id": 30,
        "question": "Which instrument is used to measure atmospheric pressure?",
        "options": ["Thermometer", "Hygrometer", "Barometer", "Anemometer"],
        "answer": "Barometer"
    }
]

money_levels = [1000, 2000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 7500000, 10000000]

game_questions = random.sample(questions, 15)

current_money = 0

print("\n Welcome to \"Who Wants to be a Millionare\"\n")

for i, q in enumerate(game_questions):
    print(f"\nQuestion {i+1} for ₹{money_levels[i]}")
    print(q["question"])

    for idx, opt in enumerate(q["options"]):
        print(f"{idx+1}. {opt}")

    user_choice = input("Enter your answer (1-4): ")

    if not user_choice.isdigit() or int(user_choice) not in [1,2,3,4]:
        print("Invalid input. Game Over.")
        break

    selected_option = q["options"][int(user_choice) - 1]

    if selected_option == q["answer"]:
        current_money = money_levels[i]
        print("Correct Answer!")
        print(f"You won ₹{current_money}")
    else:
        print("Wrong Answer!")
        print(f"Correct answer was: {q['answer']}")
        print(f"Game Over! You take home ₹{current_money}")
        break

else:
    print("\nCONGRATULATIONS! You won the maximum amount!")
    print(f"Total Winnings: ₹{current_money}")

print("\nThanks for playing!")
