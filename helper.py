from urlextract import URLExtract


def fetch_stats(selected_user, df):
     if selected_user != 'Overall':
      df = df[df['user'] == selected_user]

     num_messages = df.shape[0]
     words = []
     for message in df['message']:
        words.extend(message.split())

     num_media_messages = df[df['message'] == '<Media omitted>\n'].shape[0]
      
     return num_messages, len(words), num_media_messages
    

    !pip install urlextract
from urlextract import URLExtract

extractor = URLExtract()
urls = extractor.find_urls("Let's have URL stackoverflow.com and www.google.com")
urls
links = []
for message in df['message']:
    links.extend(extractor.find_urls(message))