import pyodbc
import flask
import datetime

class Sentimenter:
    def __init__(self, www, header, blob):
        self.www = www
        self.header = header

        self.overall = blob.sentiment 

        self.most_polar_sentence = blob.sentences[0]
        self.least_polar_sentence = blob.sentences[0]
        self.most_objective_sentence = blob.sentences[0]
        self.most_subjective_sentence = blob.sentences[0]

        for sentence in blob.sentences[1:]:
            if self.most_polar_sentence.sentiment.polarity < sentence.sentiment.polarity:
                self.most_polar_sentence = sentence

            if self.least_polar_sentence.sentiment.polarity > sentence.sentiment.polarity:
                self.least_polar_sentence = sentence

            if self.most_objective_sentence.sentiment.subjectivity > sentence.sentiment.subjectivity:
                self.most_objective_sentence = sentence

            if self.most_subjective_sentence.sentiment.subjectivity < sentence.sentiment.subjectivity:
                self.most_subjective_sentence = sentence

    def save_result(self):
        '''
        Simple method to save the result to a database, going without ORM for now
        '''
        try:
            con_str = flask.current_app.config['CONNECTION_STRING']
            cnxn = pyodbc.connect(con_str)
            cursor = cnxn.cursor()
            SQLstmt = f'''INSERT INTO results (WWW, HEADER, OVERALL, TIMESTAMP) VALUES 
            ('{self.www.url}',
            '{self.header}',
            '{self.overall}',
            '{datetime.datetime.now()}'
            )'''

            cursor.execute(SQLstmt)
            cursor.commit()
        except:
            pass

        