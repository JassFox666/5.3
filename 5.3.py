import string

def generate_hashtag(input_text):
    cleaned_text = input_text.translate(str.maketrans('', '', string.punctuation))
    words = cleaned_text.split()

    hashtag = "#" + "".join(word.capitalize() for word in words)

    if len(hashtag) > 140:
        hashtag = hashtag[:140]

    return hashtag

print(generate_hashtag('Python Community'))
print(generate_hashtag('i like python community!'))
print(generate_hashtag('Should, I. subscribe? Yes!'))