from time import *

import random as r


#paragraph_test= given paragraph for test
def mistake(paragraph_test,user_test):
    error=0
    for i in range(len(paragraph_test)):
        try:
            if paragraph_test[i] != user_test[i]:
                error=error+1
        except:
            error=error+1
            
    return error


def speed_time(time_start,time_end,user_input):
    time_delay=time_end-time_start
    time_round=round(time_delay,2)
    speed=len(user_input)/time_round
    return round(speed)
    

if __name__=='__main__':          
    while True:
        check=input("Ready for speed test: yes / no :")
        if check=="yes":
            
            test=["My main career goal is to learn every day. ","I really want to learn and to progress in my career."," In Computer Science , it requires constant learning and improving."," Taking this course will help me to learn and study this Artificial Intelligence and also to implement it."," It can help me advance in my knowledge."," This course will help me in defining Artificial Intelligence, understanding how Blockchain could potentially impact our business and industry, to write a thought leadership piece regarding use cases and industry potential of Blockchain, explain to clients, friends, joining a community of economists, business leaders, entrepreneurs, and technologists that are shaping this technology as we speak. ","Identifying which aspects of Blockchain seem most important and relevant to us, Walking away with a strong foundation in where Blockchain is going, what it does, and how to prepare for it."," Blockchain course will help me achieve it to learn. Courses on Coursera helped me to greatly increase my  knowledge about  the various fields of  technology."]

            test1=r.choice(test)
            print("***** Typing Speed *****")
            print(test1)
            print()
            print()
            time_1=time()
            testinput=input("Enter : ")
            time_2=time()


            print("Speed : ",speed_time(time_1,time_2,testinput),"w/sec")
            print("Error :",mistake(test1,testinput))
            
        elif check=="no":
            print("Thank You")
            break
        else:
            print("Wrong Input")
            
        