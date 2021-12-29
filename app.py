import logging
import json
import nltk

from flask import Flask, request, Blueprint, Response
from flask_cors import CORS

from summarizers.summarizer_bert import SummarizerBert

main = Blueprint('main', __name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@main.route('/summarize/bert', methods=['POST'])
def summarize():
    logger.debug("Summarizing sentence (Bert)")

    logger.debug(request.json)

    page_url = request.json['page_url']

    summarized_page, headline = text_summarizer_bert.summarize(page_url)

    result = {
        'result': summarized_page,
        'headline': headline
    }

    return Response(json.dumps(result), mimetype='application/json')


def create_app():
    global text_summarizer_bert

    text_summarizer_bert = SummarizerBert()

    nltk.download('punkt')

    app = Flask(__name__)
    app.register_blueprint(main)

    CORS(app)

    return app
