import json
from pprint import pprint
import xml.etree.ElementTree as ET

file = r'D:\Python\Netology\3.1.formats.json.xml\newsafr.json'


def get_text(file):
    # функция читает файл и возвращает текст новостей

    words = list()
    with open(file, encoding='utf-8') as f:
        news = json.load(f)
        articles_qty = len(news['rss']['channel']['items'])

        for article in range(0, articles_qty):
            text = news['rss']['channel']['items'][article]['description'].split(' ')

            for word in text:
                if len(word) > 6:
                    words.append(word)
        
    return words

def get_word_stat(words):
    # функция возвращает словарь частотности слов на основе текста новостей

    words_stat = dict()
    for word in words:
        if word not in words_stat:
            words_stat[word] = 1
        else:
            words_stat[word] += 1

    return words_stat


def get_unique_rating(word_stat):
    # функция получает все значения частоты упоминаемости слов и возвращает их уникальные значения

    rating = set()
    rates = list()
    for stat_value in word_stat.values():
        rating.add(stat_value)

    for rate in rating:
        rates.append(rate)
        rates = sorted(rates, reverse=True)

    return rates[0:11]

def find_top_words(rates, word_stat):
    # функция возвращает наиболее упоминаемые слова на основе списка уникальных значений частот

    top_words = []
    for key, val in word_stat.items():
        if val in rates:
            top_words.append(key)
    
    return top_words


text = get_text(file)
word_stats = get_word_stat(text)
rates = get_unique_rating(word_stats)
top_words = find_top_words(rates, word_stats)

print(top_words)


