from flask import Flask
import random
app = Flask(__name__)

@app.route("/")
def home():
    print("Let's start the game!! Gues the number!!!")
    difference=0
    correct_no=random.randrange(0,100)
    while True:
        text_type=""
        print(correct_no)
        guess_no=int(input("Please choose the number between 0 to 100\n"))
        if correct_no==guess_no:
            print("Congralutions!!, you guessed the correct no")
            text_type="Congralutions!!, you guessed the correct no"
            break
        else:
            if guess_no>correct_no:
                difference=guess_no-correct_no
            else:
                difference=correct_no-guess_no
            if difference<=10:
                print("Too close\n")
            else:
                print("Please try again!! It is incorrect\n")
    return text_type

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
	
