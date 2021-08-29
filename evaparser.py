import sys
import json
import pickle
import xml.etree.ElementTree as ET

tree = ET.parse(sys.argv[1])  # arquivo de codigo xml
root = tree.getroot()
# block = root.findall('./block')

output = ""
key = 1000
gohashid = 0
contador = 1  # identifica o primeiro e o ultimo no

def block_process(root):
    global output, contador
    for command in root:
        #if (contador != 1): output += ","  # imprime as virgulas
        if (command.tag == 'light'):
            if (contador != 1): output += ",\n"
            output += light_process(command)
        if (command.tag == 'wait'):
            if (contador != 1): output += ",\n"
            output += wait_process(command)
        if (command.tag == 'voice'):
            if (contador != 1): output += ",\n"
            output += voice_process(command)
        if (command.tag == 'talk'):
            if (contador != 1): output += ",\n"
            output += talk_process(command)
        if (command.tag == 'random'):
            if (contador != 1): output += ",\n"
            output += random_process(command)
        if (command.tag == 'eva-emotion'):
            if (contador != 1): output += ",\n"
            output += eva_emotion_process(command)
        if (command.tag == 'case'):
            if (contador != 1): output += ",\n"
            output += case_process(command)
            block_process(command)
        if (command.tag == 'switch'):
            block_process(command)
        contador = 2

# head processing
def head_process(root_element):
    init = """{
  "_id": "a1000-b3000",
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


# talk node processing
def talk_process(talk_command):
    global gohashid, key
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


# xml processing
output += head_process(root)
block_process(root)
output += tail_process()

# creating the json file
file_out_name = root.attrib['name'] + '.json'
file_out = open(file_out_name, "w")
file_out.write(output)
file_out.close()

# inserting json file in lowdb interaction database
dbfile = open('db.json', 'r')
eva_db_dict = json.load(dbfile)
print("List of registers types in db: ")
print("--------------------------------------------")
for elem in eva_db_dict:
    print("*", elem)
print("\nTotal interactions found:", len(eva_db_dict["interaccion"]))
print(type(eva_db_dict["interaccion"]))

eva_db_dict["interaccion"].append(json.loads(output))
# eva_db_dict["interaccion"].remove("EvaML_X")
print("\nTotal interactions found:", len(eva_db_dict["interaccion"]))

geeky_file = open('db2.json', 'w')
geeky_file.write(str(eva_db_dict))
geeky_file.close()
