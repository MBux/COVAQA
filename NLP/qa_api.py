from NLP.pre_trained_model import CovQAmodel

MODEL = CovQAmodel()

CONTEXTS = [
    {
        'title': "Vaccines",
        'context': "Over 285 million doses of COVID-19 vaccine have been given in the United States from December 14, 2020, through May 24, 2021. COVID-19 vaccines are safe and effective. COVID-19 vaccines were evaluated in tens of thousands of participants in clinical trials. The vaccines met the Food and Drug Administration’s (FDA) rigorous scientific standards for safety, effectiveness, and manufacturing quality needed to support emergency use authorization (EUA). Millions of people in the United States have received COVID-19 vaccines since they were authorized for emergency use by FDA. These vaccines have undergone and will continue to undergo the most intensive safety monitoring in U.S. history. This monitoring includes using both established and new safety monitoring systems to make sure that COVID-19 vaccines are safe. Serious side effects that could cause a long-term health problem are extremely unlikely following any vaccination, including COVID-19 vaccination. Vaccine monitoring has historically shown that side effects generally happen within six weeks of receiving a vaccine dose. For this reason, the FDA required each of the authorized COVID-19 vaccines to be studied for at least two months (eight weeks) after the final dose. Millions of people have received COVID-19 vaccines, and no long-term side effects have been detected."
    },
    {
        'title': "Transmission",
        'context': "COVID-19 spreads when an infected person breathes out droplets and very small particles that contain the virus. These droplets and particles can be breathed in by other people or land on their eyes, noses, or mouth. In some circumstances, they may contaminate surfaces they touch. People who are closer than 6 feet from the infected person are most likely to get infected. Anyone infected with COVID-19 can spread it, even if they do NOT have symptoms. Cases of reinfection with COVID-19 have been reported, but remain rare. CDC is actively working to learn more about reinfection to inform public health action. COVID-19 can spread from people to animals in some situations. Pet cats and dogs can sometimes become infected after close contact with people with COVID-19. Learn what you should do if you have pets."
    },
    {
        'title': "Variants",
        'context': "Viruses constantly change through mutation, and new variants of a virus are expected to occur. Sometimes new variants emerge and disappear. Other times, new variants persist. Multiple variants of the virus that causes COVID-19 have been documented in the United States and globally during this pandemic. Viruses constantly change and become more diverse. Scientists monitor these changes, including changes to the spikes on the surface of the virus. By carefully studying viruses, scientists can learn how changes to the virus might affect how it spreads and how sick people will get from it. If you think about a virus like a tree growing and branching out; each branch on the tree is slightly different than the others. By comparing the branches, scientists can label them according to the differences. These small differences, or variants, have been studied and identified since the beginning of the pandemic. Some variations allow the virus to spread more easily or make it resistant to treatments or vaccines. Those variants must be monitored more carefully. We are monitoring multiple variants; currently there are five notable variants in the United States. B.1.1.7: This variant was first detected in the United States in December 2020. It was initially detected in the United Kingdom. B.1.351: This variant was first detected in the United States at the end of January 2021. It was initially detected in South Africa in December 2020. P.1: This variant was first detected in the United States in January 2021. P.1 was initially identified in travelers from Brazil, who were tested during routine screening at an airport in Japan, in early January. B.1.427 and B.1.429: These two variants were first identified in California in February 2021. These variants seem to spread more easily and quickly than other variants, which may lead to more cases of COVID-19. An increase in the number of cases will put more strain on healthcare resources, lead to more hospitalizations, and potentially more deaths. So far, studies suggest that the current authorized vaccines work on the circulating variants. Scientists will continue to study these and other variants. CDC tracks multiple variants circulating in the United States and provides an estimate of how common they are in the nation and at the regional level. This data can change over time as more information is available. Based on current data, variant B.1.1.7 is the most common variant across the country."
    }
]


def select_context():
    pass


def submit_question(question, context):
    answer = display_answer(MODEL.get_answer(context=context, question=question))
    return answer


def display_answer(result):
    return result
