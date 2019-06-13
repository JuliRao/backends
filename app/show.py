import json

f = open('zhidao/35.json', 'r')
line = f.readline()

content = json.loads(line)
print(content)


if __name__ == '__main__':
    pass
