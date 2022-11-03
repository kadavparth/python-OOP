# api key: c342deea78354a2b9dcb50f1c0ca2932

import yagmail
import pandas as pd
import requests
import datetime

class NewsFeed:

    base_url = 'https://newsapi.org/v2/everything?'

    def __init__(self,interest,from_date,to_date,language):
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language

    def get(self):
        url = self.base_url + 'q={}&' \
                              'from={}&' \
                              'to={}&' \
                              'apiKey=c342deea78354a2b9dcb50f1c0ca2932&' \
                              'language={}'.format(self.interest,self.from_date, self.to_date,self.language)
        response = requests.get(url)
        content = response.json()
        articles = content['articles']

        # title_url_dict = {}
        # i = 0
        # while i < 9:
        #     title = content['articles'][i]['title']
        #     url = content['articles'][i]['url']
        #     title_url_dict[title] = url
        #     i += 1
        #
        # dict = {'Title':[],'Link':[]}
        # for val in title_url_dict.items():
        #     dict["Title"] += [val[0]]
        #     dict["Link"] += [val[1]]

        # title_url_dict1 = pd.DataFrame(dict, columns=["Title", "Link"])

        email_body = ''
        for article in articles:
            email_body = email_body + article['title'] + "\n" + article['url'] + "\n\n"

        return email_body

class Email:

    def __init__(self,filepath):
        self.filepath = filepath

    def send(self):
        interest = []
        xls = pd.read_excel('{}'.format(self.filepath), header=[1])
        email = yagmail.SMTP(user='notneeded119@gmail.com', password='atgkiojzvqibtqsc')

        # once you get interests you can call news feed to get titles and links
        # and store them in a new dataframe

        for i, rows in xls.iterrows():
            # interest += rows['Interest ']
            news_feed = NewsFeed(interest=rows['Interest '],
                            from_date=(datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d'),
                            to_date=datetime.datetime.now().strftime('%Y-%m-%d'),
                            language='en')
            # news_fetch = news.get()[1]
            email.send(to='{}'.format(rows['email ']),
                       subject="Hi There, your {} news for today".format(rows["Interest "]),
                       contents=f"Hi {rows['name ']}\n See what's on about {rows['Interest ']} today.{news_feed.get()}\nParth")


if __name__ == '__main__':
    # news = NewsFeed('nasa','2022-07-03','2022-07-07','en')
    email = Email('list.xlsx')
    email.send()

