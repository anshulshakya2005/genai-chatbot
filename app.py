import streamlit as st
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
 
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","you are an helpful assistent , response on the user's queries in a detailed manner."),
        ("user","question:{question}")
    ]
)
def generate_res(question,llm,temperature,api_key,max_tokens):
    
    llm = ChatGroq(model=llm,temperature=temperature,max_tokens=max_tokens,groq_api_key = api_key)
    outputparser = StrOutputParser()
    chain = prompt|llm|outputparser
    ans = chain.invoke({"question":question})
    return ans

st.title("enhanced q and a chatbot with groq")
st.sidebar.title("setting")
api_key = st.sidebar.text_input("enter your api_key here",type="password")
llm = st.sidebar.selectbox("select an groq model ",["openai/gpt-oss-120b","openai/gpt-oss-20b","qwen/qwen3.8-27b"])
temperature = st.sidebar.slider("temperature",max_value=1.0,min_value=0.0,value=0.7)
max_tokens = st.sidebar.slider(
    "max_tokens",
    min_value=50,
    max_value=2000,
    value=150
)
st.write("go ahead and ask any question")
user_input= st.text_input("you:")
if user_input:
    response = generate_res(user_input,llm,temperature,api_key,max_tokens)
    st.write(response)
else:
    st.write("provide and query please.")