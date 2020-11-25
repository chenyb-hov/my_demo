from xml.parsers.expat import ParserCreate
import encodings
class DefaultSaxHandler(object):
    def start_element(self, name, attr):
        print('sax: start_element : %s attrs: %s' % (name, str(attr)))

    def end_element(self,name):
        print('sax: end_element: %s' % name)

    def char_data(self, data):
        print('sax: char_data: %s' % data)

xml = r'''<?xml version="1.0"?><ol><li><a href="/py"></a></li><li><a href="/route"></a></li></ol>'''

handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)

L = []
L.append(r'<?xml version="1.0" ?>')
L.append(r'<div>1</div>')
L.append(r'<p>')
L.append(str(('some & data').encode('utf-8')))
L.append(r'</p>')
# print(str(L))
print(L)
print("".join(L))
datas= {}
class DefaultSaxHandler1(object):
    def start_xml(self, name, attr):
        self.name = name
        print(name, str(attr))
        #print('sax: start_element : %s attrs: %s' % (name, str(attr)))
    def end_xml(self, name):
        print(name)
    def sax_data(self, data):
        datas[self.name] = data

def parseXml(xml):
    datas.clear()
    default1 = DefaultSaxHandler1()
    parser1 = ParserCreate()
    parser1.StartElementHandler = default1.start_xml
    parser1.EndElementHandler = default1.end_xml
    parser1.CharacterDataHandler = default1.sax_data
    parser1.Parse(xml)
    return datas
xml1 = r'''<?xml version="1.0" ?><div><city color="red">Beijing</city><dates><time></time></dates></div>'''
xml2 = r'''<?xml version="1.0" ?><ul><city color="red">Fujian</city><dates><time></time></dates></ul>'''

result = parseXml(xml1)
assert result['city'] == 'Beijing'
print(result)
result1 = parseXml(xml2)
assert result['city'] == 'Fujian'
print(result1)


obj = {'a': {'b': {'c': {'d': {'e': ['f', 'g']
                               }
}}}}
print(obj['a']['b']['c']['d']['e'])
