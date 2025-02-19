Project Name:rest-api-flask

python -m venv .venv
.venv\Scripts\activate   
pip install -r requirements.txt
flask run
==run command
python
from app import db,app
app.app_context().push()
db.create_all()
from app import book

book = Book(name="Flask", description='Books is good')

>>book
>> db.session.add(book)
>>db.sesssion.commit()

>>db.session.add(Book(name='Django', description="Django description"))
