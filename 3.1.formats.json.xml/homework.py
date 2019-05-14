import json
from pprint import pprint
import xml.etree.ElementTree as ET

file_xml = r'newsafr.xml'
file_json = r'newsafr.json'

def get_text_from_json(file):
    # функция читает файл json и возвращает список слов больше 6 символов

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

    return rates[0:10]



def find_top_words(rates, word_stat):
    # функция возвращает наиболее упоминаемые слова на основе списка уникальных значений частот

    top_words = []
    for key, val in word_stat.items():
        if val in rates:
            top_words.append({
                key : val
                })
    
    return top_words



def get_text_from_xml(file):
    # функция читает файл xml и возвращает список слов больше 6 символов

    words = []
    tree = ET.parse(file_xml)
    root = tree.getroot()

    for article in range(6, len(root[0])):
        text = root[0][article][2].text.split(' ')

        for word in text:
                if len(word) > 6:
                    words.append(word)

    return words



def get_text_from_file(file):
    # функция проверяет формат файла и вызывает соответствующую функцию чтения файла или возвращает ошибку

    format = file.split('.')[-1]

    if format == 'json':
        return get_text_from_json(file)
    elif format == 'xml':
        return get_text_from_xml(file)
    else:
        print('Неизвестный формат')

def get_top_words(file):
    # возвращает список наиболее упоминаемых слов длинною более 6 символов

    text = get_text_from_file(file)
    word_stat = get_word_stat(text)
    rates = get_unique_rating(word_stat)
    top_words = find_top_words(rates, word_stat)
    
    return top_words


get_top_words('newsafr.xml')
get_top_words('newsafr.json')

