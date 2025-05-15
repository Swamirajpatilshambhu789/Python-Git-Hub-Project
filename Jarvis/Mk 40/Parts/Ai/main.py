import google.generativeai as genai


def text_to_sentences(text):
    # Split the text by '.' and strip whitespace
    sentences = [sentence.strip() for sentence in text.split('.') if sentence.strip()]
    return sentences

# Example usage
# essay = """This is the first sentence. Here is another one. This is the last sentence."""
# sentences = text_to_sentences(essay)

# Output the array of sentences
# print(sentences)


def ResponceSender(req):
    genai.configure(api_key="AIzaSyDd3i4FzfVJ0oHMkYLOHoApHl3Ao8ZXvjA")
    model = genai.GenerativeModel('gemini-2.5-pro-exp-03-25')
    response = model.generate_content(req)
    return response.text

a = input(":")

res = ResponceSender(a)
print("Print the whole res")
print(res)

if "." in res:
    print("Printing the cut res")
    breakingpoint = text_to_sentences(res)
    # print(breakingpoint)

else:
    print(res)