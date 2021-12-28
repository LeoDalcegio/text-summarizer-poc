import nltk
import time

class Formatters:
    def format_summary_from_text(self, original_text, summary):
        # Tokenize original text and summary into sentences 
        original_text__sentences = [sentence for sentence in nltk.sent_tokenize(original_text)]

        summary_sentences = [sentence for sentence in nltk.sent_tokenize(summary)]
        
        formatted = []

        text_to_format = ''

        for sentence in original_text__sentences:
            if sentence in summary_sentences:
                text_to_format += ' ' + sentence
            else:
                if len(text_to_format):
                    formatted.append(text_to_format.strip())
                
                text_to_format = ''
        
        if len(text_to_format):
            formatted.append(text_to_format)

        return formatted        
