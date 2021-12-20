import logging
import json

from flask import Flask, request, Blueprint

#from summarizer_t5 import SummarizerT5
#from summarizer_pegasus import SummarizerPegasus
from summarizers.summarizer_bert import SummarizerBert

main = Blueprint('main', __name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# @main.route('/summarize/t5', methods=['POST'])
# def summarize():
#     logger.debug("Summarizing sentences (T5)")

#     logger.debug(request.json)

#     sentences = request.json['sentences']

#     summarized_sentences = text_summarizer_t5.summarize(sentences)

#     return json.dumps(summarized_sentences)

# @main.route('/summarize/pegasus', methods=['POST'])
# def summarize():
#     logger.debug("Summarizing sentences (Pegasus)")

#     logger.debug(request.json)

#     sentences = request.json['sentences']

#     summarized_sentences = text_summarizer_pegasus.summarize(sentences)

#     return json.dumps(summarized_sentences)


@main.route('/summarize/bert', methods=['POST'])
def summarize():
    logger.debug("Summarizing sentence (Bert)")

    logger.debug(request.json)

    page_url = request.json['page_url']

    summarized_page = text_summarizer_bert.summarize(page_url)

    return json.dumps(summarized_page)


def create_app():
    global text_summarizer_t5
    global text_summarizer_pegasus
    global text_summarizer_bert

    #text_summarizer_t5 = SummarizerT5()
    #text_summarizer_pegasus = SummarizerPegasus()
    text_summarizer_bert = SummarizerBert()

    app = Flask(__name__)
    app.register_blueprint(main)

    return app
