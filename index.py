import smtplib
import pandas
dataframe=pandas.read_csv("CSV FILE")
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("#email","#PASSWORD")
  
for i in range(len(dataframe)):


    message=f"Subject: Android Club Recruitment\nHello {dataframe['NAME'][i]},\n\nThank you for showing interest in The Android Club. We have finished conducting the interviews. It was a pleasure getting to know you.This time we received a large number of applicants and after interviewing all of them carefully, we regret to inform you that you won't be joining the team.\n\nWe wish you success in all your future endeavors. Once again, thank you for your time with us and we encourage you to apply again next time. Hope you would still actively participate in all our events and stay connected to this club.\n\nOur Discord server is open for all so please feel free to come join us there.\n <LINK> \n\nWe would be sharing all our resources over there and all our members are there to help you out at any time.\nHope to see you again.\n\nBest wishes,\nTeam Android Club\nVIT Chennai"
    s.sendmail("#email",dataframe['EMAIL'][i], message.encode('utf-8'))
    
s.quit()