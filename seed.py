from models import db, Pet
from app import app

db.drop_all()
db.create_all()

Pet.query.delete()

pet1 = Pet(name='Carla',
           species='Chameleon',
           photo_url='https://images.unsplash.com/photo-1502641960251-c175da3bf508?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1567&q=80',
           age=2,
           notes="This Chameleon may change her skin to suit her surroundings, but that doesn't mean she's superficial.  If she takes a liking to you, she'll be your loyal companion through thick and thin.",
           available=True)

pet2 = Pet(name='Gus',
           species='Cat',
           photo_url='https://images.unsplash.com/photo-1573865526739-10659fec78a5?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=958&q=80',
           age=5,
           notes="Gus is a real chill cat.  Does a lot of sitting around... not looking for an adventure, but in need a of a new best friend.",
           available=True)

pet3 = Pet(name='Trixie',
           species='Australian Shepard',
           age=2,
           notes="Let's just say she is very high energy.",
           available=True,
           photo_url='https://images.unsplash.com/photo-1541382107930-f87ae2e7d95f?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MjJ8fGF1c3RyYWxpYW4lMjBzaGVwYXJkfGVufDB8fDB8&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60')

pet4 = Pet(name='Fish',
           species='Rooster',
           photo_url='https://images.unsplash.com/photo-1570975434862-9ae02c75bcec?ixid=MXwxMjA3fDB8MHxzZWFyY2h8NTF8fHJvb3N0ZXJ8ZW58MHx8MHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60',
           age=1,
           notes="You wouldn't expect a rooster to be cuddly, but this guy just wants hugs, love, and long chats... just so long as the conversation doesn't turn to aquatic life.  Want to bring this goofball home to roost?",
           available=True)

pet5 = Pet(name='Becky',
           species='Goose',
           photo_url='https://images.unsplash.com/photo-1546470786-1bc72e490b8d?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1650&q=80',
           age=2,
           available=False)

pet6 = Pet(name='Lucifer',
           species='Rabbit',
           photo_url='https://images.unsplash.com/photo-1599169713100-120531cef331?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=934&q=80',
           age=1,
           available=False)

db.session.add_all([pet1,pet2,pet3,pet4,pet5,pet6])
db.session.commit()