# Pseudo-profundity Detection

## In this repository

This is a text classification task predicting the presence of pseudo-profundity. The older classifiers presented below are now removed and newer methods will continue to be updated in the now one compact notebook. An introduction to pseudo-profundity and former findings will follow. In the current notebook are five models: **MLP, SingleLSTM, DoubleLSTM, GRU, 1DConv**. Their validation accuracies and losses are shown as below as well as individual predictions on two example sentences where 1 indicates the absence and 0 the presence of pseudo-profundity.

![Image of accuracies](https://raw.githubusercontent.com/jerrychihchun/pseudo-profunidity/master/figures/accuracy.png)
![Image of losses](https://raw.githubusercontent.com/jerrychihchun/pseudo-profunidity/master/figures/loss.png)

              "You are basic!" "Live, laugh, love!"
      "MLP    0.82606065       0.00919458"
      "1LSTM  0.998755         0.10788591"
      "2LSTM  0.7130968        0.36986926"
      "GRU    0.83411187       0.08223568"
      "1DConv 0.9997211        0.4741875"
      
      
## Definitions:
Pseudo-profound quotes/texts are labelled as **vacuous** (0) and as **mundane** (1) otherwise:

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
  
## Pseudo-profound quote examples

![Image of examples](https://raw.githubusercontent.com/jerrychihchun/pseudo-profunidity/master/figures/quotes.png)

Created by *Online Quote Poster Maker* (https://quotescover.com/) 
  
## Data
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

- Multilayer Perceptrons/MLP (old notebook removed)

- Recurrent Neural Networks/RNN (old notebook removed)

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

Below is the predicted rates of pseudo-profundity based on 16 celebrities' public Instagram captions and 1 computer-generated source by *Bullshit Generator* (http://sebpearce.com/bullshit/). The detection is done based on the training on the entire dataset with the old *MLP + Stemming* model (this means that we also need to stem the inputs for detection). The bullshit quotes aren't as pseudo-profound as expected probably because of its absence in our training data.

![Image of detection](https://raw.githubusercontent.com/jerrychihchun/pseudo-profunidity/master/figures/detection.png)
