# Pseudo-profundity Detection

This is a text classification task detecting the presence of pseudo-profundity. Pseudo-profound quotes are labelled as **vacuous** and as **mundane** otherwise.

## Pseudo-profound quote examples:

![Image of examples](https://raw.githubusercontent.com/jerrychihchun/pseudo-profunidity/master/figures/quotes.png)

Created by *Online Quote Poster Maker* (https://quotescover.com/) 
  
## Data:
- Instagram Captions

![Image of grams](https://raw.githubusercontent.com/jerrychihchun/pseudo-profunidity/master/figures/gram.png)

Wordcloud for **vacuous** Instagram captions

- Wikiquotes

![Image of grams](https://raw.githubusercontent.com/jerrychihchun/pseudo-profunidity/master/figures/wiki.png)

Wordcloud for **mundane** Wikiquotes
- Goodreads

![Image of grams](https://raw.githubusercontent.com/jerrychihchun/pseudo-profunidity/master/figures/inspiration.png)

Wordcloud for **vacuous** quotes

![Image of grams](https://raw.githubusercontent.com/jerrychihchun/pseudo-profunidity/master/figures/science.png)

Wordcloud for **mundane** quotes

## Inputs:

  - tokens (using TweetTokenizer)
  - stems (using Snowball stemer)
  - lemmas (using WordNet lemmatizer)

## Models:

- Multilayer Perceptrons (MLP)

- Recurrent Neural Networks (RNN)  
  
## Results

The RNN models outperform the MLP counterparts to a small extent. In addition, morphological normalizations, stemming in particular, prove to be effective in improving the performances. That is, stems alone contain the major (non-)pseudo-profound senses. Affixes, derivational and inflectional alike, are not as informative.

![Image of results](https://raw.githubusercontent.com/jerrychihchun/pseudo-profunidity/master/figures/result.png)

## Detection

Below is the detected rates of pseudo-profundity based on 16 celebrities' public Instagram captions and 1 computer-generated source by *Bullshit Generator* (http://sebpearce.com/bullshit/). The detection is done based on the training on the entire dataset with the *MLP + Stemming* model (this means that we also need to stem the inputs for detection). The bullshit quotes aren't as pseudo-profound as expected probably because of its absence to our training data. The detection method is found in the file **MLP_demo.ipynb** with the function name *eval* in the training class.

![Image of detection](https://raw.githubusercontent.com/jerrychihchun/pseudo-profunidity/master/figures/detection.png)
