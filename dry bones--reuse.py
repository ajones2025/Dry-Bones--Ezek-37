import json
from collections import defaultdict

# Load Hebrew Bible text (assuming JSON format from OSMH or similar dataset)
def load_hebrew_bible(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

# Define weighted word buckets
word_buckets = {

    1:   , #strongest weighting
    2:   , #lower weighting
    3:   , #lowest weighting









}

# Search for passages with clustered words
def find_reuse_passages(bible_text):
    results = []
    
    for book, chapters in bible_text.items():
        for chapter, verses in chapters.items():
            for verse, text in verses.items():
                words = set(text.split())  # Tokenize verse into words
                
                score = sum(
                    weight for weight, bucket in word_buckets.items() if words & bucket
                )
                
                if score > 0:  # If any weighted words are found
                    results.append((score, f"{book} {chapter}:{verse}", text))
    
    # Sort results by highest score first
    results.sort(reverse=True, key=lambda x: x[0])
    return results

# Example usage
# bible_text = load_hebrew_bible("hebrew_bible.json")  # Load your dataset
# matches = find_reuse_passages(bible_text)
# for match in matches[:10]:
#     print(match)




   1: {"רוּחַ", "עֶצֶם", "יָבֵשׁ", "חַיָּה", "בָּשָׂר"}
    2: {"נְבִיא", "נִבָּא", "פָּתַח", "קֶבֶר", "גִּיד" , "תִּקְוָה"},  # Lower weighting (corrected גִּידִים to גִּיד)
    3: {"עַם", "עַל"}  # Lowest weighting
}

#