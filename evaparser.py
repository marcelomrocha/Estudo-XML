import sys
import json
import xml.etree.ElementTree as ET

tree = ET.parse(sys.argv[1])  # arquivo de codigo xml
root = tree.getroot()
output = ""
key = 1000
gohashid = 0
inicio = True  # para nao iniciar com a virgula

def block_process(root):
    global output, inicio
    for command in root:
        if (command.tag == 'light'):
            if (not inicio): output += ",\n"
            output += light_process(command)

        if (command.tag == 'wait'):
            if (not inicio): output += ",\n"
            output += wait_process(command)

        if (command.tag == 'voice'):
            if (not inicio): output += ",\n"
            output += voice_process(command)

        if (command.tag == 'talk'):
            if (not inicio): output += ",\n"
            output += talk_process(command)

        if (command.tag == 'random'):
            if (not inicio): output += ",\n"
            output += random_process(command)

        if (command.tag == 'listen'):
            if (not inicio): output += ",\n"
            output += listen_process(command)

        if (command.tag == 'eva-emotion'):
            if (not inicio): output += ",\n"
            output += eva_emotion_process(command)

        if (command.tag == 'case'):
            if (not inicio): output += ",\n"
            output += case_process(command)
            block_process(command)

        if (command.tag == 'switch'):
            block_process(command)
        inicio = False

# head processing
def head_process(root_element):
    root_element.attrib["key"] = 0
    init = """{
  "_id": """ + '"' + root_element.attrib["id"] + '",' + """
  "nombre": """ + '"' + root_element.attrib['name'] + '",' + """
  "data": {
    "node": [
"""
    return init


# tail processing
def tail_process():
    tail = """
    ],
    "link": []
  }
}"""
    return tail


# light node processing
def light_process(light_command):
    global gohashid, key
    light_command.attrib["key"] = key
    light_node = """      {
        "key": """ + str(key) + """,
        "name": "Light_8",
        "type": "light",
        "color": "lightblue",
        "isGroup": false,
        "group": "",
        "lcolor": """ + '"' + light_command.attrib['color'] + '",' + """
        "state": """ + '"' + light_command.attrib['state'] + '",' + """
        "__gohashid": """ + str(gohashid) + """
      }"""
    gohashid += 1
    key += 1
    return light_node

# listen node processing
def listen_process(listen_command):
    global gohashid, key
    listen_command.attrib["key"] = key
    listen_node = """      {
        "key": """ + str(key) + """,
        "name": "Listen_8",
        "type": "listen",
        "color": "lightblue",
        "isGroup": false,
        "group": "",
        "lcolor": "zzz",
        "state": "zzz",
        "__gohashid": """ + str(gohashid) + """
      }"""
    gohashid += 1
    key += 1
    return listen_node


# talk node processing
def talk_process(talk_command):
    global gohashid, key
    talk_command.attrib["key"] = key
    talk_node = """      {
        "key": """ + str(key) + """,
        "name": "Talk_1",
        "type": "speak",
        "color": "lightblue",
        "isGroup": false,
        "text": """ + '"' + talk_command.text + '",' + """
        "__gohashid": """ + str(gohashid) + """
      }"""
    gohashid += 1
    key += 1
    return talk_node


# voice node processing
def voice_process(voice_command):
    global gohashid, key
    voice_command.attrib["key"] = key
    voice_node = """      {
        "key": """ + str(key) + """,
        "name": "Voice_1",
        "type": "voice",
        "color": "lightblue",
        "isGroup": false,
        "voice": "pt-BR_IsabelaV3Voice",""" + """
        "__gohashid": """ + str(gohashid) + """
      }"""
    gohashid += 1
    key += 1
    return voice_node


# eva_emotion node processing
def eva_emotion_process(eva_emotion_command):
    global gohashid, key
    eva_emotion_command.attrib["key"] = key
    eva_emotion_node = """      {
      "key": """ + str(key) + """,
      "name": "Eva_Emotion_13",
      "type": "emotion",
      "color": "lightyellow",
      "isGroup": false,
      "group": "",
      "emotion": """ + '"' + eva_emotion_command.attrib['emotion'] + '",' + """
      "level": 0,
      "speed": 0,
      "__gohashid": """ + str(gohashid) + """
    }"""
    gohashid += 1
    key += 1
    return eva_emotion_node


# random node processing
def random_process(random_command):
    global gohashid, key
    random_command.attrib["key"] = key
    random_node = """      {
        "key": """ + str(key) + """,
        "name": "Random_10",
        "type": "random",
        "color": "lightblue",
        "isGroup": false,
        "group": "",
        "min": """ + random_command.attrib['min'] + ',' + """
        "max": """ + random_command.attrib['max'] + ',' + """
        "__gohashid": """ + str(gohashid) + """
      }"""
    gohashid += 1
    key += 1
    return random_node


# condition node processing
def case_process(case_command):
    global gohashid, key
    case_command.attrib["key"] = key
    case_node = """      {
        "key": """ + str(key) + """,
        "name": "Condition_2",
        "type": "if",
        "color": "lightblue",
        "isGroup": false,
        "text": """ + case_command.attrib['value'] + ',' + """
        "opt": 4,
        "__gohashid": """ + str(gohashid) + """
      }"""
    gohashid += 1
    key += 1
    return case_node


# wait node processing
def wait_process(wait_command):
    global gohashid, key
    wait_command.attrib["key"] = key
    wait_node = """      {
        "key": """ + str(key) + """,
        "name": "Wait_2",
        "type": "wait",
        "color": "lightblue",
        "isGroup": false,
        "time": """ + wait_command.attrib['duration'] + ',' + """
        "__gohashid": """ + str(gohashid) + """
      }"""
    gohashid += 1
    key += 1
    return wait_node


# xml processing (string concatenation)
output += head_process(root)
block_process(root)
output += tail_process()

# creating the json file
file_out_name = root.attrib['name'] + '.json'
file_out = open(file_out_name, "w")
file_out.write(output)
# file_out.write(output.encode('utf-8'))
file_out.close()

# inserting json file in lowdb interaction database
dbfile = open('db.json', 'r')

# transforma o arquivo de texto em um dict
eva_db_dict = json.load(dbfile)

print("List of registers types in db: ")
print("--------------------------------------------")
for elem in eva_db_dict:
    print("*", elem)
print("\nTotal interactions found:", len(eva_db_dict["interaccion"]))
print(type(eva_db_dict["interaccion"]))

print(output)
# output é uma string. a função json.loads transforma a string em um dict
eva_db_dict["interaccion"].append(json.loads(output))

# eva_db_dict["interaccion"].remove("EvaML_X")
print("\nTotal interactions found:", len(eva_db_dict["interaccion"]))


def run_tree(root):
    for elem in root:
        if len(elem) != 0: run_tree(elem)
        print(elem.tag, elem.attrib["key"])

run_tree(root)
