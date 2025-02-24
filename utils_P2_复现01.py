import os

from langchain_core.output_parsers import PydanticOutputParser
from prompt_template import system_template_text, user_template_text
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from xiaohongshu_model import Xiaohongshu


def generate_xiaohongshu(theme,api_key):
    prompt = ChatPromptTemplate.from_messages([
        ("system",system_template_text),
        ("user", user_template_text)
    ])
    model = ChatOpenAI(
        model = "qwen-max-latest",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        openai_api_key = api_key
    )
    output_parser = PydanticOutputParser(pydantic_object=Xiaohongshu)
    chain = prompt | model | output_parser
    result = chain.invoke({
        "parser_instructions":output_parser.get_format_instructions(),
        "theme": theme
})
    return result
# print(generate_xiaohongshu("海南岛",os.getenv("DASHSCOPE_API_KEY")))
