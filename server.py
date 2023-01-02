import nlp_chat_bot.neuralintents as neuralintents
from nlp_chat_bot.functions import mappings


bot = neuralintents.GenericAssistant("intents.json", mappings, "model")
bot.train_model()
bot.save_model()