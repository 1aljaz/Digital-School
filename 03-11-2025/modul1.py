from collections import Counter

def count_words(text):
    """Vrne stevilo vseh besed v tekstu."""
    return len(text.split())

def reverse_text(text):
    """Vrne obrnjen stavek."""
    return text[::-1]

def most_common_word(text):
    """Vrne najbolj pogosto uporabljeno besedo."""
    words = text.split()
    if not words:
        return None
    return Counter(words).most_common(1)[0][0]

def capitalize_sentences(text):
    """Vrne stavek, ampak da vsako prvo črko v stavku kapitalizira."""
    import re
    sentences = re.split(r'([.!?])', text)
    sentences = [s.strip().capitalize() if i % 2 == 0 else s for i, s in enumerate(sentences)]
    return ''.join(sentences)

def most_common_letter(text):
    """Vrne najpogostejšo črko v besedilu."""
    letters = [c for c in text if c.isalpha()]
    if not letters:
        return None
    return Counter(letters).most_common(1)[0][0]


