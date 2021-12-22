import logging
import json

from flask import Flask, request, Blueprint

from summarizers.summarizer_bert import SummarizerBert

main = Blueprint('main', __name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@main.route('/summarize/page/bert', methods=['POST'])
def summarize_page():
    logger.debug("Summarizing page (Bert)")

    logger.debug(request.json)

    page_url = request.json['page_url']

    summarized_page = text_summarizer_bert.summarize_page(page_url)

    return json.dumps(summarized_page)


@main.route('/summarize/pdf/bert', methods=['POST'])
def summarize_pdf():
    logger.debug("Summarizing pdf (Bert)")

    logger.debug(request.json)

    pdf_url = request.json['pdf_url']

    summarized_pdf = text_summarizer_bert.summarize_pdf(pdf_url)

    return json.dumps(summarized_pdf)


def create_app():
    global text_summarizer_bert

    text_summarizer_bert = SummarizerBert()

    app = Flask(__name__)
    app.register_blueprint(main)

    return app
