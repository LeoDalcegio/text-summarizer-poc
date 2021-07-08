import logging
import json

from flask import Flask, request, Blueprint
from summarizer import T5Summarizer

main = Blueprint('main', __name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# https://www.codementor.io/@jadianes/building-a-web-service-with-apache-spark-flask-example-app-part2-du1083854


@main.route('/summarize', methods=['POST'])
def summarize(sentences):
    logger.debug("Summarizing sentences")

    summarized_sentences = t5_text_summarizer.summarize(sentences)

    return json.dumps(summarized_sentences)


def create_app():
    global t5_text_summarizer

    t5_text_summarizer = T5Summarizer()

    app = Flask(__name__)
    app.register_blueprint(main)

    return app
