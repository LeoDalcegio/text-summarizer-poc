import logging
import requests

from bs4 import BeautifulSoup
from summarizer import Summarizer
from helpers.formatters import Formatters

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class SummarizerBert:
    def __init__(self):
        logger.info("Starting the Bert summarizer")

        self.model = Summarizer('distilbert-base-uncased')
        self.formatters = Formatters()

        logger.info("Bert summarizer started")

    # right now it only accepts on sentence I THINK, not an array (TODO)
    def summarize(self, page_url):
        logger.info("Preparing page for summarization")

        page = requests.get(page_url).text

        soup = BeautifulSoup(page, "html.parser")

        # Get headline
        headline = soup.find('h1').get_text()

        # Get text from all <p> tags.
        p_tags = soup.find_all('p')

        # Get the text from each of the “p” tags and strip surrounding whitespace.
        p_tags_text = [tag.get_text().strip() for tag in p_tags]

        # Filter out sentences that contain newline characters '\n' or don't contain periods.
        sentence_list = [
            sentence for sentence in p_tags_text if not '\n' in sentence
        ]

        sentence_list = [
            sentence for sentence in sentence_list if '.' in sentence
        ]

        # Combine list items into string.
        article = ' '.join(sentence_list)

        logger.info("Summarizing page")

        summary = self.model(article)

        summary_sentences = self.formatters.get_sentences_from_summary(article, summary)

        logger.info("Page summarized")

        return summary_sentences, headline
