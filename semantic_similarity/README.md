# Studying the differences between different language models

## Models used

1. TFIDF
2. FastText
3. LASER
4. SentenceBERT
5. Universal Sentence Encoder

## STS benchmark scores attained

| Model         | Score         |
| ------------- | -------------:|
| TFIDF         | 71.4          |
| Fasttext      | 55.3          |
| LASER         | 69.4          |
| SentenceBERT  | 87.4          |
| USE           | 80.1          |

## Semantic Search

Using "search" sentences to find sentences with the same topic from a dictionary

**Search sentences:**

* **Sports:** "Tarasenko has been one of the NHL's leading scorers during his nine-year career, with 214 goals in 507 games."
* **Politics:** "A political system is a framework which defines acceptable political methods within a society."
* **Food:** "This meal has summer dinner written all over it."
* **Science:** "Science is based on research, which is commonly conducted in academic and research institutions as well as in government agencies and companies"
* **Finance:** "Stocks mixed after Powell's inflation plan"

**Sentences:**

* **Sports 1:** "The Vikings defense is already one of the best in the NFL and won’t ask much of Gladney."
* **Sports 2:** "And just like we saw in both games against FC Dallas, Nashville was sharp in the defensive third and in midfield."
* **Politics 1:** "This is election is a choice between President Trump’s strong stance with law and order and Joe Biden’s acquiescence to the anti-police left and siding with rioters."
* **Politics 2:** "Democrats are willing to resume negotiations once Republicans start to take this process seriously."
* **Food 1:** "Made with fresh peaches, sugar, and a topping that bakes like slightly underbaked cookie dough, with crunchy sugar broiled on top."
* **Food 2:** "Is there anything better than a fresh batch of soft chocolate chip cookies? "
* **Science 1:** "Scientists from 17 UK research centres are attempting to answer questions such as how long immunity lasts and why disease severity varies so much."
* **Science 2:** "Decoding goals and movement plans is hard when you don't understand the neural code in which those things are communicated."
* **Finance 1:** "Dow futures up 200 points in overnight trading after the index briefly erases 2020 losses"
* **Finance 2:** "Wednesday’s gains put the S&P 500 up more than 58% since hitting an intraday low on March 23."


### Results

<img src="https://raw.githubusercontent.com/Kurkulis/nlp_notebooks/master/semantic_similarity/images/TFIDF_search.svg">
<img src="https://raw.githubusercontent.com/Kurkulis/nlp_notebooks/master/semantic_similarity/images/FAST_search.svg">
<img src="https://raw.githubusercontent.com/Kurkulis/nlp_notebooks/master/semantic_similarity/images/LASER_search.svg">
<img src="https://raw.githubusercontent.com/Kurkulis/nlp_notebooks/master/semantic_similarity/images/BERT_search.svg">
<img src="https://raw.githubusercontent.com/Kurkulis/nlp_notebooks/master/semantic_similarity/images/USE_search.svg">

## Synonyms/Paraphrases (Different spelling, same meaning)

* **S1_a:** "The need for software developers has gone up by 50% in 5 years"
* **S1_b:** "The demand for programmers has doubled during the last five years"
* **S2_a:** "Personal computers entered the market in 1977"
* **S2_b:** "PCs came into shops in the late seventies"
* **S3_a:** "Symptoms of influenza include fever and nasal congestion."
* **S3_b:** "A stuffy nose and elevated temperature are signs you may have the flu."
* **S4_a:** "He has tons of stuff to throw away."
* **S4_b:** "He needs to get rid of a lot of junk."
* **S5_a:** "Her life spanned years of incredible change for women as they gained more rights than ever before."
* **S5_b:** "She lived through the exciting era of women's liberation."

### Results

<img src="https://raw.githubusercontent.com/Kurkulis/nlp_notebooks/master/semantic_similarity/images/TFIDF_synonym.svg">
<img src="https://raw.githubusercontent.com/Kurkulis/nlp_notebooks/master/semantic_similarity/images/FAST_synonym.svg">
<img src="https://raw.githubusercontent.com/Kurkulis/nlp_notebooks/master/semantic_similarity/images/LASER_synonym.svg">
<img src="https://raw.githubusercontent.com/Kurkulis/nlp_notebooks/master/semantic_similarity/images/BERT_synonym.svg">
<img src="https://raw.githubusercontent.com/Kurkulis/nlp_notebooks/master/semantic_similarity/images/USE_synonym.svg">

## Homonyms (same spelling/words, but different meaning)


* **H1_a:** "She lies on the couch"
* **H1_b:** "She lies to the coach"
* **H2_a:** "Train muscles twice a week"
* **H2_b:** "Train departs twice a week"
* **H3_a:** "I want to book a room"
* **H3_b:** "I want to read a book in a room"
* **H4_a:** "These plants are huge" (plant = flower etc)
* **H4_b:** "Tesla plants are huge" (plant = factory)
* **H5_a:** "I saw a man"
* **H5_b:** "A man has a saw"

### Results

<img src="https://raw.githubusercontent.com/Kurkulis/nlp_notebooks/master/semantic_similarity/images/TFIDF_homonym.svg">
<img src="https://raw.githubusercontent.com/Kurkulis/nlp_notebooks/master/semantic_similarity/images/FAST_homonym.svg">
<img src="https://raw.githubusercontent.com/Kurkulis/nlp_notebooks/master/semantic_similarity/images/LASER_homonym.svg">
<img src="https://raw.githubusercontent.com/Kurkulis/nlp_notebooks/master/semantic_similarity/images/BERT_homonym.svg">
<img src="https://raw.githubusercontent.com/Kurkulis/nlp_notebooks/master/semantic_similarity/images/USE_homonym.svg">

## Sentences contain same words, but have different meaning

The 4 first sentences have the same meaning, but different structure. The 4 last sentences have different meaning, but share words with the first 4 sentences.

**Same meaning:**

1. "She angered me with her inappropriate comments, rumor-spreading, and disrespectfulness at the **formal** dinner **table**."
2. "She made me **angry** when she was rude at dinner."
3. "Her impoliteness, gossiping, and **general** lack of respect at dinner infuriated me."
4. "I was **mad** when she started **spreading** rumors, making inappropriate comments, and disrespecting other guests at our dinner."

**Different meaning:**

5. "The company requires a **formal** dress code during work hours"
6. "President Donald Trump called Joe Biden's running mate Kamala Harris **'angry'** and **'mad'**"
7. "The influenza is **spreading** from **table** surfaces in the restaurants." 
8. "The Coffee Test is one of the tests for human-level Artificial **General** Intelligence."

### Results

<img src="https://raw.githubusercontent.com/Kurkulis/nlp_notebooks/master/semantic_similarity/images/TFIDF_samediff.svg">
<img src="https://raw.githubusercontent.com/Kurkulis/nlp_notebooks/master/semantic_similarity/images/FAST_samediff.svg">
<img src="https://raw.githubusercontent.com/Kurkulis/nlp_notebooks/master/semantic_similarity/images/LASER_samediff.svg">
<img src="https://raw.githubusercontent.com/Kurkulis/nlp_notebooks/master/semantic_similarity/images/BERT_samediff.svg">
<img src="https://raw.githubusercontent.com/Kurkulis/nlp_notebooks/master/semantic_similarity/images/USE_samediff.svg">