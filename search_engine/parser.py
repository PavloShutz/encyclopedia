"""Article's parser module."""

import re

from bs4 import BeautifulSoup, ResultSet, PageElement
import requests


def _render_source_text(word: str) -> str:
    """Get the source of searched page."""
    source = requests.get(f"http://sum.in.ua/?swrd={word}")
    source.encoding = "utf-8"
    return source.text


def _get_article_content_or_word(word: str) -> str | ResultSet:
    """Try to get article info."""
    source_text = _render_source_text(word)
    soup = BeautifulSoup(source_text, "lxml")
    try:
        article = soup.find(
            "div", attrs={"id": "article"}
        ).find_all(
            "div", attrs={"itemtype": "http://schema.org/ScholarlyArticle"}
        )
    except AttributeError:
        return word.lower()
    return article


def _refactor_article_content(article_content: PageElement) -> str:
    """Crop and refactor article"""
    p1 = re.compile(
        r'(\s*)Словник української мови: в (\d*) томах. — Том (\d*), (\d*). — Стор. (\d*).(\s*)'
    )
    p2 = re.compile(r'(\s*)Коментарі (\(\d*)\)(\s*)')
    refactored_article_content = p2.sub(
        '', p1.sub('', article_content.get_text())
    )
    return refactored_article_content


def render_article(word: str) -> str:
    """Render final article."""
    article = _get_article_content_or_word(word)
    if not isinstance(article, ResultSet):
        return f"Слова «{word}» не знайдено"
    final_article = ''
    for content in article:
        refactored_article = _refactor_article_content(content)
        final_article = final_article + refactored_article + '\n'
    return final_article
