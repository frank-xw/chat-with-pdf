import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader # take text from PDF
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS

def main():
    load_dotenv()

    # streamlit 
    st.set_page_config(page_title="Chat with your PDF", page_icon=":books:")
    st.header("Ask your PDF 💬")

    # upload file
    pdf = st.file_uploader("Upload your PDF", type="pdf")
    # extract the text
    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

        # split into chunks
        text_splitter = CharacterTextSplitter( # a class
            separator="\n",
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        chunks = text_splitter.split_text(text)

        # create embedding
        embeddings = OpenAIEmbeddings()
        knowledge_base = FAISS.from_texts(chunks, embeddings)

        # show user input
        user_question = st.text_input("Ask a question about your PDF:")
        if user_question:
            docs = knowledge_base.similarity_search(user_question)
            st.write(docs)

if __name__ == '__main__':
    main()