from tkinter import *
from tkinter import messagebox as msgbox
import mysql.connector as mycon
import pandas as pd
import tkinter as tk
con1 = mycon.connect(host="localhost", user="root", password="1234", database="ipproject")


if con1.is_connected():
    print("Connected")


#Window
#Coding to display welcome picture + logo of 'Lights, Camera and Popcorn' app
if con1.is_connected():    
    welcomewindow = Tk()
    welcomewindow.title("Welcome to Lights Camera Popcorn!")
    welcomewindow.configure(background="black")
    welcomephoto=PhotoImage(file= "C:\\Users\\mohsi\\Desktop\\welcomeimage.png")
    Label (welcomewindow, image=welcomephoto, bg ="black") .grid(row=0, column=0, sticky=W)        


#Window            
#coding to open the screen from where to choose between logging-in, in case of being an old user, and registering a new account, in case of a new user.        
def openloginorregisterscreen(): 
        startappwindow.destroy()
        global loginorregisterscreen
        loginorregisterscreen = Toplevel()
        loginorregisterscreen.title('Welcome To the Login/Register Screen!')
        loginorregisterscreen.geometry("900x500")
        loginorregisterscreen.configure(background="black")
        l2 = Label(loginorregisterscreen, text="OLD USER", bg='firebrick4', fg='grey99',font='fixedsys',width = 23)
        l2.place(x=190,y=175)
        l3 = Label(loginorregisterscreen, text="NEW USER", bg='firebrick4', fg='grey99',font='fixedsys',width = 23)
        l3.place(x=410,y=175)
        LogIn = Button(loginorregisterscreen,text = "Log-In",bg='medium blue',font='fixedsys',fg='white',width =23, command=openloginwindow)
        LogIn.place(x=190,y=225)
        Register = Button(loginorregisterscreen,text = "Register",bg='medium blue',font='fixedsys',fg='white',width =23, command=openregisterwindow)
        Register.place(x=410, y=225)

        
#Command
#coding to close 'Lights, Camera and Popcorn' app
def closestartappwindow():
    root.destroy()
    startappwindow.destroy()


#window
#Coding to open window from where choose between continuing to 'Lights, Camera and Popcorn' app     
if con1.is_connected():
    startappwindow = Toplevel()
    startappwindow.title("Would you like to continue to the App?")
    startappwindow.configure(background="black")
    startappwindow.geometry("800x500")
    l1 = Label(startappwindow, text="Continue to App?", bg='yellow', fg='grey1',font='fixedsys', width =60)
    l1.place(x=140,y=175)
    b1 = Button(startappwindow,text = "Yes, continue to app.",bg='midnight blue',font='fixedsys',fg='grey99',width =50, command=openloginorregisterscreen)
    b1.place(x=175,y=225)
    b2 = Button(startappwindow,text = "No, do not continue to app.",bg='red4',font='fixedsys',fg='grey99',width =50, command=closestartappwindow)
    b2.place(x=175,y=275)


#Window    
#Coding for opening the Register Window
def openregisterwindow():
        registerscreen = Toplevel()
        registerscreen.title('Register Screen')
        registerscreen.geometry("900x500")
        registerscreen.configure(background="black")
        emaillabel = Label(registerscreen, text="Enter Email", bg='chocolate1',font='fixedsys',fg='white',width =23)
        emaillabel.place(x=125, y =175)
        passwordlabel = Label(registerscreen, text="Enter Password", bg='chocolate1',font='fixedsys',fg='white',width =23)
        passwordlabel.place(x=125, y =225)
        namelabel = Label(registerscreen, text="Enter Name", bg='chocolate1',font='fixedsys',fg='white',width =23)
        namelabel.place(x=125, y =275)
        global emailentry
        emailentry = Entry(registerscreen, font='fixedsys', justify = CENTER, fg='white', bg='light sea green', selectborderwidth = 3, width = 23)
        emailentry.place(x=375, y =175)
        global passwordentry
        passwordentry = Entry(registerscreen, font='fixedsys', justify = CENTER, fg='white', bg='light sea green', selectborderwidth = 3, width = 23)
        passwordentry.place(x=375, y =225)
        global nameentry
        nameentry = Entry(registerscreen, font='fixedsys', justify = CENTER, fg='white', bg='light sea green', selectborderwidth = 3, width = 23)
        nameentry.place(x=375, y =275)
        checkemailbutton = Button(registerscreen,  font='fixedsys', text = "Check Email", bg='firebrick4', fg='white', width =23, command = checkingemail)
        checkemailbutton.place(x = 625, y = 175)
        checkpasswordbutton = Button(registerscreen,  font='fixedsys', text = "Check password", bg='firebrick4', fg='white', width =23, command = checkingpassword)
        checkpasswordbutton.place(x = 625, y = 225)
        submitdetailsbutton = Button(registerscreen,  font='fixedsys', text = "Submit Details", bg='grey33', fg='white', width =23 , command = submitregistrationdetails)
        submitdetailsbutton.place(x = 375, y = 325)
        registerherelabel = Label(registerscreen, text="Register by entering details as instructed below.", bg='grey33',font='fixedsys',fg='white',width =86)
        registerherelabel.place(x=125, y =75)
        registerinfolabel = Label(registerscreen, text="Email must contain '@' and '.com', Password must contain atleast 8 characters and atleast one uppercase letter or numerical digit.",
                                  bg='grey99',font='fixedsys',fg='grey1', wraplength =600)
        registerinfolabel.place(x=200, y =112)
        
        
#Command
#Coding to check email validity and availability
def checkingemail():
        global emaileligibility
        checkemailavailability = emailentry.get()
        if "@"  not in checkemailavailability:
            msgbox.showerror("Error", "Does not contain '@', please re-enter.")
            emaileligibility = "false"

        elif ".com" not in checkemailavailability:
            msgbox.showerror("Error", "Does not contain '.com', please re-enter.")
            emaileligibility = "false"
        else:
            msgbox.showinfo("Email is of correct format")
            emaileligibility = "correct"


#command
#Coding to check if password is of correct format.
def checkingpassword():
    pwd = passwordentry.get()
    global eligibility
    eligibility = "empty"
    for x in pwd:
        if x.isupper()==True or x.isnumeric()==True:
            eligibility = "correct"
            break
        else:
            eligibility = "false"
            continue
    if eligibility ==  "correct"  and len(pwd) >= 8:
        msgbox.showinfo("Password is of correct format")
        eligibility = "correct"
    else: 
        msgbox.showerror("Password is of incorrect format.")


#command
#Coding to submit E-mail, Password and Name for registration.
def submitregistrationdetails():
    checkingemail()
    if emaileligibility == "correct" and eligibility == "correct":
        registersubmitemail = emailentry.get()
        registersubmitname = nameentry.get()
        registersubmitpassword = passwordentry.get()
        sqlinsertemail = "insert into users values (%s,%s,%s)"
        crsr = con1.cursor()
        crsr.execute(sqlinsertemail, (registersubmitemail, registersubmitname, registersubmitpassword))
        con1.commit()
        msgbox.showinfo("Your account has been registered!")
    else:
        msgbox.showerror("Password or Email is of incorrect format.")


#window
#Coding to open a window from where to log-in
def openloginwindow():
    loginorregisterscreen.destroy()
    global loginscreen
    loginscreen = Toplevel()
    loginscreen.title('Log-In Screen')
    loginscreen.geometry("900x500")
    loginscreen.configure(background="black")
    registerherelabel = Label(loginscreen, text="Register by entering details as instructed below.", bg='yellow',font='fixedsys',fg='grey1',width =86)
    registerherelabel.place(x=125, y =112)
    loginemail = Label(loginscreen, text="Email", bg='grey25',font='fixedsys',fg='yellow',width =23)
    loginemail.place(x=250, y =175)
    loginpassword = Label(loginscreen, text="Password", bg='grey25',font='fixedsys',fg='yellow',width =23)
    loginpassword.place(x=250, y =225)
    global loginemailentry
    loginemailentry = Entry(loginscreen, font='fixedsys', justify = CENTER, fg='yellow', bg='grey25', selectborderwidth = 3, width = 23)
    loginemailentry.place(x=500, y =175)
    global loginpasswordentry
    loginpasswordentry = Entry(loginscreen, font='fixedsys', justify = CENTER, fg='yellow', bg='grey25', selectborderwidth = 3, width = 23, show = "*")
    loginpasswordentry.place(x=500, y =225)
    loginbutton = Button(loginscreen,  font='fixedsys', text = "Log-in", bg='yellow', fg='grey1', width =23, command=logintoapp)
    loginbutton.place(x = 375, y = 275)
    newaccountbutton = Button(loginscreen,  font='fixedsys', text = "Sign Up", bg='firebrick4', fg='grey1', width =23, command=openregisterwindow)
    newaccountbutton.place(x = 375, y = 365)
    endprogrambutton = Button(loginscreen,  font='fixedsys', text = "End Program", bg='grey1', fg='firebrick4', width =23, command=endprogram)
    endprogrambutton.place(x = 375, y = 400)
    
#command
#coding to end program
def endprogram():
    msgbox.showinfo("Thankyou for using the - Lights, Camera, Popcorn! - app!")
    loginscreen.destroy()
    loginorregisterscreen.destroy()
    
#Command
#Coding to submit details for log-in
def logintoapp():
    global loginsubmitemail
    loginsubmitemail = loginemailentry.get() #use this for future transactions
    global loginsubmitpassword
    loginsubmitpassword = loginpasswordentry.get()
    sqllogin = "SELECT EMAIL, PASSWORD FROM USERS WHERE Email = %s AND Password = %s"
    loginsql = con1.cursor()
    loginsql.execute(sqllogin, (loginsubmitemail, loginsubmitpassword))
    loginsql.fetchall()
    count=loginsql.rowcount
    if count > 0:
        openhomescreen()
        global useemailtransac #use this for future transactions
        useemailtransac = loginsubmitemail
        loginscreen.destroy()
    else:
        msgbox.showerror("Either user doesn't exist or password is incorrect!")
        


#Window
#Home Screen from where to navigate to seeing which movies are on show, buying tickets, viewing previous purchases,
#and 'about us'- information about the history and foundation of this app/theatre franchise :)
def openhomescreen():
    global homescreen
    homescreen = Toplevel()
    homescreen.title('Menu/Home Screen')
    homescreen.geometry("1000x700")
    homescreen.configure(background="black")
    viewmoviesbutton = Button(homescreen, text="Movies-On-Show", bg='grey25',font='fixedsys',fg='yellow',width =30, command = viewmovieswindow)
    buyticketsbutton = Button(homescreen, text="Buy tickets", bg='grey25',font='fixedsys',fg='yellow',width =30, command = buyticketswindow)
    yourmoviebutton = Button(homescreen, text="YourMovie™", bg='grey25',font='fixedsys',fg='yellow',width =30, command = yourmoviewindow)
    #infoaboutusbutton = Button(homescreen, text="About Us", bg='grey25',font='fixedsys',fg='yellow',width =30)
    logoutbutton = Button(homescreen, text="Log-out", bg='firebrick4',font='fixedsys',fg='grey1',width =30, command = logoutcommand)
    emaillabel = Label(homescreen, text=loginsubmitemail, bg='firebrick4',font='fixedsys',fg='grey99',width =30)
    homescreenlabel = Label(homescreen, text="Lights, Camera, Popcorn!- HOME SCREEN", bg='yellow',font='fixedsys',fg='grey1',width =50)
    viewmoviesbutton.place(x=375, y =175)
    buyticketsbutton.place(x=375, y =225)
    yourmoviebutton.place(x=375, y =275)
    #infoaboutusbutton.place(x=375, y =325)
    logoutbutton.place(x = 375, y=375)
    emaillabel.place(x=750,y=5)
    homescreenlabel.place(x=300,y=125)



#window
#Window showing all movies being shown in theatres
def viewmovieswindow():
    moviescurrentlyshowingscreen = Toplevel()
    moviescurrentlyshowingscreen.title('Movies Currently on show')
    moviescurrentlyshowingscreen.geometry("1000x700")
    moviescurrentlyshowingscreen.configure(background="black")
    currentmovieslabel = Label(moviescurrentlyshowingscreen, text="These are the movies currently showing on the - Lights, Camera, Popcorn! - App. Click on the movies below to view more information before buying your tickets.",
                                bg='grey25',font='fixedsys',fg='yellow', wraplength  =650)
    currentmovieslabel.place(x= 212,  y =125)
    
    notimetodiebutton = Button(moviescurrentlyshowingscreen, text=" #1: 007: No Time To Die",
                               bg='yellow',font='fixedsys',fg='grey25',width =30, command = notimetodiescreen)
    notimetodiebutton.place(x =100, y =175)
    blackwidowbutton = Button(moviescurrentlyshowingscreen, text="#2: Black Widow",
                              bg='yellow',font='fixedsys',fg='grey25',width =30, command = blackwidowscreen)
    blackwidowbutton.place(x =100, y =225)
    venombutton = Button(moviescurrentlyshowingscreen, text="#3: Venom: Let There Be Carnage",
                         bg='yellow',font='fixedsys',fg='grey25',width =30, command = vltbcscreen)
    venombutton.place(x =100, y =275)
    mibutton = Button(moviescurrentlyshowingscreen, text="#4: Mission Impossible: 07",
                      bg='yellow',font='fixedsys',fg='grey25',width =30, command = miscreen)
    mibutton.place(x =100, y =325)
    wonderwomanbutton = Button(moviescurrentlyshowingscreen, text="#5: Wonder Woman 1984",
                               bg='yellow',font='fixedsys',fg='grey25',width =30, command = wwscreen)
    wonderwomanbutton.place(x =400, y =175)
    thebatmanbutton = Button(moviescurrentlyshowingscreen, text="#6: The Batman",
                             bg='yellow',font='fixedsys',fg='grey25',width =30, command = tbscreen)
    thebatmanbutton.place(x =400, y =225)
    marvelseternalsbutton = Button(moviescurrentlyshowingscreen, text="#7: Marvel's Eternals",
                                   bg='yellow',font='fixedsys',fg='grey25',width =30, command = mescreen)
    marvelseternalsbutton.place(x =400, y =275)
    mulanbutton = Button(moviescurrentlyshowingscreen, text="#8: Mulan",
                         bg='yellow',font='fixedsys',fg='grey25',width =30, command = mulanscreen)
    mulanbutton.place(x =400, y =325)
    flashpointbutton = Button(moviescurrentlyshowingscreen, text="#9: Flashpoint",
                              bg='yellow',font='fixedsys',fg='grey25',width =30, command = flashscreen)
    flashpointbutton.place(x =400, y =375)
    ssbutton = Button(moviescurrentlyshowingscreen, text="#10: Suicide Squad 2",
                      bg='yellow',font='fixedsys',fg='grey25',width =30, command= ssscreen)
    ssbutton.place(x =700, y =175)
    unchartedbutton = Button(moviescurrentlyshowingscreen, text="#11: Uncharted",
                             bg='yellow',font='fixedsys',fg='grey25',width =30, command = ucscreen)
    unchartedbutton.place(x =700, y =225)
    cogbutton = Button(moviescurrentlyshowingscreen, text="#12: Crimes Of Grindelwald",
                       bg='yellow',font='fixedsys',fg='grey25',width =30, command = cogscreen)
    cogbutton.place(x =700, y =275)
    jwdbutton = Button(moviescurrentlyshowingscreen, text="#13: Jurassic World: Dominion",
                       bg='yellow',font='fixedsys',fg='grey25',width =30, command = jwdscreen)
    jwdbutton.place(x =700, y =325)

#add all movie information boxes here
#13 to be added



#Window
#Shows all information about the movie, 007: No Time To Die
def notimetodiescreen():
    notimetodieinfo = Toplevel()
    notimetodieinfo.title('007: No Time To Die')
    notimetodieinfo.geometry("1000x700")
    notimetodieinfo.configure(background="grey1")
    nttdtitle = Label(notimetodieinfo, text="007: No Time To Die", bg='yellow',font='fixedsys',fg='grey1')
    nttdtitle.place(x=150, y =75)
    nttdsummary = Label(notimetodieinfo, text="SUMMARY: Recruited to rescue a kidnapped scientist, globe-trotting spy James Bond finds himself hot on the trail of a mysterious villain, who's armed with a dangerous new technology.",
                        bg='blue4',font='fixedsys',fg='grey99', wraplength = 800)
    nttdsummary.place(x=150, y =125)
    nttdcast = Label(notimetodieinfo, text="STARRING: Daniel Craig as 'James Bond', Rami Malek as 'Safin', Ana De Armas as 'Paloma'", bg='blue4',font='fixedsys',fg='grey99', wraplength = 800)
    nttdcast.place(x=150, y =175)
    nttdtime = Label(notimetodieinfo, text="RUNTIME: 163 minutes", bg='blue4',font='fixedsys',fg='grey99')
    nttdtime.place(x=150, y =200)
    nttddirector = Label(notimetodieinfo, text="DIRECTOR: Cary JF", bg='blue4',font='fixedsys',fg='grey99')
    nttddirector.place(x=150, y =225)
    nttdrelease = Label(notimetodieinfo, text="RELEASE DATE: 2020-11-21", bg='blue4',font='fixedsys',fg='grey99')
    nttdrelease.place(x=150, y =250)
##    nttdphoto=PhotoImage(file= "C:\\Users\\mohsi\\Desktop\\nttd.png")
##    Label (notimetodieinfo, image=nttdphoto, bg ="black") .grid(row=0, column=0, sticky=W)


#Window
#Shows all information about the movie, Black Widow
def blackwidowscreen():
    bwinfo = Toplevel()
    bwinfo.title('Black Widow')
    bwinfo.geometry("1000x700")
    bwinfo.configure(background="grey1")
    bwtitle = Label(bwinfo, text="Black Widow", bg='yellow',font='fixedsys',fg='grey1')
    bwtitle.place(x=150, y =75)
    bwsummary = Label(bwinfo, text="SUMMARY: Following the events of Captain America: Civil War (2016), Natasha Romanoff finds herself alone and forced to confront a dangerous conspiracy with ties to her past. Pursued by a force that will stop at nothing to bring her down, Romanoff must deal with her history as a spy and the broken relationships left in her wake long before she became an Avenger.",
                        bg='blue4',font='fixedsys',fg='grey99', wraplength = 800)
    bwsummary.place(x=150, y =125)
    bwcast = Label(bwinfo, text="STARRING: Scarlett Johansson as 'Natasha Romanoff', Florence Pugh as 'Yelena Belova', Rachel Weisz as 'Melina Vostokoff'", bg='blue4',font='fixedsys',fg='grey99', wraplength = 800)
    bwcast.place(x=150, y =200)
    bwtime = Label(bwinfo, text="RUNTIME: 120+ minutes", bg='blue4',font='fixedsys',fg='grey99')
    bwtime.place(x=150, y =240)
    bwdirector = Label(bwinfo, text="DIRECTOR: Cate Shortland", bg='blue4',font='fixedsys',fg='grey99')
    bwdirector.place(x=150, y =265)
    bwrelease = Label(bwinfo, text="RELEASE DATE: 2020-11-06", bg='blue4',font='fixedsys',fg='grey99')
    bwrelease.place(x=150, y =290)


#Window
#Shows all information about the movie, Venom: Let there be Carnage
def vltbcscreen():
    vltbcinfo = Toplevel()
    vltbcinfo.title('Venom: Let there be Carnage')
    vltbcinfo.geometry("1000x700")
    vltbcinfo.configure(background="grey1")
    vltbctitle = Label(vltbcinfo, text="Venom: Let there be Carnage", bg='yellow',font='fixedsys',fg='grey1')
    vltbctitle.place(x=150, y =75)
    vltbcsummary = Label(vltbcinfo, text="SUMMARY: Venom: Let There Be Carnage is an American superhero film based on the Marvel Comics character Venom, produced by Columbia Pictures in association with Marvel and Tencent Pictures.",
                        bg='blue4',font='fixedsys',fg='grey99', wraplength = 800)
    vltbcsummary.place(x=150, y =125)
    vltbccast = Label(vltbcinfo, text="STARRING: Tom Hardy as 'Eddie Brock / Venom', Michelle Williams as 'Anne Weying', Woody Harrelson as 'Cletus Kasady / Carnage'",
                      bg='blue4',font='fixedsys',fg='grey99', wraplength = 800)
    vltbccast.place(x=150, y =200)
    vltbctime = Label(vltbcinfo, text="RUNTIME: 120+ minutes", bg='blue4',font='fixedsys',fg='grey99')
    vltbctime.place(x=150, y =240)
    vltbcdirector = Label(vltbcinfo, text="DIRECTOR: Andy Serkis", bg='blue4',font='fixedsys',fg='grey99')
    vltbcdirector.place(x=150, y =265)
    vltbcrelease = Label(vltbcinfo, text="RELEASE DATE: 2020-10-31", bg='blue4',font='fixedsys',fg='grey99')
    vltbcrelease.place(x=150, y =290)


#Window
#Shows all information about the movie, Mission Impossible: 07
def miscreen():
    miinfo = Toplevel()
    miinfo.title('Mission Impossible: 07')
    miinfo.geometry("1000x700")
    miinfo.configure(background="grey1")
    mititle = Label(miinfo, text="Mission Impossible: 07", bg='yellow',font='fixedsys',fg='grey1')
    mititle.place(x=150, y =75)
    misummary = Label(miinfo, text="SUMMARY: Mission: Impossible 7 is an American action spy film written and directed by Christopher McQuarrie, and starring Tom Cruise, who reprises his role as Ethan Hunt.",
                        bg='blue4',font='fixedsys',fg='grey99', wraplength = 800)
    misummary.place(x=150, y =125)
    micast = Label(miinfo, text="STARRING: Tom Cruise as 'Ethan Hunt', Ving Rhames as 'Luther Stickell', Vanessa Kirby as 'Alanna Mitsopolis'",
                      bg='blue4',font='fixedsys',fg='grey99', wraplength = 800)
    micast.place(x=150, y =165)
    mitime = Label(miinfo, text="RUNTIME: 120+ minutes", bg='blue4',font='fixedsys',fg='grey99')
    mitime.place(x=150, y =205)
    midirector = Label(miinfo, text="DIRECTOR: Christopher McQuarrie", bg='blue4',font='fixedsys',fg='grey99')
    midirector.place(x=150, y =230)
    mirelease = Label(miinfo, text="RELEASE DATE: 2020-11-19", bg='blue4',font='fixedsys',fg='grey99')
    mirelease.place(x=150, y =255)


#Window
#Shows all information about the movie, Wonder Woman 1984
def wwscreen():
    wwinfo = Toplevel()
    wwinfo.title('Wonder Woman 1984')
    wwinfo.geometry("1000x700")
    wwinfo.configure(background="grey1")
    wwtitle = Label(wwinfo, text="Wonder Woman 1984", bg='yellow',font='fixedsys',fg='grey1')
    wwtitle.place(x=150, y =75)
    wwsummary = Label(wwinfo, text="SUMMARY: In 1984, during the Cold War, Diana Prince comes into conflict with two formidable foes—media businessman Maxwell Lord and friend-turned-enemy Barbara Ann Minerva while reuniting with Steve Trevor.",
                        bg='blue4',font='fixedsys',fg='grey99', wraplength = 800)
    wwsummary.place(x=150, y =125)
    wwcast = Label(wwinfo, text="STARRING: Pedro Pascal as 'Maxwell Lord', Gal Gadot as 'Diana Prince / Wonder Woman', Chris Pine as 'Steve Trevor'.",
                      bg='blue4',font='fixedsys',fg='grey99', wraplength = 800)
    wwcast.place(x=150, y =200)
    wwtime = Label(wwinfo, text="RUNTIME: 151 minutes", bg='blue4',font='fixedsys',fg='grey99')
    wwtime.place(x=150, y =240)
    wwdirector = Label(wwinfo, text="DIRECTOR: Patty Jenkins", bg='blue4',font='fixedsys',fg='grey99')
    wwdirector.place(x=150, y =265)
    wwrelease = Label(wwinfo, text="RELEASE DATE: 2020-12-16", bg='blue4',font='fixedsys',fg='grey99')
    wwrelease.place(x=150, y =290)


#Window
#Shows all information about the movie, The Batman
def tbscreen():
    tbinfo = Toplevel()
    tbinfo.title('The Batman')
    tbinfo.geometry("1000x700")
    tbinfo.configure(background="grey1")
    tbtitle = Label(tbinfo, text="The Batman", bg='yellow',font='fixedsys',fg='grey1')
    tbtitle.place(x=150, y =75)
    tbsummary = Label(tbinfo, text="SUMMARY: In his second year of fighting crime, Batman explores the corruption that plagues Gotham City and how it may tie to his own family, in addition to coming into conflict with a serial killer known as the Riddler.",
                        bg='blue4',font='fixedsys',fg='grey99', wraplength = 800)
    tbsummary.place(x=150, y =125)
    tbcast = Label(tbinfo, text="STARRING: Robert Pattinson as 'Bruce Wayne / The Batman', Zoë Kravitz as 'Selina Kyle / Catwoman', Paul Dano as 'Edward Nashton / Riddler'.",
                      bg='blue4',font='fixedsys',fg='grey99', wraplength = 800)
    tbcast.place(x=150, y =200)
    tbtime = Label(tbinfo, text="RUNTIME: 180+ minutes", bg='blue4',font='fixedsys',fg='grey99')
    tbtime.place(x=150, y =240)
    tbdirector = Label(tbinfo, text="DIRECTOR: Matt Reeves", bg='blue4',font='fixedsys',fg='grey99')
    tbdirector.place(x=150, y =265)
    tbrelease = Label(tbinfo, text="RELEASE DATE: 2020-12-07", bg='blue4',font='fixedsys',fg='grey99')
    tbrelease.place(x=150, y =290)


#Window
#Shows all information about the movie, Marvel's Eternals
def mescreen():
    meinfo = Toplevel()
    meinfo.title("Marvel's Eternals")
    meinfo.geometry("1000x700")
    meinfo.configure(background="grey1")
    metitle = Label(meinfo, text="Marvel's Eternals", bg='yellow',font='fixedsys',fg='grey1')
    metitle.place(x=150, y =75)
    mesummary = Label(meinfo, text="SUMMARY: After an unexpected tragedy following the events of Avengers: Endgame (2019), the Eternals—an immortal alien race created by the Celestials who have secretly lived on Earth for over 7000 years—reunite to protect humanity from their evil counterparts, the Deviants.",
                        bg='blue4',font='fixedsys',fg='grey99', wraplength = 800)
    mesummary.place(x=150, y =125)
    mecast = Label(meinfo, text="STARRING: Angelina Jolie as 'Thena', Richard Madden as 'Ikaris', Kumail Nanjiani as 'Kingo'.",
                      bg='blue4',font='fixedsys',fg='grey99', wraplength = 800)
    mecast.place(x=150, y =200)
    metime = Label(meinfo, text="RUNTIME: 120+ minutes", bg='blue4',font='fixedsys',fg='grey99')
    metime.place(x=150, y =240)
    medirector = Label(meinfo, text="DIRECTOR: Chloé Zhao", bg='blue4',font='fixedsys',fg='grey99')
    medirector.place(x=150, y =265)
    merelease = Label(meinfo, text="RELEASE DATE: 2020-11-05", bg='blue4',font='fixedsys',fg='grey99')
    merelease.place(x=150, y =290)


#Window
#Shows all information about the movie, Mulan
def mulanscreen():
    mulaninfo = Toplevel()
    mulaninfo.title("Mulan")
    mulaninfo.geometry("1000x700")
    mulaninfo.configure(background="grey1")
    mulantitle = Label(mulaninfo, text="Mulan", bg='yellow',font='fixedsys',fg='grey1')
    mulantitle.place(x=150, y =75)
    mulansummary = Label(mulaninfo, text="SUMMARY: In Imperial China, Hua Mulan is an adventurous and active girl, to the disappointment of her parents, who hopes that one day she will be wed to a good husband. As a young woman, Mulan is forced to meet with a matchmaker to demonstrate her fitness as a future wife. Mulan, flustered, attempts to pour tea in front of the matchmaker, but a spider causes a panic that destroys the kettle, and the matchmaker calls her a disgrace in front of her family.",
                        bg='blue4',font='fixedsys',fg='grey99', wraplength = 800)
    mulansummary.place(x=150, y =125)
    mulancast = Label(mulaninfo, text="STARRING: Yifei Liu as 'Mulan', Donnie Yen as 'Commander Tung', Tzi Ma as 'Hua Zhou'.",
                      bg='blue4',font='fixedsys',fg='grey99', wraplength = 800)
    mulancast.place(x=150, y =215)
    mulantime = Label(mulaninfo, text="RUNTIME: 115 minutes", bg='blue4',font='fixedsys',fg='grey99')
    mulantime.place(x=150, y =240)
    mulandirector = Label(mulaninfo, text="DIRECTOR: Niki Caro", bg='blue4',font='fixedsys',fg='grey99')
    mulandirector.place(x=150, y =265)
    mulanrelease = Label(mulaninfo, text="RELEASE DATE: 2020-10-04", bg='blue4',font='fixedsys',fg='grey99')
    mulanrelease.place(x=150, y =290)


#Window
#Shows all information about the movie, FlashPoint
def flashscreen():
    flashinfo = Toplevel()
    flashinfo.title("FlashPoint")
    flashinfo.geometry("1000x700")
    flashinfo.configure(background="grey1")
    flashtitle = Label(flashinfo, text="FlashPoint", bg='yellow',font='fixedsys',fg='grey1')
    flashtitle.place(x=150, y =75)
    flashsummary = Label(flashinfo, text="SUMMARY: Feature film based on the comic book superhero, The Flash. Stars Ezra Miller as Central City Police Department Detective Bartholomew 'Barry' Henry Allen, who is given the superpowers of superspeed after being struck by lightning during a science experiment by the city's most renknowned Laboratory that goes wrong.",
                        bg='blue4',font='fixedsys',fg='grey99', wraplength = 800)
    flashsummary.place(x=150, y =125)
    flashcast = Label(flashinfo, text="STARRING: Ezra Miller as 'Barry Allen / The Flash'.",
                      bg='blue4',font='fixedsys',fg='grey99', wraplength = 800)
    flashcast.place(x=150, y =215)
    flashtime = Label(flashinfo, text="RUNTIME: 120+ minutes", bg='blue4',font='fixedsys',fg='grey99')
    flashtime.place(x=150, y =240)
    flashdirector = Label(flashinfo, text="DIRECTOR: Andrés Muschietti", bg='blue4',font='fixedsys',fg='grey99')
    flashdirector.place(x=150, y =265)
    flashrelease = Label(flashinfo, text="RELEASE DATE: 2020-12-25", bg='blue4',font='fixedsys',fg='grey99')
    flashrelease.place(x=150, y =290)


#Window
#Shows all information about the movie, Suicide Squad 2
def ssscreen():
    ssinfo = Toplevel()
    ssinfo.title("Suicide Squad 2")
    ssinfo.geometry("1000x700")
    ssinfo.configure(background="grey1")
    sstitle = Label(ssinfo, text="Suicide Squad 2", bg='yellow',font='fixedsys',fg='grey1')
    sstitle.place(x=150, y =75)
    sssummary = Label(ssinfo, text="SUMMARY: The further adventures of Harley Quinn, Rick Flag and their team of assembled supervillains.",
                        bg='blue4',font='fixedsys',fg='grey99', wraplength = 900)
    sssummary.place(x=150, y =125)
    sscast = Label(ssinfo, text="STARRING: Margot Robbie as 'Harley Quinn', John Cena as 'Peacemaker', Idris Elba as 'Bloodsport'.",
                      bg='blue4',font='fixedsys',fg='grey99', wraplength = 800)
    sscast.place(x=150, y =150)
    sstime = Label(ssinfo, text="RUNTIME: 120+ minutes", bg='blue4',font='fixedsys',fg='grey99')
    sstime.place(x=150, y =175)
    ssdirector = Label(ssinfo, text="DIRECTOR: James Gunn", bg='blue4',font='fixedsys',fg='grey99')
    ssdirector.place(x=150, y =200)
    ssrelease = Label(ssinfo, text="RELEASE DATE: 2020-12-29", bg='blue4',font='fixedsys',fg='grey99')
    ssrelease.place(x=150, y =225)


#Window
#Shows all information about the movie, UnCharted
def ucscreen():
    ucinfo = Toplevel()
    ucinfo.title('UnCharted')
    ucinfo.geometry("1000x700")
    ucinfo.configure(background="grey1")
    uctitle = Label(ucinfo, text="UnCharted", bg='yellow',font='fixedsys',fg='grey1')
    uctitle.place(x=150, y =75)
    ucsummary = Label(ucinfo, text="SUMMARY: An American Action adventure film based on the PlayStation exclusive videogame, Uncharted 4: A thief's End.",
                        bg='blue4',font='fixedsys',fg='grey99', wraplength = 800)
    ucsummary.place(x=150, y =125)
    uccast = Label(ucinfo, text="STARRING: Tom Holland as 'Nathan Drake', Sophia Taylor Ali as 'Chloe Frazer', Mark Wahlberg as 'Victor Sully Sullivan'.",
                      bg='blue4',font='fixedsys',fg='grey99', wraplength = 800)
    uccast.place(x=150, y =175)
    uctime = Label(ucinfo, text="RUNTIME: 120+ minutes", bg='blue4',font='fixedsys',fg='grey99')
    uctime.place(x=150, y =215)
    ucdirector = Label(ucinfo, text="DIRECTOR: Ruben Fleischer", bg='blue4',font='fixedsys',fg='grey99')
    ucdirector.place(x=150, y =240)
    ucrelease = Label(ucinfo, text="RELEASE DATE: 2020-12-31", bg='blue4',font='fixedsys',fg='grey99')
    ucrelease.place(x=150, y =265)


#Window
#Shows all information about the movie, Crimes Of Grindelwald
def cogscreen():
    coginfo = Toplevel()
    coginfo.title('Crimes Of Grindelwald')
    coginfo.geometry("1000x700")
    coginfo.configure(background="grey1")
    cogtitle = Label(coginfo, text="Crimes Of Grindelwald", bg='yellow',font='fixedsys',fg='grey1')
    cogtitle.place(x=150, y =75)
    cogsummary = Label(coginfo, text="SUMMARY: Gellert Grindelwald plans to raise an army of wizards to rule over non-magical beings. In response, Newt Scamander's former professor, Albus Dumbledore, seeks his help to stop him.",
                        bg='blue4',font='fixedsys',fg='grey99', wraplength = 800)
    cogsummary.place(x=150, y =125)
    cogcast = Label(coginfo, text="STARRING: Eddie Redmayne as 'Newt Scamander', Johnny Depp as 'Gellert Grindelwald', Ezra Miller as 'Credence Barebone', Jude Law as 'Albus PVB Dumbledore', Katherine Waterston as 'Tina Goldstein'.",
                      bg='blue4',font='fixedsys',fg='grey99', wraplength = 800)
    cogcast.place(x=150, y =165)
    cogtime = Label(coginfo, text="RUNTIME: 134 minutes", bg='blue4',font='fixedsys',fg='grey99')
    cogtime.place(x=150, y =205)
    cogdirector = Label(coginfo, text="DIRECTOR: David Yates", bg='blue4',font='fixedsys',fg='grey99')
    cogdirector.place(x=150, y =230)
    cogrelease = Label(coginfo, text="RELEASE DATE: 2020-12-26", bg='blue4',font='fixedsys',fg='grey99')
    cogrelease.place(x=150, y =255)


#Window
#Shows all information about the movie, Jurassic World: Dominion
def jwdscreen():
    jwdinfo = Toplevel()
    jwdinfo.title('Jurassic World: Dominion')
    jwdinfo.geometry("1000x700")
    jwdinfo.configure(background="grey1")
    jwdtitle = Label(jwdinfo, text="Jurassic World: Dominion", bg='yellow',font='fixedsys',fg='grey1')
    jwdtitle.place(x=150, y =75)
    jwdsummary = Label(jwdinfo, text="SUMMARY: Sequel to the 2018 film 'Jurassic World: Fallen Kingdom'; the plot will revolve around the mutual co-existence of dinosaurs and humans, following the climax of the prequel.",
                        bg='blue4',font='fixedsys',fg='grey99', wraplength = 800)
    jwdsummary.place(x=150, y =125)
    jwdcast = Label(jwdinfo, text="STARRING: Bryce Dallas Howard as 'Claire Dearing', Chris Pratt as 'Owen Grady', Sam Neill as 'Dr. Alan Grant', Laura Dern as 'Dr. Ellie Sattler', Jeff Goldblum as 'Dr. Ian Malcolm'.",
                      bg='blue4',font='fixedsys',fg='grey99', wraplength = 800)
    jwdcast.place(x=150, y =165)
    jwdtime = Label(jwdinfo, text="RUNTIME: 180+ minutes", bg='blue4',font='fixedsys',fg='grey99')
    jwdtime.place(x=150, y =205)
    jwddirector = Label(jwdinfo, text="DIRECTOR: Colin Trevorrow", bg='blue4',font='fixedsys',fg='grey99')
    jwddirector.place(x=150, y =230)
    jwdrelease = Label(jwdinfo, text="RELEASE DATE: 2021-01-09", bg='blue4',font='fixedsys',fg='grey99')
    jwdrelease.place(x=150, y =255)



#window
#Window from where to buy tickets
def buyticketswindow():
    buyticketsscreen = Toplevel()
    buyticketsscreen.title('Buy your tickets here!')
    buyticketsscreen.geometry("1000x700")
    buyticketsscreen.configure(background="maroon")
    buyticketslabel = Label(buyticketsscreen, text="Buy Tickets here!", bg='grey99',font='fixedsys',fg='grey1',width =50)
    buyticketslabel.place(x=525, y =175)
    
    #column of movies available to buy tickets for
    allmoviesavailablelabel = Label(buyticketsscreen, text="MOVIES SHOWING", bg='grey1',font='fixedsys',fg='grey99', width = 30)
    allmoviesavailablelabel.place(x=25, y =175)
    notimetodielabel = Label(buyticketsscreen, text="#1: 007: No Time To Die", bg='grey1',font='fixedsys',fg='grey99',width= 30)
    notimetodielabel.place(x=25, y =200)
    bwlabel = Label(buyticketsscreen, text="#2: Black Widow", bg='grey1',font='fixedsys',fg='grey99',width =30)
    bwlabel.place(x=25, y =220)
    vltbclabel = Label(buyticketsscreen, text="#3: Venom: Let There Be Carnage", bg='grey1',font='fixedsys',fg='grey99',width =30)
    vltbclabel.place(x=25, y =240)
    milabel = Label(buyticketsscreen, text="#4: Mission Impossible: 07", bg='grey1',font='fixedsys',fg='grey99',width =30)
    milabel.place(x=25, y =260)
    wwlabel = Label(buyticketsscreen, text="#5: Wonder Woman 1984", bg='grey1',font='fixedsys',fg='grey99',width =30)
    wwlabel.place(x=25, y =280)
    tblabel = Label(buyticketsscreen, text="#6: The Batman", bg='grey1',font='fixedsys',fg='grey99',width =30)
    tblabel.place(x=25, y =300)
    melabel = Label(buyticketsscreen, text="#7: Marvel's Eternals", bg='grey1',font='fixedsys',fg='grey99',width =30)
    melabel.place(x=25, y =320)
    mulanlabel = Label(buyticketsscreen, text="#8: Mulan", bg='grey1',font='fixedsys',fg='grey99',width =30)
    mulanlabel.place(x=25, y =340)
    flashlabel = Label(buyticketsscreen, text="#9: FlashPoint", bg='grey1',font='fixedsys',fg='grey99',width =30)
    flashlabel.place(x=25, y =360)
    sslabel = Label(buyticketsscreen, text="#10: Suicide Squad 2", bg='grey1',font='fixedsys',fg='grey99',width =30)
    sslabel.place(x=25, y =380)
    uclabel = Label(buyticketsscreen, text="#11: UnCharted", bg='grey1',font='fixedsys',fg='grey99',width =30)
    uclabel.place(x=25, y =400)
    coglabel = Label(buyticketsscreen, text="#12: Crimes Of Grindelwald", bg='grey1',font='fixedsys',fg='grey99',width =30)
    coglabel.place(x=25, y =420)
    jwdlabel = Label(buyticketsscreen, text="#13: Jurassic World: Dominion", bg='grey1',font='fixedsys',fg='grey99',width =30)
    jwdlabel.place(x=25, y =440)
    
    #column of show timings
    alltimingslabel = Label(buyticketsscreen, text="SHOW TIMINGS", bg='grey1',font='fixedsys',fg='grey99')
    alltimingslabel.place(x=275, y =175)
    notimetodieshowtime = Label(buyticketsscreen, text="3:00 PM", bg='grey1',font='fixedsys',fg='grey99',width= 12)
    notimetodieshowtime.place(x=275, y =200)
    bwshowtime = Label(buyticketsscreen, text="4:00 PM", bg='grey1',font='fixedsys',fg='grey99',width =12)
    bwshowtime.place(x=275, y =220)
    vltbcshowtime = Label(buyticketsscreen, text="5:00 PM", bg='grey1',font='fixedsys',fg='grey99',width =12)
    vltbcshowtime.place(x=275, y =240)
    mishowtime = Label(buyticketsscreen, text="6:00 PM", bg='grey1',font='fixedsys',fg='grey99',width =12)
    mishowtime.place(x=275, y =260)
    wwshowtime = Label(buyticketsscreen, text="7:00 PM", bg='grey1',font='fixedsys',fg='grey99',width =12)
    wwshowtime.place(x=275, y =280)
    tbshowtime = Label(buyticketsscreen, text="8:00 PM", bg='grey1',font='fixedsys',fg='grey99',width =12)
    tbshowtime.place(x=275, y =300)
    meshowtime = Label(buyticketsscreen, text="9:00 PM", bg='grey1',font='fixedsys',fg='grey99',width =12)
    meshowtime.place(x=275, y =320)
    mulanshowtime = Label(buyticketsscreen, text="10:00 PM", bg='grey1',font='fixedsys',fg='grey99',width =12)
    mulanshowtime.place(x=275, y =340)
    flashshowtime = Label(buyticketsscreen, text="10:45 PM", bg='grey1',font='fixedsys',fg='grey99',width =12)
    flashshowtime.place(x=275, y =360)
    ssshowtime = Label(buyticketsscreen, text="11:30 PM", bg='grey1',font='fixedsys',fg='grey99',width =12)
    ssshowtime.place(x=275, y =380)
    ucshowtime = Label(buyticketsscreen, text="12:15 AM", bg='grey1',font='fixedsys',fg='grey99',width =12)
    ucshowtime.place(x=275, y =400)
    cogshowtime = Label(buyticketsscreen, text="1:00 AM", bg='grey1',font='fixedsys',fg='grey99',width =12)
    cogshowtime.place(x=275, y =420)
    jwdshowtime = Label(buyticketsscreen, text="1:45 AM", bg='grey1',font='fixedsys',fg='grey99',width =12)
    jwdshowtime.place(x=275, y =440)
    
    #column of show prices
    allpriceslabel = Label(buyticketsscreen, text="PRICES", bg='grey1',font='fixedsys',fg='grey99')
    allpriceslabel.place(x=387, y =175)
    notimetodieprice = Label(buyticketsscreen, text="12 USD", bg='grey1',font='fixedsys',fg='grey99',width= 6)
    notimetodieprice.place(x=387, y =200)
    bwprice = Label(buyticketsscreen, text="12 USD", bg='grey1',font='fixedsys',fg='grey99',width =6)
    bwprice.place(x=387, y =220)
    vltbcprice = Label(buyticketsscreen, text="12 USD", bg='grey1',font='fixedsys',fg='grey99',width =6)
    vltbcprice.place(x=387, y =240)
    miprice = Label(buyticketsscreen, text="11 USD", bg='grey1',font='fixedsys',fg='grey99',width =6)
    miprice.place(x=387, y =260)
    wwprice = Label(buyticketsscreen, text="13 USD", bg='grey1',font='fixedsys',fg='grey99',width =6)
    wwprice.place(x=387, y =280)
    tbprice = Label(buyticketsscreen, text="13 USD", bg='grey1',font='fixedsys',fg='grey99',width =6)
    tbprice.place(x=387, y =300)
    meprice = Label(buyticketsscreen, text="12 USD", bg='grey1',font='fixedsys',fg='grey99',width =6)
    meprice.place(x=387, y =320)
    mulanprice = Label(buyticketsscreen, text="14 USD", bg='grey1',font='fixedsys',fg='grey99',width =6)
    mulanprice.place(x=387, y =340)
    flashprice = Label(buyticketsscreen, text="10 USD", bg='grey1',font='fixedsys',fg='grey99',width =6)
    flashprice.place(x=387, y =360)
    ssprice = Label(buyticketsscreen, text="13 USD", bg='grey1',font='fixedsys',fg='grey99',width =6)
    ssprice.place(x=387, y =380)
    ucprice = Label(buyticketsscreen, text="15 USD", bg='grey1',font='fixedsys',fg='grey99',width =6)
    ucprice.place(x=387, y =400)
    cogprice = Label(buyticketsscreen, text="16 USD", bg='grey1',font='fixedsys',fg='grey99',width =6)
    cogprice.place(x=387, y =420)
    jwdprice = Label(buyticketsscreen, text="12 USD", bg='grey1',font='fixedsys',fg='grey99',width =6)
    jwdprice.place(x=387, y =440)
    
    #entry and selection of tickets
    EntryMovieNumberLabel = Label(buyticketsscreen, text="Choose Movie here, by typing in Movie# ONLY", bg='grey99',font='fixedsys',fg='grey1')
    EntryMovieNumberLabel.place(x=475, y =225)
    global EntryMovieNumberEntry
    EntryMovieNumberEntry = Entry(buyticketsscreen, font='fixedsys', justify = CENTER, fg='grey1', bg='grey99', selectborderwidth = 3, width = 15)
    EntryMovieNumberEntry.place(x=850, y =225)
    EntryDateLabel = Label(buyticketsscreen, text="Choose the Date on which you wish to watch the Movie, by typing the Date in YYYY-MM-DD format ONLY",
                           bg='grey99',font='fixedsys',fg='grey1', wraplength  = 375)
    EntryDateLabel.place(x=475, y =265)
    global EntryDateEntry
    EntryDateEntry = Entry(buyticketsscreen, font='fixedsys', justify = CENTER, fg='grey1', bg='grey99', selectborderwidth = 3, width = 15)
    EntryDateEntry.place(x=850, y =265)
    reserveticketsbutton = Button(buyticketsscreen, text="Reserve Ticket",bg='firebrick4',font='fixedsys',fg='grey99',width =25, command = buytickets)
    reserveticketsbutton.place(x =637, y =425)


#Command
#Buys the tickets
def buytickets():
    #first part of insert query, not executed until the condition is left unfulfilled later
    submitemail = useemailtransac
    submitmovie = EntryMovieNumberEntry.get()
    submitdate = EntryDateEntry.get()
    buyticketquery = "Insert into ticketssold values (%s,%s,%s)"
    submitqry = con1.cursor()
    #counts rows, i.e. tickets already sold for same showing
    checkmovie = EntryMovieNumberEntry.get()
    checkdate = EntryDateEntry.get()
    checksqlquery = "SELECT * FROM ticketssold WHERE MovieNumber = %s AND DateOfShowing = %s"
    checkquery = con1.cursor()
    checkquery.execute(checksqlquery, (checkmovie, checkdate))
    checkquery.fetchall()
    checkcount=checkquery.rowcount
    #checks if less than 100 tickets have been sold
    if checkcount > 99:
        #if 100 have been sold
        msgbox.showerror("No Tickets available for this show :( Try a different movie/date")
    else:
        #if less than 100 have been sold
        #insert query is completed
        submitqry.execute(buyticketquery, (submitemail, submitmovie, submitdate))
        con1.commit()
        msgbox.showinfo("Your ticket has been reserved!")
    

#window
#window where user can manage bookings, refund purchases
def yourmoviewindow():
    yourmoviemenu = Toplevel()
    yourmoviemenu.title('YourMovie')
    yourmoviemenu.geometry("900x500")
    yourmoviemenu.configure(background="grey1")
    checkprevbutton = Button(yourmoviemenu, text="Check Previous Purchases",bg='firebrick4',font='fixedsys',fg='grey99',width =45, command = previouspurchaseswindow)    
    checkprevbutton.place(x=225, y =175)
    refundbutton = Button(yourmoviemenu, text="Cancelling Previous Purchases",bg='firebrick4',font='fixedsys',fg='grey99',width =45, command = refundwindow)    
    refundbutton.place(x=225, y =225)


#Window
#Window where user can check previous purchases
def previouspurchaseswindow():
    ppw = Toplevel()
    ppw.title('Previous Purchases Search')
    ppw.geometry("900x500")
    ppw.configure(background="grey1")
    findpplabel = Label(ppw, text="Find Previous Purchases by entering in the fields given below", bg='grey99',font='fixedsys',fg='grey1',wraplength = 600)
    findpplabel.place(x=175, y =100)
    entermovienumberlabel = Label(ppw, text="Enter Movie Number", bg='grey99',font='fixedsys',fg='grey1',width = 30)
    entermovienumberlabel.place(x=175, y =125)
    enterdatelabel = Label(ppw, text="Enter Date Of Showing", bg='grey99',font='fixedsys',fg='grey1',width = 30)
    enterdatelabel.place(x=175, y =150)
    global movieentry
    movieentry = Entry(ppw, font='fixedsys', justify = CENTER, fg='white', bg='light sea green', selectborderwidth = 3, width = 24)
    movieentry.place(x=475, y =125)
    global dateentry
    dateentry = Entry(ppw, font='fixedsys', justify = CENTER, fg='white', bg='light sea green', selectborderwidth = 3, width = 24)
    dateentry.place(x=475, y =150)
    findppbutton = Button(ppw, text="Search",bg='yellow',font='fixedsys',fg='grey1',width =30, command = findppsearchcommand)    
    findppbutton.place(x=320, y =175)

#Command
#searches for previous purchases
def findppsearchcommand():
    ppwr = Toplevel()
    ppwr.title('Previous Purchases Result')
    ppwr.geometry("900x500")
    ppwr.configure(background="grey1")
    mepp = movieentry.get()
    dapp = dateentry.get()
    checkpp = "SELECT MovieNumber, DateOfShowing FROM ticketssold WHERE Email = %s AND MovieNumber = %s AND DateOfShowing = %s"
    checkppsql = con1.cursor()
    checkppsql.execute(checkpp, (loginsubmitemail, mepp, dapp))
    checkppresult = checkppsql.fetchall()
    toshowresultlabel = Label(ppwr, text=checkppresult, bg='grey99',font='fixedsys',fg='grey1',wraplength  = 125)
    toshowresultlabel.place(x=100,y=100)
    ticketsboughtlabel = Label(ppwr, text='Tickets Bought', bg='yellow',font='fixedsys',fg='grey1',width = 20)
    ticketsboughtlabel.place(x=100,y=25)
    movieanddatelabel = Label(ppwr, text='Movie Number  Date Of showing', bg='yellow',font='fixedsys',fg='grey1',width = 30)
    movieanddatelabel.place(x=100,y=50)


#window
#window where user can take back their reservations
def refundwindow():
    rsw = Toplevel()
    rsw.title('Cancelling Tickets')
    rsw.geometry("900x500")
    rsw.configure(background="grey1")
    findrlabel = Label(rsw, text="Choose which Tickets you want to cancel by entering in the fields given", bg='grey99',font='fixedsys',fg='grey1',wraplength = 600)
    findrlabel.place(x=175, y =100)
    entermovienumberforrefund = Label(rsw, text="Enter Movie Number", bg='grey99',font='fixedsys',fg='grey1',width = 30)
    entermovienumberforrefund.place(x=175, y =125)
    enterdateforrefund = Label(rsw, text="Enter Date Of Showing", bg='grey99',font='fixedsys',fg='grey1',width = 30)
    enterdateforrefund.place(x=175, y =150)
    global movieentryrefund
    movieentryrefund = Entry(rsw, font='fixedsys', justify = CENTER, fg='white', bg='light sea green', selectborderwidth = 3, width = 24)
    movieentryrefund.place(x=475, y =125)
    global dateentryrefund
    dateentryrefund = Entry(rsw, font='fixedsys', justify = CENTER, fg='white', bg='light sea green', selectborderwidth = 3, width = 24)
    dateentryrefund.place(x=475, y =150)
    refundbutton = Button(rsw, text="Cancel",bg='yellow',font='fixedsys',fg='grey1',width =30, command = refundcommand)    
    refundbutton.place(x=320, y =175)
    notelabel = Label(rsw, text="Note: All tickets reserved on the entered date for the entered movie will be cancelled.",
                      bg='firebrick4',font='fixedsys',fg='grey1',wraplength = 700)
    notelabel.place(x=125, y =225)


#command
#command that un-reserves the tickets
def refundcommand():
    rcmer = movieentryrefund.get()
    rcder = dateentryrefund.get()
    refundsqlquery = "delete from ticketssold where email = %s AND MovieNumber = %s AND dateofshowing = %s"
    refundsql = con1.cursor()
    refundsql.execute(refundsqlquery, (loginsubmitemail, rcmer, rcder))
    con1.commit()
    msgbox.showinfo("Your tickets have been un-reserved!")


#Command
#Command to logout
def logoutcommand():
    msgbox.showinfo("You have successfully logged out.")
    loginsubmitemail = ''
    homescreen.destroy()
    openloginwindow()
mainloop()        
































    
