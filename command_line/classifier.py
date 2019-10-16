import json
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from keras_preprocessing.text import tokenizer_from_json
from tensorflow.keras.preprocessing.sequence import pad_sequences

model_conv = tf.keras.models.load_model('1DConv_model.h5')

tokenizer = Tokenizer()
with open('tokenizer.json') as f:
    data = json.load(f)
    tokenizer = tokenizer_from_json(data)

max_length = 100
trunc_type='post'
padding_type='post'

if __name__== "__main__" :
	predict = True
	print('Enter a sentence to detect pseudo-profundity (q to quit):')
	while predict:
	    text = input()
	    if text == 'q':
	    	break
	    sequences = tokenizer.texts_to_sequences([text])
	    padded = pad_sequences(sequences, maxlen=max_length, padding=padding_type, truncating=trunc_type)
	    print(1-model_conv.predict(padded)[0][0])



