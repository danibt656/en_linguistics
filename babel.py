""" Duree: an experiment in linguistics.
This module procedurally generates a body of text following basic English
phrase structure rules. It writes the text to an HTML file.
TODO:
    * Modulate phrases
    * Include prep phrases
NOTES:
    *
"""
import webbrowser
import random


class Book:
    def __init__(self, num_chapters):
        """init the class"""
        self.num_chapters = num_chapters
        self.articles = ["the", "a", "one"]
        self.adjectives = ["talented", "green", "fast", "slow", "dark"]
        self.nouns = ["boy", "girl", "cat", "king", "squid"]
        self.verbs = ["ate", "drank", "dreamed", "wrote", "read"]

    def gen_book(self):
        """generate book"""
        output_file = open("index.html", "w")
        book = ""
        ch_count = 0
        book += "<html><head><link rel=\"stylesheet\" href=\"style.css\"></head><body>"
        print("Num chapters: {0}".format(self.num_chapters))
        while ch_count < self.num_chapters:
            chapter = self.gen_chapter()
            book += "<h1>Chapter {0}</h1>\n".format(ch_count+1)
            book += "<p>{0}</p>\n".format(chapter)
            ch_count += 1
        book += "</body></html>"
        output_file.write(book)
        output_file.close()
        print("Printed book succesfully")

    def gen_chapter(self):
        """generate chapter"""
        num_paragraphs = random.randrange(20, 30)
        paragraphs = [self.gen_paragraph() for i in range(num_paragraphs)]
        return "\n".join(paragraphs)

    def gen_paragraph(self):
        """generate paragraph"""
        num_sentences = random.randrange(5, 8)
        sentences = [self.gen_sentence() for i in range(num_sentences)]
        return "<p>{0}</p>".format(" ".join(sentences))

    def gen_sentence(self):
        """generate sentece"""
        noun_phrase = self.gen_noun_phrase()
        verb_phrase = self.gen_verb_phrase()
        return "{0} {1}.".format(noun_phrase, verb_phrase).capitalize()

    def gen_noun_phrase(self):
        """generate noun phrase"""
        article = random.choice(self.articles)
        adjective = random.choice(self.adjectives)
        noun = random.choice(self.nouns)
        return "{0} {1} {2}".format(article, adjective, noun)

    def gen_verb_phrase(self):
        """generate verb phrase"""
        verb = random.choice(self.verbs)
        noun_phrase = self.gen_noun_phrase()
        return "{0} {1}".format(verb, noun_phrase)


if __name__ == '__main__':
    num_chapters = 3
    random.seed(1234567890)
    BOOK = Book(num_chapters)
    BOOK.gen_book()
