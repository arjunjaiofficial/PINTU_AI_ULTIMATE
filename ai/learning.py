from data.memory import remember, recall

def learn(topic, information):
    remember(f"knowledge_{topic.lower()}", information)

def get_knowledge(topic):
    return recall(f"knowledge_{topic.lower()}")