def convert(text):
    emoticons = {":)": "🙂", ":(": "🙁"}
    return emoticons.get(text, text)

def main():
    text = input("What can I do for you? ")
    print(" ".join(convert(word) for word in text.split()))

main()