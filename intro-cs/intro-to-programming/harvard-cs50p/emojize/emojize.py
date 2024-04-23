import emoji

text = input("Input: ").strip()
emojized_text = emoji.emojize(text, language="alias")
print(emojized_text)
