secret_word=[]
for i in range(5):
    user=input("Enter any word")
    secret_word.append(user)
for words in secret_word[:]:
    word=words
    if word == 'z' or word == 'x':
        clean_words=word
        print(clean_words)
        secret_word.remove(clean_words)
        print(secret_word)
