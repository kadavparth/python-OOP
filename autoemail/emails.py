import yagmail
import pandas as pd

xls = pd.read_excel('list.xlsx',header=[1])
# print(xls)
# email = yagmail.SMTP(user='notneeded119@gmail.com',password='atgkiojzvqibtqsc')
interest = []
for i,rows in xls.iterrows():
    # email.send(to='{}'.format(rows['email ']),
    #            subject="Hi There",
    #            contents="Hi this is the body of the email\n Parth",
    #            attachments='design.txt')
    print(rows[["Interest "]])
    interest += [rows['Interest ']]

# print(interest)