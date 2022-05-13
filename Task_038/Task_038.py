#38
incoming_text = 'абвлабфбв слияние абвцукв текста алоабвабв выполнено'

def del_words(incoming_text):
    incoming_text = list(filter(lambda x: 'абв' not in x, incoming_text.split()))
    return " ".join(incoming_text)

incoming_text = del_words(incoming_text)
print(incoming_text)