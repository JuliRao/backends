import json

f = open('燕山君.json', 'r')
line = f.readline()

content = json.loads(line)
print(content)


if __name__ == '__main__':
    pass
