print("Welcome to the Bitcoin Quiz")

playing = input("Start Game? ")

if playing.lower() != "yes":
    quit()

print("Okay! Lets Go :) ")
points = 0

answer = input("Who created Bitcoin? ")
if answer.lower() == "satoshi nakamoto":
    print("Good Job!")
    points += 1
else:
    print("Incorrect! ")

answer = input("When was bitcoin created? ")
if answer.lower() == "2009":
    print("Good Job!")
    points += 1
else:
    print("Incorrect! ")

answer = input("The first block on a blockchain is called? ")
if answer.lower() == "genesis block":
    print("Good Job!")
    points += 1
else:
    print("Incorrect! ")

answer = input("Which food is famous for being bought for 10000 Bitcoins? ")
if answer.lower() == "pizza":
    print("Good Job!")
    points += 1
else:
    print("Incorrect! ")

answer = input("Who received the first Bitcoin Transaction from the Bitcoin creator? ")
if answer.lower() == "hal finney":
    print("Good Job!")
    points += 1
else:
    print("Incorrect! ")

answer = input("How many minutes approximately does it take to mine a block on the bitcoin blockchain? ")
if answer.lower() == "10":
    print("Good Job!")
    points += 1
else:
    print("Incorrect! ")

answer = input("What is the numeric total number of Bitcoins that can ever exist? ")
if answer.lower() == "21 million":
    print("Good Job!")
    points += 1
else:
    print("Incorrect! ")

answer = input("Is it possible to edit/reverse a transaction on the Bitcoin Blockchain? ")
if answer.lower() == "no":
    print("Good Job!")
    points += 1
else:
    print("Incorrect! ")

answer = input("How many Sats make 1 Bitcoin ")
if answer.lower() == "100 million":
    print("Good Job!")
    points += 1
else:
    print("Incorrect! ")
    
print(f"You scored {points} / 10")