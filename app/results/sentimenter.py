import pyodbc
import flask

class Sentimenter:
    def __init__(self, url, header, blob):
        self.url = url
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
            conn = pyodbc.connect(con_str)
            cursor = cnxn.cursor()
            cursor.execute()
            cursor.commit()
        except:
            pass

        