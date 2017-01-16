# -*-
#
# @author: a sadeghi
# @email:  sadeghi.afshin@gmail.com
#
# @date:   2017-01-05
# -*-
import re
import unicodedata

from bs4.element import Tag


def isTagOrString(element):
    if isinstance(element, Tag):
        return (True, element)
    else:
        element = element.strip().strip(',').strip(u'\xb7').strip()
        return (False, str(element.encode('utf-8')))


def profile2name(text):
    return normalizeText(re.sub('_', ' ' , re.sub('\d+', '', text)))


def researcher2publication(identifier):
    return {'identifier': identifier, 'primary': False, 'corresponding': False}


def normalizeText(text, return_string = True):
    if all(ord(c) < 128 for c in text):
        return text
    text = text.strip()
    text = ''.join((c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn'))
    if return_string:
        return str(text)
    else:
        return text


def fixForcedLineChange(text):
    return text.replace('-\n', '').replace('\n', ' ')


def getStats(blob):
    return str(blob('div', attrs={'class': 'stats-count'})[0].contents[0].strip())
