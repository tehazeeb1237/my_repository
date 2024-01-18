prize_1 = 2000
prize_2 = 4000
prize_3 = 6000
prize_4 = 8000

q1 = "1. What is the maximum length of a Python identifier?"
q2 = "2. What will be the output of the following code snippet? print(2**3 + (5 + 6)**(1 + 1))"
q3 = "3. How is a code block indicated in Python?"
q4 = "4. Which of the following concepts is not a part of Python?"

list_que = [q1, q2, q3, q4]

print(list_que[0])

list_ans1 = ["32", "16", "128", "no fixed length"]
for i, ans in enumerate(list_ans1):
    print(i + 1, ".", ans)

ans1 = list_ans1.index("no fixed length")
sel_ans1 = int(input("Enter the correct option: "))

if ans1 == sel_ans1 - 1:
    print("BINGO!!....correct answer \nYou have won prize money of", prize_1, "\nCONGRATULATIONS....")
    print(list_que[1])
    list_ans2 = [129, 32, 9, 121]
    for i, ans in enumerate(list_ans2):
        print(i + 1, ".", ans)
    ans2 = list_ans2.index(129)
    sel_ans2 = int(input("Enter the correct option: "))

    if ans2 == sel_ans2 - 1:
        print("BINGO!!....correct answer \nYou have won prize money of", prize_2, "\nCONGRATULATIONS....")
        total = prize_1 + prize_2
        print(list_que[2])
        list_ans3 = ['brackets', 'indentation', 'key', 'none']
        for i, ans in enumerate(list_ans3):
            print(i + 1, ".", ans)
        ans3 = list_ans3.index('indentation')
        sel_ans3 = int(input("Enter the correct option: "))

        if ans3 == sel_ans3 - 1:
            print("BINGO!!....correct answer \nYou have won prize money of", prize_3, "\nCONGRATULATIONS....")
            total += prize_3
            print(list_que[3])
            list_ans4 = ['pointers', 'loops', 'dynamic typing', 'all of the above']
            for i, ans in enumerate(list_ans4):
                print(i + 1, ".", ans)
            ans4 = list_ans4.index('pointers')
            sel_ans4 = int(input("Enter the correct option: "))

            if ans4 == sel_ans4 - 1:
                print("BINGO!!....correct answer \nYou have won prize money of", prize_4, "\nCONGRATULATIONS....")
                total += prize_4
            else:
                print("SORRY!!..it's a wrong answer \nYou have won", total, "\nBETTER LUCK NEXT TIME")
        else:
            print("SORRY!!..it's a wrong answer \nYou have won", total, "\nBETTER LUCK NEXT TIME")
    else:
        print("SORRY!!..it's a wrong answer \nYou have won", prize_1, "\nBETTER LUCK NEXT TIME")
else:
    print("SORRY!!..it's a wrong answere \nBETTER LUCK NEXT TIME")
