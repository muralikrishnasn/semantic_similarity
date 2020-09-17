# 4 sentences with same meaning, but different structure and 4 sentences with same words as the first ones, but different meaning.
same = ["She angered me with her inappropriate comments, rumor-spreading, and disrespectfulness at the formal dinner table.", "She made me angry when she was rude at dinner.",
        "Her impoliteness, gossiping, and general lack of respect at dinner infuriated me.", "I was mad when she started spreading rumors, making inappropriate comments, and disrespecting other guests at our dinner."]

different = ["The company requires a formal dress code during work hours", "President Donald Trump called Joe Biden's running mate Kamala Harris 'angry' and 'mad'.",
             "The influenza is spreading from table surfaces in the restaurants.", "The Coffee Test is one of the tests for human-level Artificial General Intelligence."]

same_diff = ["She angered me with her inappropriate comments, rumor-spreading, and disrespectfulness at the formal dinner table.", "She made me angry when she was rude at dinner.",
             "Her impoliteness, gossiping, and general lack of respect at dinner infuriated me.", "I was mad when she started spreading rumors, making inappropriate comments, and disrespecting other guests at our dinner.", "The company requires a formal dress code during work hours", "President Donald Trump called Joe Biden's running mate Kamala Harris 'angry' and 'mad'.",
             "The influenza is spreading from table surfaces in the restaurants.", "The Coffee Test is one of the tests for human-level Artificial General Intelligence."]

same_diff_cat = ["SAME_1", "SAME_2", "SAME_3",
                 "SAME_4", "DIFF_1", "DIFF_2", "DIFF_3", "DIFF_4"]


# -----------------------------------------------------------------


# Synonyms/Paraphrases (Different spelling, same meaning)
synonyms = ["The need for software developers has gone up by 50% in 5 years", "The demand for programmers has doubled during the last five years", "Personal computers entered the market in 1977", "PCs came into shops in the late seventies", "Symptoms of influenza include fever and nasal congestion.",
            "A stuffy nose and elevated temperature are signs you may have the flu.", "He has tons of stuff to throw away.", "He needs to get rid of a lot of junk.", "Her life spanned years of incredible change for women as they gained more rights than ever before.", "She lived through the exciting era of women's liberation."]

synonym_cat = ["S1_a", "S1_b", "S2_a", "S2_b",
               "S3_a", "S3_b", "S4_a", "S4_b", "S5_a", "S5_b"]


# -----------------------------------------------------------------


# Homonyms (same spelling/words, but different meaning)
homonyms = ["She lies on the couch", "She lies to the coach", "Train muscles twice a week", "Train departs twice a week",
            "I want to book a room", "I want to read a book in a room", "These plants are huge", "Tesla plants are huge", "I saw a man", "A man has a saw"]

homonym_cat = ["H1_a", "H1_b", "H2_a", "H2_b",
               "H3_a", "H3_b", "H4_a", "H4_b", "H5_a", "H5_b"]

# -----------------------------------------------------------------


# Semantic search

# Search sentences:
search_sentences = ["Tarasenko has been one of the NHL's leading scorers during his nine-year career, with 214 goals in 507 games.", "A political system is a framework which defines acceptable political methods within a society.",
                    "This meal has summer dinner written all over it.", "Science is based on research, which is commonly conducted in academic and research institutions as well as in government agencies and companies", "Stocks mixed after Powell's inflation plan"]

search_cat = ["SPORTS", "POLITICS", "FOOD", "SCIENCE", "FINANCE"]

# Sentences to search from:
sentences = ["The Vikings defense is already one of the best in the NFL and won’t ask much of Gladney.", "And just like we saw in both games against FC Dallas, Nashville was sharp in the defensive third and in midfield.", "This is election is a choice between President Trump’s strong stance with law and order and Joe Biden’s acquiescence to the anti-police left and siding with rioters.", "Democrats are willing to resume negotiations once Republicans start to take this process seriously.", "Made with fresh peaches, sugar, and a topping that bakes like slightly underbaked cookie dough, with crunchy sugar broiled on top.",
             "Is there anything better than a fresh batch of soft chocolate chip cookies?", "Scientists from 17 UK research centres are attempting to answer questions such as how long immunity lasts and why disease severity varies so much.", "Decoding goals and movement plans is hard when you don't understand the neural code in which those things are communicated.", "Dow futures up 200 points in overnight trading after the index briefly erases 2020 losses", "Wednesday’s gains put the S&P 500 up more than 58% since hitting an intraday low on March 23."]

sentence_cat = ["SPORTS_1", "SPORTS_2", "POLITICS_1", "POLITICS_2",
                "FOOD_1", "FOOD_2", "SCIENCE_1", "SCIENCE_2", "FINANCE_1", "FINANCE_2"]
