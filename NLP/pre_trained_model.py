from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline


class CovQAmodel:
    def __init__(self):
        self._model_name = "deepset/roberta-base-squad2-covid"
        # a) Get predictions
        self._nlp = pipeline('question-answering', model=self._model_name, tokenizer=self._model_name)

        # b) Load model & tokenizer
        self._model = AutoModelForQuestionAnswering.from_pretrained(self._model_name)
        self._tokenizer = AutoTokenizer.from_pretrained(self._model_name)

    def get_answer(self, context, question):
        return self._nlp(question=question, context=context)


if __name__ == "__main__":
    model_name = "deepset/roberta-base-squad2-covid"
    nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)
    # context = "COVID-19 Pandemic"
    context = r"""
    Millions of people in the United States have received COVID-19 vaccines since they were authorized for emergency use by FDA. These vaccines have undergone and will continue to undergo the most intensive safety monitoring in U.S. history. This monitoring includes using both established and new safety monitoring systems to make sure that COVID-19 vaccines are safe.
    """
    result = nlp(question="Are the vaccines safe?", context=context)
    print(result)
