import streamlit as st


def main():
    st.set_page_config(page_title="Chat with multiple PDFs", page_icon=":books:")

    st.header("Chat with multiple PDFs :books:")
    st.text_input("Ask a questions about your documents:")

    with st.sidebar:
        st.subheader("Your documents")
        st.file_uploader(label="Upload your PDFs here and click on 'Process'")
        st.button("Process")



if __name__ == '__main__':
    main()