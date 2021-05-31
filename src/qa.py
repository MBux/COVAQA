import streamlit as st
import NLP.qa_api as qa


def app():
    subheader_text = "This page allows you to ask our QA assistant any COVID-19 related question relevant to the" \
                     + " provided categories."
    st.title('COVAQA')
    st.subheader(subheader_text)
    st.write("""*Disclaimer. The responses may not always be 100% accurate; however, all answers are based on CDC and
    WHO data.""")
    QA_form()


def QA_form():
    with st.form("Covid QA Window"):
        st.write("Please select a category below, and then type your question.")
        context = st.selectbox("Select Question Category", qa.CONTEXTS, format_func=lambda context: context['title'])
        question = st.text_input("Type your question here...")
        answer = "Please ask a question."

        if question:
            answer = qa.submit_question(question, context['context'])

        submit = st.form_submit_button("Submit")
        if submit:
            st.write(answer['answer'])
