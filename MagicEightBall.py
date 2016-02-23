import random
import time

pg_answers = ["It is certain",
              "It is decidedly so",
              "Without a doubt",
              "Yes, definitely",
              "You may rely on it",
              "As I see it, yes",
              "Most likely",
              "Outlook good",
              "Yes",
              "Signs point to yes",
              "Reply hazy try again",
              "Ask again later",
              "Better not tell you now",
              "Cannot predict now",
              "Concentrate and ask again",
              "Don't count on it",
              "My reply is no",
              "My sources say no",
              "Outlook not so good",
              "Very doubtful"
              ]

sar_answers = ["As If",
               "Ask Me If I Care",
               "Dumb Question Ask Another",
               "Forget About It",
               "Get A Clue",
               "In Your Dreams",
               "Not",
               "Not A Chance",
               "Obviously",
               "Oh Please",
               "Sure",
               "That's Ridiculous",
               "Well Maybe",
               "What Do You Think?",
               "Whatever",
               "Who Cares?",
               "Yeah And I'm The Pope",
               "Yeah Right",
               "You Wish",
               "You've Got To Be Kidding"
               ]


def magic_eight_ball(rating):
    rating = rating
    if rating != 1:
        return(random.choice(sar_answers))
    else:
        return(random.choice(pg_answers))


def main():
    my_name = input("Hello! Whats your name?\n")
    rating = int(input("Select mode:\n1: Normal\n2: Sarcastic\n(1/2): "))
    question = input("What is your question?\n(Yes or no questions only please)")
    time.sleep(2)
    print("Let me think...")
    time.sleep(3)
    answer = magic_eight_ball(rating)
    print(answer)
    with open('answers.txt', 'a') as f:
        f.write("{} - {} - {}\n".format(my_name, question, answer))

if __name__ == '__main__':
    main()