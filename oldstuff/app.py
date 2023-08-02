from llama_index import SimpleDirectoryReader, GPTVectorStoreIndex, LLMPredictor, ServiceContext
from langchain import OpenAI
import gradio as gr
import os
import openai

os.environ["OPENAI_API_KEY"] = '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'
openai.api_key = os.environ["OPENAI_API_KEY"]

def construct_index(directory_path):
    num_outputs = 512

    llm_predictor = LLMPredictor(llm=OpenAI(temperature=0.7, model_name="text-davinci-003", max_tokens=num_outputs))

    service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor)

    docs = SimpleDirectoryReader(directory_path).load_data()

    index = GPTVectorStoreIndex.from_documents(docs, service_context=service_context)

    index.save_to_disk('index.json')

    return index

def chatbot(input_text):
    index = GPTVectorStoreIndex.load_from_disk('index.json')
    response = index.query(input_text, response_mode="compact")
    return response.response

iface = gr.Interface(fn=chatbot,
                     inputs=gr.inputs.Textbox(lines=7, label="Enter your text"),
                     outputs="text",
                     title="Custom-trained AI Chatbot")

index = construct_index("docs")
iface.launch(share=True)