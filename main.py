import smtplib

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('justinlite08@gmail.com','POtter@11')
server.sendmail('justinlite08@gmail.com',
                'jatinrastogi08@gmail.com',
                "Hi bro I haven't talked to you in a long time I hope you are doing fine."
                )

