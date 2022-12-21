from peewee import *


# when use non local db use connect. Don't forget close connect!
database = SqliteDatabase('db.sqlite3')


class BaseModel(Model):
    class Meta:
        database = database


class Words(BaseModel):
    id = PrimaryKeyField(null=False)
    word = CharField(column_name='word')
    lenght = IntegerField(column_name='lenght')


class Prompts(BaseModel):
    id = PrimaryKeyField(null=False)
    prompt = CharField(column_name='prompt')
    count = IntegerField(column_name='count')
    words = ForeignKeyField(Words, field='word', backref='words')



