from transformers import PegasusTokenizer, PegasusForConditionalGeneration

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class SummarizerPegasus:
    def __init__(self):
        logger.info("Starting the Pegasus summarizer")

        self.model = PegasusForConditionalGeneration.from_pretrained('google/pegasus-xsum')
        self.tokenizer = PegasusTokenizer.from_pretrained('google/pegasus-xsum')


    # right now it only accepts on sentence I THINK, not an array (TODO)
    def summarize(self, sentences):
        logger.info("Summarizing sentences | create datafame")

        inputs = tokenizer([sentences], max_length=1024, return_tensors='pt')
        summary_ids = model.generate(inputs['input_ids'])

        summaries = [tokenizer.decode(g, skip_special_tokens=True, clean_up_tokenization_spaces=False) for g in summary_ids]

        return summaries
