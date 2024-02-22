import os
from langchain.agents import *
from langchain.llms import OpenAI
from langchain.sql_database import SQLDatabase
from langchain.chat_models import ChatOpenAI
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from HKTChatBotBuilder import *
from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.sql_database import SQLDatabase
from langchain.llms.openai import OpenAI
from langchain.agents import AgentExecutor
import pymysql
from langchain.llms import AzureOpenAI


# llm_botbuilder = HKTChatBotBuilder()
llm = AzureOpenAI(temperature=0.9,model="gpt-3.5-turbo", engine='text-davinci-003')
# llm = ChatOpenAI(model_="gpt-3.5-turbo", engine="td2")
# print(llm.Config)
db_user = "root"
db_password = "1234"
db_host = "192.168.50.120"
db_name = "langchain"

# conn = 'mysql+pymysql://winson:joniwhfe@localhost/data_project'
db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}")
# db = SQLDatabase.from_uri(conn)
toolkit = SQLDatabaseToolkit(db=db,llm=llm)
agent_executor = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True
)
response = agent_executor.run("Can I have average age of people having heart disease?")

print(response)
