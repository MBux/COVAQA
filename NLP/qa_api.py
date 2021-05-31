import pre_trained_model

model = pre_trained_model.CovQAmodel()


def select_context():
    pass


def submit_question():
    question = "How is covid transmitted?"
    context = "COVID-19 spreads when an infected person breathes out droplets and very small particles that contain the virus. These droplets and particles can be breathed in by other people or land on their eyes, noses, or mouth. In some circumstances, they may contaminate surfaces they touch. People who are closer than 6 feet from the infected person are most likely to get infected"
    display_answer(model.get_answer(context=context, question=question))


def display_answer(result):
    print(result)

submit_question()
