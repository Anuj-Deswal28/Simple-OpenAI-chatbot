from langchain_core.prompts import ChatPromptTemplate, MessagePlaceholder
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core import PydanticOutputParser
from pydantic import BaseModel, Field

class Person(BaseModel):
    result : str = Field(description= "all output should come in this str")

parser = PydanticOutputParser(pydantic_object =Person)
# template
prompt = ChatPromptTemplate([
    ('system', 'You are a customer support expert'),
    MessagePlaceholder(variable_name = 'chat_history')
    ('human', 'Explain in simple terms, what is {topic} \n {format_instruction}')
])

chat_template = prompt.partial(format_instructions=parser.get_format_instructions())

chat_template.save('template.json')