import json

f = open('zhidao.json', 'r')
line = f.readline()

content = json.loads(line)
print(content)


if __name__ == '__main__':
    pass
