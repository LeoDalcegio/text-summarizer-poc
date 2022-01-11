import logging
import json
import nltk

from flask import Flask, request, Blueprint, Response
from flask_cors import CORS

from summarizers.summarizer_bert import SummarizerBert
from summarizers.summarizer_xlnet import SummarizerXLNet
from summarizers.keyword_extractor import KeywordExtractor

main = Blueprint('main', __name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@main.route('/summarize/bert', methods=['POST'])
def summarize_page_bert():
    logger.info("Summarizing sentences (Bert)")

    page_url = request.json['page_url']

    summarized_page, headline = text_summarizer_bert.summarize(page_url)

    summarized_page_with_keywords = keyword_extractor.extract(summarized_page)

    result = {
        'result': summarized_page_with_keywords,
        'headline': headline
    }

    return Response(json.dumps(result), mimetype='application/json')

@main.route('/summarize/xlnet', methods=['POST'])
def summarize_page_xlnet():
    logger.info("Summarizing sentences (XLNet)")

    page_url = request.json['page_url']

    summarized_page, headline = text_summarizer_xlnet.summarize(page_url)

    result = {
        'result': summarized_page,
        'headline': headline
    }

    return Response(json.dumps(result), mimetype='application/json')


def create_app():
    global text_summarizer_bert
    global text_summarizer_xlnet
    global keyword_extractor

    text_summarizer_bert = SummarizerBert()
    text_summarizer_xlnet = SummarizerXLNet()
    keyword_extractor = KeywordExtractor()

    nltk.download('punkt')

    app = Flask(__name__)
    app.register_blueprint(main)

    CORS(app)

    return app
