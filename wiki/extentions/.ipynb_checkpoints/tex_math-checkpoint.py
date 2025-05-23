from markdown.extensions import Extension
from markdown.inlinepatterns import InlineProcessor
import xml.etree.ElementTree as etree
import re

class MathInlineProcessor(InlineProcessor):
    def handleMatch(self, m, data):
        el = etree.Element('span')
        el.set('class', 'tex-math')
        el.text = f"\\({m.group(1)}\\)"
        return el, m.start(0), m.end(0)

class MathExtension(Extension):
    def extendMarkdown(self, md):
        pattern = MathInlineProcessor(r'\$\$(.+?)\$\$', md)
        md.inlinePatterns.register(pattern, 'tex_math', 175)

def makeExtension(**kwargs):
    return MathExtension(**kwargs)
