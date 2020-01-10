import spacy
stopWordList = ["ourselves", "hers", "between", "yourself", "but", "again", "there", "about", "once", "during", "out", "very", "having", "with", "they", "own", "an", "be", "some", "for", "do", "its", "yours", "such", "into", "of", "most", "itself", "other", "off", "is", "s", "am", "or", "who", "as", "from", "him", "each", "the", "themselves", "until", "below", "are", "we", "these", "your", "his", "through", "don", "nor", "me", "were", "her", "more", "himself", "this", "down", "should", "our", "their", "while", "above", "both", "up", "to", "ours", "had", "she", "all", "no", "when", "at", "any", "before", "them", "same", "and", "been", "have", "in", "will", "on", "does", "yourselves", "then", "that", "because", "what", "over", "why", "so", "can", "did", "not", "now", "under", "he", "you", "herself", "has", "just", "where", "too", "only", "myself", "which", "those", "i", "after", "few", "whom", "t", "being", "if", "theirs", "my", "against", "a", "by", "doing", "it", "how", "further", "was", "here", "than", "something", "someone", "anyone", "everything", "whereís", "anything", "youu", "us"]

nlp = spacy.load("en_core_web_sm")
doc = nlp("An interval-based temporal logic is introduced, together with a computationally effective reasoning algorithm based on constraint propagation. This system is notable in offering a delicate balance between expressive power and the efficiency of its deductive engine. A notion of reference intervals is introduced which captures the temporal hierarchy implicit in many domains, and which can be used to precisely control the amount of deduction performed automatically by the system. Examples are provided for a database containing historical data, a database used for modeling processes and process interaction, and a database for an interactive system where the present moment is continually being updated. ")

keyword = set()
for chunk in doc.noun_chunks:
    if (chunk.text.lower() not in stopWordList):
        keyword.add(chunk.text)

print(keyword)