from peewee import *
db = SqliteDatabase('gallery.sqlite')


class Artists(Model):
    artist = CharField(unique=True)
    email = CharField()

    class Meta:
        database = db

    def __str__(self):
        return f'Name: {self.artist_name} | email: {self.email}'

class Artworks(Model):
    artist = ForeignKeyField(Artists, backref= 'works')
    artwork_name = CharField()
    price = DecimalField()
    available = CharField(default='Available')

    class Meta:
        database = db

    def __str__(self):
        return f'Artist: {self.artist} | Name: {self.artwork_name} | Price: {self.price} | Available: {self.available}'

db.connect()
db.create_tables([Artists, Artworks])





main()