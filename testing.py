from main import *
Sentence_testing = {
    "Example_currency" : "Please convert $500 USD to AED",
    "Example_email" : "I am Daniel send an annual leave email to tony.c.lin@pccw.com from 25/6 to 28/6"
}

object = LangChain_main()

# Botbuilder
# agent_bot_builder = object.botbuilder()
# agent_bot_builder.run(Sentence_testing['Example_currency'])

# OpenAI
agent_openai = object.openai()
agent_openai.run(Sentence_testing['Example_currency'])

# API
# agent_googlesearch = GoogleSearch()
# result = agent_googlesearch.simple_search(Sentence_testing['Example_Googlesearch'])
# print(result)