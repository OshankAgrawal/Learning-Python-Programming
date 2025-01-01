sentence = input("Enter any string")

def even_length_word(sentence):
    word = sentence.split()

    for i in word:
        if len(i)%2 == 0:
            print(i)

print("Even-length words in the string:")
even_length_word(sentence)
