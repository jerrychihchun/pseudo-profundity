# Pseudo-profundity Detection

This is a text classification task detecting the presence of pseudo-profundity, i.e. its detection. Pseudo-profound quotes are labelled as **vacuous** and as **mundane** otherwise.

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

RNN models outperform the MLP counterparts to a small extent. In addition, morphological normalizations, stemming in particular prove to be effective in detecting pseudo-profundity. I.e., stems alone may contribute the majority of pseudo-profound senses. Affixes, derivational and inflectional alike, are not as informative.

![Image of results](https://raw.githubusercontent.com/jerrychihchun/pseudo-profunidity/master/figures/result.png)
