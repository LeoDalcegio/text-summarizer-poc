from sparknlp.base import DocumentAssembler
from sparknlp.annotator import T5Transformer
from pyspark.ml import Pipeline
import sparknlp

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class SummarizerT5:
    def __init__(self):
        logger.info("Starting the T5 summarizer")

        self.spark = sparknlp.start()

        document_assembler = DocumentAssembler() \
            .setInputCol("text") \
            .setOutputCol("documents")

        t5 = T5Transformer() \
            .pretrained("t5_small", 'en') \
            .setTask("summarize:")\
            .setMaxOutputLength(200)\
            .setInputCols(["documents"]) \
            .setOutputCol("summaries")

        self.pipeline = Pipeline().setStages([document_assembler, t5])

    def summarize(self, sentences):
        logger.info("Summarizing sentences | create datafame")

        data_df = self.spark.createDataFrame(sentences).toDF("text")

        logger.info("Summarizing sentences | fiting data")

        results = self.pipeline.fit(data_df).transform(data_df)

        logger.info("Summarizing sentences | selecting results")

        summaries = results.select("summaries.result").collect()

        logger.info("Summarizing sentences | returning summaries")

        return summaries
