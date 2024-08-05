from question import Question
question_prompts = [
    "What colors are apples ? \n(a)Red/Green \n(b)Purple \n(c)Orange\n",
    "What colors are Bananas ? \n(a)Red \n(b)Green\n(c)Yellow\n",
    "What colors are strawberries ? \n(a)Yellow \n(b)Red \n(c)Blue\n",
    "What is the capital of France? \n(a)Berlin \n(b)Madrid \n(c)Paris\n",
    "Which planet is known as the Red Planet? \n(a)Earth \n(b)Mars \n(c)Jupiter\n",
    "Who wrote 'Romeo and Juliet'? \n(a)Charles Dickens \n(b)William Shakespeare \n(c)Mark Twain\n",
    "What is the largest mammal in the world? \n(a)Elephant \n(b)Blue Whale \n(c)Giraffe\n",
    "What is the chemical symbol for water? \n(a)H2O \n(b)CO2 \n(c)NaCl\n",
    "Which country is famous for the Eiffel Tower? \n(a)Italy \n(b)France \n(c)Spain\n",
    "Which element does 'O' represent on the periodic table? \n(a)Oxygen \n(b)Gold \n(c)Silver\n",
    "What is the largest planet in our solar system? \n(a)Saturn \n(b)Earth \n(c)Jupiter\n",
    "What fruit is known for keeping doctors away if eaten daily? \n(a)Banana \n(b)Apple \n(c)Mango\n",
    "What food is often associated with cartoons and mice? \n(a)Pizza \n(b)Cheese \n(c)Bread\n",
    "What do pandas eat? \n(a)Bananas \n(b)Bamboo \n(c)Apples\n",
    "What superhero is known for his bat signal? \n(a)Superman \n(b)Spider-Man \n(c)Batman\n",
]

questions = [
    Question(question_prompts[0],"a"),
    Question(question_prompts[1],"c"),
    Question(question_prompts[2],"b"),
    Question(question_prompts[3],"c"),
    Question(question_prompts[4],"b"),
    Question(question_prompts[5],"b"),
    Question(question_prompts[6],"b"),
    Question(question_prompts[7],"a"),
    Question(question_prompts[8],"b"),
    Question(question_prompts[9],"a"),
    Question(question_prompts[10],"c"),
    Question(question_prompts[11],"b"),
    Question(question_prompts[12],"b"),
    Question(question_prompts[13],"b"),
    Question(question_prompts[14],"c"),
]


def function(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print(f"You got {score} out of {len(questions)} questions.")

function(questions)
