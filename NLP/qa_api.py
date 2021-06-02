from NLP.pre_trained_model import CovQAmodel

MODEL = CovQAmodel()

CONTEXTS = [
    {
        'title': "Vaccines",
        'context': "Over 285 million doses of COVID-19 vaccine have been given in the United States from December 14, 2020, through May 24, 2021. COVID-19 vaccines are safe and effective. COVID-19 vaccines were evaluated in tens of thousands of participants in clinical trials. The vaccines met the Food and Drug Administration’s (FDA) rigorous scientific standards for safety, effectiveness, and manufacturing quality needed to support emergency use authorization (EUA). Millions of people in the United States have received COVID-19 vaccines since they were authorized for emergency use by FDA. These vaccines have undergone and will continue to undergo the most intensive safety monitoring in U.S. history. This monitoring includes using both established and new safety monitoring systems to make sure that COVID-19 vaccines are safe. Serious side effects that could cause a long-term health problem are extremely unlikely following any vaccination, including COVID-19 vaccination. Vaccine monitoring has historically shown that side effects generally happen within six weeks of receiving a vaccine dose. For this reason, the FDA required each of the authorized COVID-19 vaccines to be studied for at least two months (eight weeks) after the final dose. Millions of people have received COVID-19 vaccines, and no long-term side effects have been detected. The Pfizer-BioNTech COVID-19 vaccine has not been approved or licensed by the U.S. Food and Drug Administration (FDA), but has been authorized for emergency use by FDA under an Emergency Use Authorization (EUA) to prevent Coronavirus Disease 2019 (COVID-19) for use in individuals 12 years of age and older. The emergency use of this product is only authorized for the duration of the declaration that circumstances exist justifying the authorization of emergency use of the medical product under Section 564(b)(1) of the FD&C Act unless the declaration is terminated or authorization revoked sooner. The FDA authorization of the Pfizer-BioNTech COVID-19 Vaccine for emergency use is a significant step forward in our fight against this pandemic. As we continue to distribute our vaccine, here are some key facts and answers to common questions. The ingredients are mRNA, lipids ((4-hydroxybutyl)azanediyl)bis(hexane-6,1-diyl)bis(2-hexyldecanoate), 2 [(polyethylene glycol)-2000]-N,N-ditetradecylacetamide, 1,2-Distearoyl-sn-glycero-3-phosphocholine, and cholesterol), potassium chloride, monobasic potassium phosphate, sodium chloride, dibasic sodium phosphate dihydrate, and sucrose. mRNA, delivered to your body's cells by lipid nanoparticles, instructs the cells to generate the spike protein found on the surface of the novel coronavirus that initiates infection.1,2  Instructing cells to generate the spike protein spurs an immune response, including generation of antibodies specific to the SARS-CoV-2 spike protein. mRNA vaccines do not contain any virus particles, meaning they don't contain weakened or dead parts of a virus" + 
       " or bacterium. mRNA is a transient carrier of information that does not integrate into human DNA. mRNA does not enter a cell’s nucleus, which is where our DNA is kept. There is a remote chance that the Pfizer-BioNTech COVID-19 Vaccine could cause a severe allergic reaction. A severe allergic reaction would usually occur within a few minutes to one hour after getting a dose of the Pfizer-BioNTech COVID-19 Vaccine. For this reason, your vaccination provider may ask you to stay at the place where you received your vaccine for monitoring after vaccination. Available data on the Pfizer-BioNTech COVID-19 Vaccine administered to pregnant women are insufficient to inform vaccine-associated risks in pregnancy.1 If you are pregnant, discuss your options with your healthcare provider. It has been suggested that COVID-19 vaccines will cause infertility because of a shared amino acid sequence in the spike protein of SARS-CoV-2 and a placental protein. Although the SARS-CoV-2 spike protein shares an amino acid sequence with a placental protein, the two proteins are immunologically different and distinct. In an animal study in which the Pfizer-BioNTech COVID-19 Vaccine was administered prior to and during gestation, no vaccine-related adverse effects on female fertility, fetal development, or postnatal development were reported.1 If you are pregnant, or planning to become pregnant, discuss your options with your healthcare provider. Pfizer and BioNTech will track participants in our Phase 3 clinical trial for two years following their second dose, in order to document the long-term effectiveness and safety of the vaccine. Our trial is closely monitored by Pfizer and an outside, independent group of experts called a Data Monitoring Committee, or DMC. Trial investigators also monitor participants’ health, and participants in the trial attend regular planned follow-up visits as part of the trial. The safety of patients is and always will be our number one priority. The Moderna vaccine is one of the vaccines currently available in the United States and other countries to protect against COVID-19, which is the disease the novel coronavirus causes. Clinical trials and real world data suggest that the Moderna vaccine effectively and safely protects adults against the virus and its complications. The Moderna vaccine is also known as the mRNA-1273 vaccine. It is one of the vaccines currently available to protect people against COVID-19 Moderna are an American pharmaceutical and biotechnology company who research and develop drugs and vaccines. The Food and Drug Administration (FDA)Trusted Source issued emergency use authorization (EUA) for the vaccine in December 2020. Since then, Canada, the European Union, and the United Kingdom have also authorized its use. he Moderna vaccine is an mRNA vaccine. These are new typesTrusted Source of vaccines that work differently from other vaccines. mRNA vaccines deliver the genetic code to our cells to make a protein" +
    "that triggers the body’s immune response. The body then produces antibodies and develops longer lasting immunity that can fight off the SARS-CoV-2 virus should it enter the body at a later stage. A large 2020 trial, involving 30,420 adult volunteers at various sites across the U.S., reports that the Moderna vaccine has a 94.1% efficacy rate against COVID-19, including against severe disease. The average age of participants was 51.4 years, with 24.8% aged 65 years or older. Just over half of the participants (52.7%) were male. The majority of participants were white (79.2%), with racial and ethnic demographics generally representative of U.S. demographics (10.2% Black or African American and 20.5% Hispanic or Latino). Another study, which has yet to undergo peer review, investigated the real world effectiveness of the Moderna and Pfizer vaccines. The researchers compared 31,069 vaccinated individuals (having received at least one dose of either vaccine) with 31,069 unvaccinated people. The findings suggest that getting both doses of either COVID-19 vaccine was 88.7% effective in preventing infection. Those who did get COVID-19 following vaccination had significantly lower 14-day hospital admission rates than unvaccinated people of a similar demographic."
    },
    {
        'title': "Transmission",
        'context': "COVID-19 spreads when an infected person breathes out droplets and very small particles that contain the virus. These droplets and particles can be breathed in by other people or land on their eyes, noses, or mouth. In some circumstances, they may contaminate surfaces they touch. People who are closer than 6 feet from the infected person are most likely to get infected. Anyone infected with COVID-19 can spread it, even if they do NOT have symptoms. Cases of reinfection with COVID-19 have been reported, but remain rare. CDC is actively working to learn more about reinfection to inform public health action. COVID-19 can spread from people to animals in some situations. Pet cats and dogs can sometimes become infected after close contact with people with COVID-19. Learn what you should do if you have pets. SARS-CoV-2, the virus that causes COVID-19, is an enveloped virus, meaning that its genetic material is packed inside an outer layer (envelope) of proteins and lipids. The envelope contains structures (spike proteins) for attaching to human cells during infection. The envelope for SARS-CoV-2, as with other enveloped respiratory viruses, is labile and can degrade quickly upon contact with surfactants contained in cleaning agents and under environmental conditions. Because of the many factors affecting the efficiency of environmental transmission, the relative risk of fomite transmission of SARS-CoV-2 is considered low compared with direct contact, droplet transmission, or airborne transmission. However, it is not clear what proportion of SARS-CoV-2 infections are acquired through surface transmission. There have been few reports of COVID-19 cases potentially attributed to fomite transmission. Infections can often be attributed to multiple transmission pathways. Fomite transmission is difficult to prove definitively, in part because respiratory transmission from asymptomatic people cannot be ruled out. Case reports indicate that SARS-CoV-2 is transmitted between people by touching surfaces an ill person has recently coughed or sneezed on, and then directly touching the mouth, nose, or eyes. Hand hygiene is a barrier to fomite transmission and has been associated with lower risk of infection. Quantitative microbial risk assessment (QMRA) studies have been conducted to understand and characterize the relative risk of SARS-CoV-2 fomite transmission and evaluate the need for and effectiveness of prevention measures to reduce risk. Findings of these studies suggest that the risk of SARS-CoV-2 infection via the fomite transmission route is low, and generally less than 1 in 10,000, which means that each contact with a contaminated surface has less than a 1 in 10,000 chance of causing an infection. Some studies estimated exposure risks primarily using outdoor environmental SARS-CoV-2 RNA quantification data. They noted that their QMRA estimates are subject to uncertainty that can be reduced with additional data to improve the accuracy" + 
        " and precision of information that is entered into the models. Concentrations of infectious SARS-CoV-2 on outdoor surfaces could be expected to be lower than indoor surfaces because of air dilution and movement, as well as harsher environmental conditions, such as sunlight. One QMRA study also evaluated the effectiveness of prevention measures that reduce the risk of fomite transmission and found that hand hygiene could substantially reduce the risk of SARS-CoV-2 transmission from contaminated surfaces, while surface disinfection once- or twice-per-day had little impact on reducing estimated risks. Numerous researchers have studied how long SARS-CoV-2 can survive on a variety of porous and non-porous surfaces. On porous surfaces, studies report inability to detect viable virus within minutes to hours; on non-porous surfaces, viable virus can be detected for days to weeks. The apparent, relatively faster inactivation of SARS-CoV-2 on porous compared with non-porous surfaces might be attributable to capillary action within pores and faster aerosol droplet evaporation. Data from surface survival studies indicate that a 99% reduction in infectious SARS-CoV-2 and other coronaviruses can be expected under typical indoor environmental conditions within 3 days (72 hours) on common non-porous surfaces like stainless steel, plastic, and glass. However, experimental conditions on both porous and non-porous surfaces do not necessarily reflect real-world conditions, such as initial virus amount (e.g., viral load in respiratory droplets) and factors that can remove or degrade the virus, such as ventilation and changing environmental conditions. They also do not account for inefficiencies in transfer of the virus between surfaces to hands and from hands to mouth, nose, and eyes. In fact, laboratory studies try to optimize the recovery of viruses from surfaces (e.g., purposefully swabbing the surface multiple times or soaking the contaminated surface in viral transport medium before swabbing). When accounting for both surface survival data and real-world transmission factors, the risk of fomite transmission after a person with COVID-19 has been in an indoor space is minor after 3 days (72 hours), regardless of when it was last cleaned. Both cleaning (use of soap or detergent) and disinfection (use of a product or process designed to inactivate SARS-CoV-2) can reduce the risk of fomite transmission. Cleaning reduces the amount of soil (e.g., dirt, microbes and other organic agents, and chemicals) on surfaces, but efficacy varies by the type of cleaner used, cleaning procedure, and how well the cleaning is performed. No reported studies have investigated the efficacy of surface cleaning (with soap or detergent not containing a registered disinfectant) for reducing concentrations of SARS-CoV-2 on non-porous surfaces. From studies of cleaning focused on other microbes, a 90–99.9% reduction of microbe levels could be possible depending on the cleaning" +
        "method and the surface being cleaned. In addition to physical removal of SARS-CoV-2 and other microbes, surface cleaning can be expected to degrade the virus. Surfactants in cleaners can disrupt and damage the membrane of an enveloped virus like SARS-CoV-2. To substantially inactivate SARS-CoV-2 on surfaces, the surface must be treated with a disinfectant product registered with the Environmental Protection Agency’s (EPA’s) or technology that has been shown to be effective against the virus. Disinfectant products might also contain cleaning agents, so they are designed to clean by both removing soil and inactivating microbes. Cleaners and disinfectants should be used safely, following the manufacturer guidance. There have been increases in poisonings and injuries from unsafe use of cleaners and disinfectants since the start of the COVID-19 pandemic. Some types of disinfection applications, particularly those including fogging or misting, are neither safe nor effective for inactivating the virus unless properly used. Surface disinfection has been shown to be effective for preventing secondary transmission of SARS-CoV-2 between an infected person and other people within households. However, there is little scientific support for routine use of disinfectants in community settings, whether indoor or outdoor, to prevent SARS-CoV-2 transmission from fomites. In public spaces and community settings, available epidemiological data and QMRA studies indicate that the risk of SARS-CoV-2 transmission from fomites is low—compared with risks from direct contact, droplet transmission or airborne transmission. outine cleaning performed effectively with soap or detergent, at least once per day, can substantially reduce virus levels on surfaces. When focused on high-touch surfaces, cleaning with soap or detergent should be enough to further reduce the relatively low transmission risk from fomites in situations when there has not been a suspected or confirmed case of COVID-19 indoors. In situations when there has been a suspected or confirmed case of COVID-19 indoors within the last 24 hours, the presence of infectious virus on surfaces is more likely and therefore high-touch surfaces should be disinfected. When a person with suspected or confirmed COVID-19 has been indoors, virus can remain suspended in the air for minutes to hours. The length of time virus remains suspended and is infectious depends on numerous factors, including viral load in respiratory droplets or in small particles, disturbance of air and surfaces, ventilation, temperature, and humidity. Wearing masks consistently and correctly can substantially reduce the amount of virus indoors, including the amount of virus that lands on surfaces. Based on limited epidemiologic and experimental data, the risk of infection from entering a space where a person with COVID-19 has been is low after 24 hours. During the first 24 hours, the risk can be reduced by increasing ventilation and" +
        " waiting as long as possible before entering the space (at least several hours, based on documented airborne transmission cases), and using personal protective equipment (including any protection needed for the cleaning and disinfection products) to reduce risk. Certain techniques can improve the fit and filtration effectiveness of masks. After a person with suspected or confirmed COVID-19 has been in an indoor space, the risk of fomite transmission from any surfaces is minor after 3 days (72 hours). Researchers have found that 99% reduction in infectious SARS-CoV-2 on non-porous surfaces can occur within 3 days. In indoor settings, risks can be reduced by wearing masks (which reduces droplets that can be deposited on surfaces), routine cleaning, and consistent hand hygiene. People can be infected with SARS-CoV-2 through contact with surfaces. However, based on available epidemiological data and studies of environmental transmission factors, surface transmission is not the main route by which SARS-CoV-2 spreads, and the risk is considered to be low. The principal mode by which people are infected with SARS-CoV-2 is through exposure to respiratory droplets carrying infectious virus. In most situations, cleaning surfaces using soap or detergent, and not disinfecting, is enough to reduce risk. Disinfection is recommended in indoor community settings where there has been a suspected or confirmed case of COVID-19 within the last 24 hours. The risk of fomite transmission can be reduced by wearing masks consistently and correctly, practicing hand hygiene, cleaning, and taking other measures to maintain healthy facilities."
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
