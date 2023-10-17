#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def answer(question):
    if question.lower()=='q1':
        answer=" We know that the amount of flour needed weighs two times the amount of butter we need"\
            "\n We also know that the mass of butter plus the mass of the flour must be 350kg"\
            "\nThat gives us two equations:\n"\
            "Equation 1: 2*butter=flour\n"\
            "Equation 2: butter+flour=350"\
            "This means that the total mass of the butter and flour is the same as the mass of the butter plus two times the mass of the butter"\
            "\nWhich means that 3 times the mass of the butter is the same as the mass of the pastry wanted:\n"\
            "Equation 3: 3*butter=350\n\n"\
            "Now we have these 3 equations we can start making variables in code and find out how much butter and flour we need"\
            "\n\n pastry=350 #We know the mass of the pastry is 350"\
            "\n butter=350/3 #The mass of the pastry is the same as 3 times the butter needed so the amount of butter needed is the mass of pastry divided by 3"\
            "\n flour=2*butter #The mass of the flour is the same as 2 times the mass of the butter"\
            "\n\nSo now we can print the variables flour and butter to find out how much we need:"\
            "\n print(flour)"\
            "\n print(butter)"
    elif question.lower()=='q2':
        answer="The string 'spam' is the 4th item in the list so it can be accessed with the number 3\n"\
            "print(List[3]) this will print 'spam'"\
            "To make things easier we will make a variable called word:\n"\
            "word= List[3]\n"\
            "print(word) will now print 'spam'\n"\
            "So lets get the letter u from 'spam'\n"\
            "print(word[1]) u is the second item in the string so we can access it with the number 1"\
            "\n\n\n>>>>>>>>>Bonus Answer<<<<<<<<\n\n"\
            "We can actually count backwards to get each item in a list or string\n"\
            "print(List[-1]) using -1 we access the last item in the list, -2 is the second from last and so on. Try it out!\n"\
            "So to print 'spam' we will use print(List[-1])\n"\
            "And to print the 'u' from 'spam' we can use print(List[-1][-3]) or print(List[-1][1])\n"\
            "We can skip creating the variable word and print it directly but I recommend that for now you don't skip the step:\n"\
            "So do:\nword= List[-1]\n"\
            "Letter= Word[1]\n"\
            "print(Letter)"
                
    return answer
