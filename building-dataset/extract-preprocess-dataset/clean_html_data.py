import json
from bs4 import BeautifulSoup

f = open('json/MVD_Dataset.json')

# returns JSON object as
# a dictionary
data = json.load(f)

index = 0
for i in data:
    try:

        soup = BeautifulSoup(i['doc'], features="html.parser")

        # kill all script and style elements
        for script in soup(["script", "style"]):
            script.extract()  # rip it out

        # get text
        text = soup.get_text()

        # break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in text.splitlines())
        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # drop blank lines
        text = '\n'.join(chunk for chunk in chunks if chunk)

        invalid_tags = ['b', 'i', 'u', 'div']
        soup = BeautifulSoup(text)
        for tag in invalid_tags:
            for match in soup.findAll(tag):
                match.replaceWithChildren()

        data[index]['doc'] = soup.get_text()

    except:
        print("ERR")
        print(i)

    index = index + 1

from urllib.request import urlopen

json_object = json.dumps(data, indent=4)

# Writing to sample.json
with open("json/cleaned_dataset_mvd_new.json", "w") as outfile:
    outfile.write(json_object)