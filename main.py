## Integrate our code OpenAI API
import os
from constants import openai_key
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain

from langchain.memory import ConversationBufferMemory
from langchain.chains import SequentialChain

import streamlit as st

os.environ["OPENAI_API_KEY"]=openai_key

# streamlit framework

st.title('Celebrity Search Results')
input_text=st.text_input("Search the topic u want")

# Prompt Templates

first_input_prompt=PromptTemplate(
    input_variables=['name'],
    template="Tell me about celebrity {name}"
)

# Memory

person_memory = ConversationBufferMemory(input_key='name', memory_key='chat_history')
achieve_memory = ConversationBufferMemory(input_key='person', memory_key='chat_history')


## OPENAI LLMS
llm=OpenAI(temperature=0.9)
chain=LLMChain(
    llm=llm,prompt=first_input_prompt,verbose=True,output_key='person',memory=person_memory)

# Prompt Templates

second_input_prompt=PromptTemplate(
    input_variables=['person'],
    template="Mention 5 achievements of {person} "
)

chain2=LLMChain(
    llm=llm,prompt=second_input_prompt,verbose=True,output_key='achieve',memory=achieve_memory)
# Prompt Templates

parent_chain=SequentialChain(
    chains=[chain,chain2],input_variables=['name'],output_variables=['person','achieve'],verbose=True)



if input_text:
    st.write(parent_chain({'name':input_text}))

    with st.expander('Person Name'): 
        st.info(person_memory.buffer)

    with st.expander('Major Events'): 
        st.info(achieve_memory.buffer)