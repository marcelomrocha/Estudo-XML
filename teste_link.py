import sys
import json
import xml.etree.ElementTree as ET

tree = ET.parse("teste.xml")  # arquivo de codigo xml
root = tree.getroot() # evaml root node

qtd = len(root.find("interaction"))
interaction = root.find("interaction")
print("numero de nodes no bloco principal da interacao: ", qtd)

links = []

def cria_link(node_from, node_to):
    if len(node_to) == 0:
        links.append(node_from.attrib["key"] + ", " + node_to.attrib["key"])
    elif (node_to.tag == "switch"):
        link_process(node_from, node_to)
    else:
        links.append(node_from.attrib["key"] + ", " + node_to.attrib["key"])
        link_process(node_to, node_to)

def link_process(node_from, node_list):
    qtd = len(node_list)
    print(node_list.tag, qtd, node_list[0].tag)
    node_to = node_list[0]
    print(node_from.tag, node_to.tag)
    cria_link(node_from, node_to)
    for i in range(0, qtd-1):
        node_from = node_list[i]
        node_to = node_list[i+1]
        print(node_from.tag, node_to.tag)
        cria_link(node_from, node_to)

link_process(root.find("settings").find("voice"), interaction)
print("numero de arestas: ", len(links))
print(links)
