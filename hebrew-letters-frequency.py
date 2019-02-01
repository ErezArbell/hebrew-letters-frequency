# -*- coding: utf-8 -*-
import urllib2
import sys

def get_text(url):
	response = urllib2.urlopen(url)
	return response.read()

hebrew_letters = u"אבגדהוזחטיכלמנסעפצקרשת"
final_letters = {
	u'ך': u'כ',
	u'ם': u'מ',
	u'ן': u'נ',
	u'ף': u'פ',
	u'ץ': u'צ'
}

letters = dict()
for letter in hebrew_letters:
	letters[letter] = 0

for url in sys.argv[1:]:
	text = get_text(url)
	text = unicode(text, "utf-8")
	for letter in text:
		if letter in final_letters.keys():
			letter = final_letters[letter]
		if letter in hebrew_letters:
			letters[letter] += 1

sum = 0
for letter in letters:
	sum += letters[letter]

letters_tupple = [(letter,letters[letter]) for letter in hebrew_letters]
for letter, c in sorted(letters_tupple, key=lambda (a,b): b):
    print("%3s%8d%8.2f%%" % (letter , letters[letter], 100.0*letters[letter]/sum))