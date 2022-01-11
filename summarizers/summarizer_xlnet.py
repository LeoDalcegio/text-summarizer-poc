import logging

from summarizer import Summarizer, TransformerSummarizer
from helpers.formatters import Formatters
from helpers.scrapper import Scrapper

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class SummarizerXLNet:
    def __init__(self):
        logger.info("Starting the XLNet summarizer")

        self.model = TransformerSummarizer(transformer_type="XLNet",transformer_model_key="xlnet-base-cased")
        self.formatters = Formatters()
        self.scrapper = Scrapper()

        logger.info("XLNet summarizer started")

    # right now it only accepts on sentence I THINK, not an array (TODO)
    def summarize(self, page_url):
        logger.info("Preparing page for summarization")

        article, headline = self.scrapper.scrape_page(page_url)

        logger.info("Summarizing page")

        summary = self.model(article, max_length=300)

        summary_sentences = self.formatters.get_sentences_from_summary(article, summary)

        logger.info("Page summarized")

        return summary_sentences, headline
