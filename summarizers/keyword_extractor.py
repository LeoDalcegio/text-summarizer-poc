import logging

from keybert import KeyBERT
from helpers.formatters import Formatters

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class KeywordExtractor:
    def __init__(self):
        logger.info("Starting the keyword extractor")

        self.kw_model = KeyBERT()
        self.formatters = Formatters()

        logger.info("Keyword extractor started")

    # right now it only accepts on sentence I THINK, not an array (TODO)
    def extract(self, sentences):
        logger.info("Extracting keywords")

        sentences_with_keywords = []

        for sentence in sentences:
            keywords = self.kw_model.extract_keywords(sentence)

            # pegar a de maior probabilidade por padrão
            # pegar a que é concatenada com outras, ex: é um "municipo brasileiro" do estado, se tiver mais de uma, pegar a que tem a maior probabilidade            

            logger.info(keywords)

            sentences_with_keywords.append({'sentence': sentence, 'keywords': keywords})

        logger.info("Keywords extracted")

        return sentences_with_keywords
