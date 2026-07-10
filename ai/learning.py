from database.memory import save_knowledge, get_knowledge as db_get_knowledge


def learn(topic, information):
    save_knowledge(topic, information)


def get_knowledge(topic):
    return db_get_knowledge(topic)