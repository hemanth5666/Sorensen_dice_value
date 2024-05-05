def generate_ngrams(text, n):
    """Generate n-grams from a given text."""
    text = text.replace(" ", "")  # Remove spaces
    return [text[i:i+n] for i in range(len(text) - n + 1)]

def count_common_ngrams(ngrams1, ngrams2):
    """Count common n-grams between two lists of n-grams."""
    common_ngrams_count = 0
    for ngram in ngrams1:
        if ngram in ngrams2:
            common_ngrams_count += 1
    return common_ngrams_count
    
#count_common_ngrams= len(ngrams1.intersection(ngrams2))

def sorenson_dice_coefficient(text1, text2, n):
    """Compute the Sorensen-Dice coefficient between two texts using n-grams."""
    
    ngrams1 = generate_ngrams(text1.lower(), n)
    ngrams2 = generate_ngrams(text2.lower(), n)
    
    common_ngrams_count = count_common_ngrams(ngrams1, ngrams2)
    total_ngrams_count = len(ngrams1) + len(ngrams2)
    
    return 2.0 * common_ngrams_count / total_ngrams_count if total_ngrams_count > 0 else 0

# Example usage:
text1 = "englishyu"
text2 = "english"
n = 2  # Change n-gram size

print("Sørensen-Dice coefficient", sorenson_dice_coefficient(text1, text2, n))
