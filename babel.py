"""
This module procedurally generates a body of text following basic English
phrase structure rules. It writes the text to an HTML file.
TODO:
    * Modulate words
    * Generate large words arrays from files
    * Include prep phrases
NOTES:
    *
"""
import webbrowser
import random
import words


class Book:
    def __init__(self, num_chapters):
        """init Book class"""
        self.num_chapters = num_chapters

        w = words.Word()
        self.adjectives = w.gen_adjectives()
        self.adverbs = w.gen_adverbs()
        self.nouns = w.gen_nouns()
        self.verbs = w.gen_verbs()
        self.articles = ["the", "a", "one"]

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
        num_paragraphs = random.randrange(30, 50)
        paragraphs = [self.gen_paragraph() for i in range(num_paragraphs)]
        return "\n".join(paragraphs)

    def gen_paragraph(self):
        """generate paragraph"""
        num_sentences = random.randrange(8, 13)
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
        adverb = random.choice(self.adverbs)
        return "{0} {1} {2}".format(verb, noun_phrase, adverb)


if __name__ == '__main__':
    num_chapters = 3
    random.seed(1234567890)
    BOOK = Book(num_chapters)
    BOOK.gen_book()
