import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader # take text from PDF

def main():
    load_dotenv()


    # streamlit 
    st.set_page_config(page_title="Chat with your PDF", page_icon=":books:")
    st.header("Ask your PDF 💬")
    st.text_input("Ask a questions about your documents:")

    # upload file
    pdf = st.file_uploader("Upload your PDF", type="pdf")
    # extract the text
    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

        st.write(text)


    # with st.sidebar:
    #     st.subheader("Your documents")
    #     st.file_uploader(label="Upload your PDFs here and click on 'Process'")
    #     st.button("Process")



if __name__ == '__main__':
    main()