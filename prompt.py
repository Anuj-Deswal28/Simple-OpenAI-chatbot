from langchain_core.prompts import ChatPromptTemplate, MessagePlaceholder
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

# template
chat_template = ChatPromptTemplate([
    ('system', 'You are a customer support expert'),
    MessagePlaceholder(variable_name = 'chat_history')
    ('human', 'Explain in simple terms, what is {topic}')
])



chat_template.save('template.json')