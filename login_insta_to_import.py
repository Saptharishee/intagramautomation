from selenium import webdriver
import datetime
#import pyttsx3
#import speech_recognition as sr

#import unitest #for '''assertIn("str to be serched",driver.title)
from selenium.webdriver.common.keys import Keys
import time



#code artist # '''Saptharishee M '''
from selenium import webdriver
import datetime
import pyautogui as pg 
from selenium.webdriver.common.keys import Keys
import time
import tkinter
from tkinter import *
from tkinter import messagebox
#from messagegrp import *
#from bs4 import BeautifulSoup
#//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[3]/div/div/div/div/div[1]
def options(choice):
    #print("1.message to more no. of people","2.message to specific person","3.comment ","4. like first photo of the artile","5.like first n num of photo in article ","6.search to follow and search to message ","100. enter '100' to find the code artist ","7.exit",sep="\n")
    #choice=int(input("enter your choice"))
    #print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
    #choice=5
    if choice==1:
        time.sleep(3)
        driver.find_element_by_xpath("//a[@class='xWeGp']").click()
        message_ingrp()
        #make it read all the names 
    elif choice==2:
        time.sleep(3)
        driver.find_element_by_xpath("//a[@class='xWeGp']").click()
        message()
    elif choice==3:
        comment_grp()
    elif choice==4:
        like()
    elif choice==5:
        #like_grp()
        like_in()
        #scroll()
    elif choice==6:
        search_person=input("enter the person u want to search :")
        search(search_person)
    elif choice==7:
        driver.close()
        exit()
    elif choice==100:
        tkinter.messagebox.showinfo(title="credits",message="CODE ARTIST : Saptharishee M " )
    print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
def message_ingrp():
    lab1=Label(top,text="no of people you want to send message ",width=20,font=("bold",10))
    lab1.place(x=80,y=150)
    
    time.sleep(5)
    #end=int(entry1)
    end=Entry()
    end.place(x=100,y=150)
    
    driver.find_element_by_xpath("//a[@class='xWeGp']").click()
    #end=int(input("number of people u want to send message"))
    #print(type(end))
    time.sleep(5)
    #entry1.place(x=200,y=120)
    #end=int(end)
    for i in range(1,end+1):
        time.sleep(5)
        person=driver.find_element_by_xpath("//*[@id='react-root']/section/div/div[2]/div/div/div[1]/div[3]/div/div/div/div/div[{}]".format(i))
        person.click()
        time.sleep(3)
        message="If u are reciving this message then the automated testing software is on good go ,Hey this is an automated message from the sender  plss igone if its wrongly sent to you"
        driver.find_element_by_xpath("//*[@id='react-root']/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea").send_keys(message)
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='react-root']/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button").click()
#//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[3]/div/div/div/div/div[1]                                                                                                         
    options()
def message():
    #search=input("enter the name of the person who you wanna messsage")

    q=input("would u like to create a group ???  #say y/n")
    time.sleep(5)
    #driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[2]/a").click()
    if q=="y":
        print("to send grp msgs create or select a doc which contains the list of people in each line")
        file_read=input("enter the name of the file stored in same directory with extension")
        obj=open(file_read)
        senders=obj.readlines()
        time.sleep(3)
        icon_search=driver.find_element_by_xpath("//button[@class='wpO6b ZQScA']").click()
        for i in senders:
            try:
                search=i
                time.sleep(3)
                driver.find_element_by_name("queryBox").send_keys(search)
                time.sleep(3)
                driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/div[2]/div[1]/div/div[3]/button").click()
            except:
                continue
        driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div[2]/div[1]").click()
                    #class="sqdOP yWX7d    y3zKF   cB_4K  "
        time.sleep(3)
                    #_7UhW9   xLCgt      MMzan   _0PwGv            fDxYl
        message="If u are reciving this message then the automated testing software is on good go ,Hey this is an automated message from the sender  plss igone if its wrongly sent to you"
        driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/div/button").click()
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='react-root']/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea").send_keys(message)
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='react-root']/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button").click()
        options()
#//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[3]/div/div/div/div/div[1]
                
    else:
        search=input("enter the name of the person who you wanna messsage")
        time.sleep(3)
        icon_search=driver.find_element_by_xpath("//button[@class='wpO6b ZQScA']").click()
        driver.find_element_by_name("queryBox").send_keys(search)
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/div[2]/div[1]/div/div[3]/button").click()
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]/div/button").click()
      
        message="If u are reciving this message then the automated testing software is on good go ,Hey this is an automated message from the sender  plss igone if its wrongly sent to you"
        
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='react-root']/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea").send_keys(message)
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='react-root']/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button").click()
        options()
                                          
def comment():
    time.sleep(3)
    driver.find_element_by_xpath("//a[@href='/']").click()
    time.sleep(3)
    message="So TRUE 100% "
    comment=driver.find_element_by_xpath("//*[@id='react-root']/section/main/section/div/div[2]/div/article[1]/div[2]/section[3]/div/form/textarea").click()
    time.sleep(3)
    driver.find_element_by_xpath("//*[@id='react-root']/section/main/section/div/div[2]/div/article[1]/div[2]/section[3]/div/form/textarea").send_keys(message)
    time.sleep(3)
    driver.find_element_by_xpath("//*[@id='react-root']/section/main/section/div/div[2]/div/article[1]/div[2]/section[3]/div/form/button").click()
    options()
def comment_grp():
    for i in range(1,9):
        time.sleep(3)
        driver.find_element_by_xpath("//a[@href='/']").click()
        time.sleep(3)
        message="best picture ever ........"
        comment=driver.find_element_by_xpath("//*[@id='react-root']/section/main/section/div/div[2]/div/article[{}]/div[2]/section[3]/div/form/textarea".format(i)).click()
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='react-root']/section/main/section/div/div[2]/div/article[{}]/div[2]/section[3]/div/form/textarea".format(i)).send_keys(message)
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='react-root']/section/main/section/div/div[2]/div/article[{}]/div[2]/section[3]/div/form/button".format(i)).click()
        
    options()
def like():
    time.sleep(3)
    driver.find_element_by_xpath("//a[@href='/']").click()
    time.sleep(3)
    try:
        driver.find_element_by_xpath("//*[@id='react-root']/section/main/section/div/div[2]/div/article[1]/div[2]/section[1]/span[1]/button").click()
    except:
        driver.find_element_by_class_name("wp06b").click()
    #//*[@id="react-root"]/section/main/section/div/div[2]/div/article[2]/div[2]/section[1]/span[1]/button
    #print("sucessful oooo")
    options()
def like_grp():
    time.sleep(3)
    driver.find_element_by_xpath("//a[@href='/']").click()
    time.sleep(3)
    endval=int(input("how many profile do u wanna like :"))
    count=0
    while endval>0:
        try:
            try:
                for i in range(1,9):
                    driver.find_element_by_xpath("//*[@id='react-root']/section/main/section/div/div[2]/div/article[{}]/div[2]/section[1]/span[1]/button".format(i)).click()    
                    endval-=1
                    count+=1
                    print(count)

                    print("naan end val",endval)
            except:
                time.sleep(2)
                y = 1000
                #driver.execute_script("Window.scrollBy(0,500);")
                for timer in range(0,50):
                     driver.execute_script("window.scrollTo(0, "+str(y)+")")
                     #driver.find_element_by_class_name("wpO6b ").click()
                     y += 1000  
                     time.sleep(1)
                try:
                     driver.find_element_by_class_name("wpO6b ").click()
                     count+=1
                     print(count)
                     i+=1
                     endval-=1
                     print("naan end val",endval)
                except Exception as e:
                     time.sleep(4)
                     pg.moveTo(500,500)
                     pg .doubleClick()
                     count+=1
                     endval-=1
                     
                     print(count) 
                     print("naan end val",endval)                
                #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                #if i==9:
                #    i=4
                #elif i==8:
                #    i=5
                #print("naan i :",i)
                #driver.find_element_by_xpath("//*[@id='react-root']/section/main/section/div/div[2]/div/article[4]/div[2]/section[1]/span[1]/button").click()
                #//*[@id="react-root"]/section/main/section/div/div[2]/div/article[4]/div[2]/section[1]/span[1]/button
                
               
        except:
            continue
   
        
    

    options()









def like_in():
    time.sleep(3)
    driver.find_element_by_xpath("//a[@href='/']").click()
    time.sleep(3)
    endval=int(input("how many profile do u wanna like :"))
    count=0
    y=500
    passes=0
    while endval>0:
        try:
            try:
                for i in range(1,9):
                    driver.find_element_by_xpath("//*[@id='react-root']/section/main/section/div/div[2]/div/article[{}]/div[2]/section[1]/span[1]/button".format(i)).click()    
                    endval-=1
                    count+=1
                    print(count)

                    print("naan end val",endval)
            except:
                time.sleep(2)
                try:
                    time.sleep(4)
                    pg.moveTo(500,500)
                    pg .doubleClick()
                    count+=1
                    endval-=1
                     
                    print(count) 
                    print("naan end val",endval)
            
                except:
                    pass 
             

        
        finally:
                passes+=1
                print("no passed : ",passes)                
                pg.press(["down","down","down","down","down","down","down","down","down","down","down","down","down","down","down","down","down","down","down","down","down","down"])
                #driver.execute_script("window.scrollTo(0,"+str(y)+");")
                #"+str(y)+"
                #x=y
                y+=500



def like_top_accord_hashtag():
    search_hash=input("Enter the # with # to like ")
    search(search_hash)
    pass
    options()
def search(search_person):
    try:    
        driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input").send_keys(search_person)
        time.sleep(3)
    except:
        driver.find_element_by_xpath("//*[@id='react-root']/section/div/div[1]/div/div[2]/input").send_keys(search_person)
        time.sleep(3)


    driver.find_element_by_xpath("//a[@class='yCE8d  ']").click()
    print("1.to follow ","2. to  message existing follower",sep="\n")
    choice=int(input("enter your choice"))
    if choice==1:
        try:
            time.sleep(3)
            driver.find_element_by_xpath("//button[@class='_5f5mN       jIbKX  _6VtSN     yZn4P   ']").click()
        except:
            
            try:
                time.sleep(3)
                #//*[@id="react-root"]/section/main/div/header/section/div[2]/button
                driver.find_element_by_xpath("//button[@type='button']").click()
                #"//button[@class=' ffKix sqdOP  L3NKy   y3zKF     ']"
            except:
                time.sleep(3)
                driver.find_element_by_xpath("//*[@id='react-root']/section/main/header/div[2]/div[1]/button").click()

        time.sleep(3)
        print("would you like to message the person ")
        cont=input("#say y/n")
        if cont=='y':
            time.sleep(3)
            #driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/div[2]/div[1]/div/button").click()
            driver.find_element_by_xpath("//button[@class='fAR91 sqdOP  L3NKy _4pI4F   _8A5w5    ']").click()
            message="u got this message now via profile vist.. \n ....Hey this is an automated message from the sender  plss igone if its wrongly sent to you"
            time.sleep(3)
            driver.find_element_by_xpath("//*[@id='react-root']/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea").send_keys(message)
            time.sleep(3)
            driver.find_element_by_xpath("//*[@id='react-root']/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button").click()
            time.sleep(3)
            
        
    elif choice==2:
        time.sleep(3)
        #driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/div[2]/div[1]/div/button").click()
        driver.find_element_by_xpath("//button[@class='fAR91 sqdOP  L3NKy _4pI4F   _8A5w5    ']").click()
        message="u got this message now via profile vist.. \n ....Hey this is an automated message from the sender  plss igone if its wrongly sent to you"
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='react-root']/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea").send_keys(message)
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='react-root']/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button").click()
        time.sleep(3)
    options()
def login():

    

    driver.get(url)
    time.sleep(3)
    driver.find_element_by_xpath("//input[@name='username']").send_keys(username)
    
    driver.find_element_by_xpath("//input[@name='password']").send_keys(password)

    time.sleep(3)

    driver.find_element_by_xpath("//button[@type='submit']").click()
    assert"Instagram"in driver.title

    time.sleep(5)
    #time.sleep(3)
    driver.find_element_by_xpath("//button[@class='sqdOP yWX7d    y3zKF     ']").click()
    #driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div/div/button").click()
    time.sleep(4)
    driver.find_element_by_xpath("//button[@class='aOOlW   HoLwm ']").click()
    #/html/body/div[4]/div/div/div/div[3]/button[2]##/html/body/div[4]/div/div/div/div[3]/button[2]
    #print("Hi!!{}".format(username))
def scroll():
    y=250
    while True:
       for timer in range(0,50):
            driver.execute_script("window.scrollTo(0, "+str(y)+")")
            #driver.find_element_by_class_name("wpO6b ").click()
            pg.doubleClick()
            print(timer)
            y +=250 
            time.sleep(1)

url= 'https://www.instagram.com/'
#username=input("User Name:")
#password=input("Password :")
username="stita_pragyan"
#code artist # '''Saptharishee M '''
#mynameisrodolph
password="letslearn"
#nadclutir12345
driver = webdriver.Chrome('E:\\applications\\crome driver\\chromedriver_win32\\chromedriver.exe')
top=Tk()
top.geometry('500x500')

top.title("gui_instabot")



