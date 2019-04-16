
import os
from pathlib import Path
from peewee import *

pwd = Path(__file__).parent

db = SqliteDatabase(str(Path(pwd) /  "../lufly/sys_data/sys_table.sqlitedb"))

class BaseModel(Model):
    class Meta:
        database = db


class CharPhoneTable(BaseModel):
    id = IntegerField(primary_key=True)
    char = CharField(2)
    phones = CharField(2)
    priority = IntegerField()
    updatedt = DateTimeField("%Y-%m-%d %H:%M:%S")


class CharShapeTable(BaseModel):
    id = IntegerField(primary_key=True)
    char = CharField(2)
    shapes = CharField(2)
    priority = IntegerField()
    updatedt = DateTimeField("%Y-%m-%d %H:%M:%S")


class WordPhoneTable(BaseModel):
    id = IntegerField(primary_key=True)
    word = CharField()
    phones = CharField()
    priority = IntegerField()
    updatedt = DateTimeField("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return f"<{self.id},{self.word},{self.phones},{self.priority},{self.updatedt}>"


class FullToTwoTable(BaseModel):
    id = IntegerField(primary_key=True)
    full = CharField()
    two = CharField()


class ZrmToTwoTable(BaseModel):
    id = IntegerField(primary_key=True)
    full = CharField();
    two = CharField(); 


class CharFreqTable(BaseModel):
    id = IntegerField(primary_key=True)
    char = CharField()
    freq = CharField()
    updatedt = DateTimeField("%Y-%m-%d %H:%M:%S")


class DelWordTable(BaseModel):
    id = IntegerField(primary_key=True)
    word = CharField()
    updatedt = DateTimeField("%Y-%m-%d %H:%M:%S")


class EngWordTable(BaseModel):
    id = IntegerField(primary_key=True)
    word = CharField(unique=True)
    priority = IntegerField()
    updatedt = DateTimeField("%Y-%m-%d %H:%M:%S")


def create_tables():
    if not CharPhoneTable.table_exists():
        CharPhoneTable.create_table()
    if not CharShapeTable.table_exists():
        CharShapeTable.create_table()
    if not WordPhoneTable.table_exists():
        WordPhoneTable.create_table()
    if not FullToTwoTable.table_exists():
        FullToTwoTable.create_table()
    if not CharFreqTable.table_exists():
        CharFreqTable.create_table()
    if not DelWordTable.table_exists():
        DelWordTable.create_table()
    if not EngWordTable.table_exists():
        EngWordTable.create_table()
    if not ZrmToTwoTable.table_exists():
        ZrmToTwoTable.create_table()





create_tables()
