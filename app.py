import logging
import json
import nltk

from flask import Flask, request, Blueprint

from summarizers.summarizer_bert import SummarizerBert

main = Blueprint('main', __name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@main.route('/summarize/bert', methods=['POST'])
def summarize():
    logger.debug("Summarizing sentence (Bert)")

    logger.debug(request.json)

    page_url = request.json['page_url']

    summarized_page = text_summarizer_bert.summarize(page_url)

    return json.dumps(summarized_page)


def create_app():
    global text_summarizer_bert

    text_summarizer_bert = SummarizerBert()

    nltk.download('punkt')

    app = Flask(__name__)
    app.register_blueprint(main)

    return app
