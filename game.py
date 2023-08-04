import random;

def selectRandomQuestions(questions):
    tmp = [];
    while len(tmp) < 5:
        num = random.randint(0, len(questions) - 1);
        if num not in tmp:
            tmp.append(num);
    return tmp;

def createDict(questions, index):
    gquestions = {};
    for el in index:
        q, a = questions[el].split(":");
        gquestions[q] = [i.strip("?") for i in a.split(',')];
    return gquestions;

def countCorrectAnswers(questions):
    count = 0;
    for q, a in questions.items():
        print(q);
        correct = a[0];
        random.shuffle(a);
        for el in a:
            print(el);
        answer = input('Enter your answer: ');
        if answer == correct:
            print('Correct!');
            count += 1;
        else:
            print('Incorrect, the correct answer was', correct);
    return 'You got %d/5' % count;

def main():
    questions = [
        "What is the capital of Armenia:?Yerevan,Pekin,Gyumri,Buenos Aires",
        "What is the capital of France:?Paris,Erevan,Gyumri,London",
        "What is the capital of China:?Pekin,Paris,Vienna,Tbilisi",
        "What is the capital of USA:?Washington,Paris,Pekin,London",
        "What is the capital of Brazil:?Brazil,Washington,Pekin,Yerevan",
        "What is the capital of Georgia:?Tbilisi,Washington,Lisbon,Brazil",
        "What is the capital of Germany:?Berlin,Erevan,Lisbon,Roma",
        "What is the capital of Austria:?Vienna,Erevan,Lisbon,Roma",
        "What is the capital of Italy:?Roma,Washington,Lisbon,Brazil",
        "What is the capital of Spain:?Madrid,Paris,Yerevan,London",
        "What is the capital of the United Kingdom:?London,Erevan,Madrid,Lisbon",
        "What is the capital of Italy:?Roma,Washington,Madrid,Tbilisi",
        "What is the capital of UAE:?Abu Dhabi,Washington,Gyumri,Tbilisi",
        "What is the capital of Portugal:?Lisbon,Washington,Gyumri,Tbilisi",
        "What is the capital of Argentina:?Lisbon,Washington,Gyumri,Buenos Aires"
    ];
    
    tmp = selectRandomQuestions(questions);
    res = createDict(questions, tmp);
    print(countCorrectAnswers(res));

main();

