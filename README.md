# Pseudo-profundity Detection

This is a text classification task detecting the presence or absence of pseudo-profundity, i.e. its detection. Pseudo-profound quotes are labelled as **vacuous** and as **mundane** otherwise.

## Pseudo-profound quote examples:

![Image of examples](https://raw.githubusercontent.com/jerrychihchun/pseudo-profunidity/master/figures/quotes.png)
Created by *Online Quote Poster Maker* (https://quotescover.com/) 

## Models:
- Multilayer Perceptrons (MLP)
  Input types:
  - tokens (using TweetTokenizer)
  - stems (using Snowball stemer)
  - lemmas (using WordNet lemmatizer)
- Recurrent Neural Networks (RNN)
  Input types:
  - tokens (using TweetTokenizer)
  - stems (using Snowball stemer)
  - lemmas (using WordNet lemmatizer)
  
## Data Sources:
- Instagram Captions
- Wikiquotes
- Goodreads

## Results
