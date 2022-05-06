import gensim
import gensim.downloader
 
google_news_vectors = gensim.downloader.load('word2vec-google-news-300')
 
# Finding Capital of Britain given Capital of France: (Paris - France) + Britain = 
print("Finding Capital of Britain: (Paris - France) + Britain")
capital = google_news_vectors.most_similar(["Paris", "Britain"], ["France"], topn=1)
print(capital)
print()
 
# Finding Capital of India given Capital of Germany: (Berlin - Germany) + India = 
print("Finding Capital of India: (Berlin - Germany) + India")
capital = google_news_vectors.most_similar(["Berlin", "India"], ["Germany"], topn=1)
print(capital)
print()
 
# Finding words similar to BMW
print("5 similar words to BMW:")
words = google_news_vectors.most_similar("BMW", topn=5)
for word in words:
  print(word)
print()
 
# Finding words similar to Beautiful
print("3 similar words to beautiful:")
words = google_news_vectors.most_similar("beautiful", topn=3)
for word in words:
  print(word)
print()
 
# Finding cosine similarity between fight and battle
cosine = google_news_vectors.similarity("fight", "battle")
print("Cosine similarity between fight and battle:", cosine)
print()