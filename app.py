from model import database, Words, Prompts


def create_tables():
    with database:
        database.create_tables([Words, Prompts])


def add_word(word):
    row = Words(word=word, lenght=len(word))
    row.save()


def add_prompt(prompt: str, count: int, words: list):
    row = Prompts(prompt=prompt, count=count, words=words)
    row.save()


def delete_prompt(id: int):
    row = Prompts.get(Prompts.id == id)
    row.delete_instance()

