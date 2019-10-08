# Pseudo-profundity Detection

This is a text classification task detecting the presence of pseudo-profundity. Pseudo-profound quotes/texts are labelled as **vacuous** and as **mundane** otherwise:

  - *MUNDANE*: “If there is no wall, there is no deal!”
  - *VACUOUS*: “A wet man doesn’t fear the rain.”

- Psycology:  
  - **pseudo-profound quotes**:
  “consists of seemingly impressive assertions that are presented as true and meaningful but
  are actually vacuous (Pennycook et al., 2015, p. 549)”
- Philosophy & Literature:
  - **humbug** (Black, 1982):
  “deceptive misrepresentation, short of lying, especially by pretentious
  word or deed, of somebody’s own thoughts, feelings, or attitudes (Max Black)”
  - **kitsch** (Botz-Bornstein, 2015, 2017)
  - **bullshit** (Frankfurt, 2009)
  
## Pseudo-profound quote examples:

![Image of examples](https://raw.githubusercontent.com/jerrychihchun/pseudo-profunidity/master/figures/quotes.png)

Created by *Online Quote Poster Maker* (https://quotescover.com/) 
  
## Data:
- Instagram Captions

![Image of gram](https://raw.githubusercontent.com/jerrychihchun/pseudo-profunidity/master/figures/gram.png)

Wordcloud for **vacuous** Instagram captions

- Wikiquotes

![Image of wiki](https://raw.githubusercontent.com/jerrychihchun/pseudo-profunidity/master/figures/wiki.png)

Wordcloud for **mundane** Wikiquotes
- Goodreads

![Image of inspiration](https://raw.githubusercontent.com/jerrychihchun/pseudo-profunidity/master/figures/inspiration.png)

Wordcloud for **vacuous** quotes

![Image of science](https://raw.githubusercontent.com/jerrychihchun/pseudo-profunidity/master/figures/science.png)

Wordcloud for **mundane** quotes

## Inputs:

- tokens (using TweetTokenizer)
- stems (using Snowball stemer)
- lemmas (using WordNet lemmatizer)

## Models:

- Multilayer Perceptrons/MLP (Credits: Grokking Deep Learning by Andrew Trask)

- Recurrent Neural Networks/RNN (Credits: Sentiment Prediction with Mat Leonard)

## Results

The RNN models outperform the MLP counterparts to a small extent. In addition, morphological normalizations, stemming in particular, prove to be effective in improving the performances. That is, stems alone contain the major (non-)pseudo-profound senses. Affixes, derivational and inflectional alike, are not as informative.

![Image of results](https://raw.githubusercontent.com/jerrychihchun/pseudo-profunidity/master/figures/result.png)

## Top 40 Vacuous Words (least mundane)

![Image of topvacuous](https://raw.githubusercontent.com/jerrychihchun/pseudo-profunidity/master/figures/topvacuous.png)

## Word Similarity

The most and least similar words to the buzzword *tranquility* in the space of pseudo-profundity

![Image of tran](https://raw.githubusercontent.com/jerrychihchun/pseudo-profunidity/master/figures/tranquility.png)
![Image of tran_dis](https://raw.githubusercontent.com/jerrychihchun/pseudo-profunidity/master/figures/tranquility_dis.png)

## Detection

Below is the detected rates of pseudo-profundity based on 16 celebrities' public Instagram captions and 1 computer-generated source by *Bullshit Generator* (http://sebpearce.com/bullshit/). The detection is done based on the training on the entire dataset with the *MLP + Stemming* model (this means that we also need to stem the inputs for detection). The bullshit quotes aren't as pseudo-profound as expected probably because of its absence to our training data. The detection method is found in the file **MLP_demo.ipynb** with the function name *eval* in the training class.

![Image of detection](https://raw.githubusercontent.com/jerrychihchun/pseudo-profunidity/master/figures/detection.png)
