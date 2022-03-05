from app import db


class ExampleModel(db.Model):
    """Description of Model"""
    id = db.Column(db.Integer, primary_key=True)
    example_1 = db.Column(db.String(255))
    example_2 = db.Column(db.Integer, index=True, unique=False)


    def __repr__(self):
        return '<Question {}'.format(str(self.id) + ' ' + str(self.example_1) + ' '
                                     + str(self.example_2)
                                     )


class CoffeeJournal(db.Model):
    """Coffee Journal for the User to Enter"""
    id = db.Column(db.Integer, primary_key=True)
    entry_datetime = db.Column(db.DateTime())
    coffee_name = db.Column(db.Unicode(255))
    rating = db.Column(db.Integer)
    flavor_notes = db.Column(db.Unicode)

    def to_dict(self):
        """
        Pulls an instance's row(s) into a dict or list of dicts
        """
        # Need to test this with more than one row at a time
        return {
            'entry_datetime': self.entry_datetime,
            'coffee_name': self.coffee_name,
            'rating': self.rating,
            'flavor_notes': self.flavor_notes
        }

    def __repr__(self):
        return '<CoffeeJournal {}>'.format(
                str(self.id) + ' ' + str(self.entry_datetime) + ' ' + str(self.coffee_name) +
                ' ' + str(self.rating) + ' ' + str(self.flavor_notes)
        )
