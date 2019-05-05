from newsapi import NewsApiClient

class News:

    def __init__(self):
        self.newsapi = NewsApiClient(api_key='f86096b6f36d449eb740af2501bb3748')
        title = "The top 3 news headlines I have include: \n<break time=\"500ms\"/>"
        headlines = "\n<break time=\"800ms\"/>".join(self.get_articles())
        self.message = title + headlines


    def get_articles(self):
        top_headlines = self.newsapi.get_top_headlines(q='tech', language='en')
        iterations = 0
        information = []
        for article in top_headlines['articles']:
            iterations = iterations + 1
            if iterations == 1:
                information.append(("- {}" + article['title'] + " By " + article['source']['name']+ '.').format('First, '))
            elif iterations == 2:
                information.append(("- {}" + article['title'] + " By " + article['source']['name']+ '.').format('Next, '))
            elif iterations == 3:
                information.append(("- {}" + article['title'] + " By " + article['source']['name'] + '.').format('Lastly, '))
                break

        return information

