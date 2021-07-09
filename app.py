import logging
import json

from flask import Flask, request, Blueprint
#from summarizer_t5 import SummarizerT5
from summarizer_pegasus import SummarizerPegasus

main = Blueprint('main', __name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# https://www.codementor.io/@jadianes/building-a-web-service-with-apache-spark-flask-example-app-part2-du1083854


"""@main.route('/summarize/t5', methods=['POST'])
def summarize():
    logger.debug("Summarizing sentences (T5)")

    logger.debug(request.json)

    sentences = request.json['sentences']

    summarized_sentences = text_summarizer_t5.summarize(sentences)

    return json.dumps(summarized_sentences)"""

@main.route('/summarize/pegasus', methods=['POST'])
def summarize():
    logger.debug("Summarizing sentences (Pegasus)")

    logger.debug(request.json)

    sentences = request.json['sentences']

    summarized_sentences = text_summarizer_pegasus.summarize(sentences)

    return json.dumps(summarized_sentences)

def create_app():
    #global text_summarizer_t5
    global text_summarizer_pegasus

    #text_summarizer_t5 = SummarizerT5()
    text_summarizer_pegasus = SummarizerPegasus()

    app = Flask(__name__)
    app.register_blueprint(main)

    return app
