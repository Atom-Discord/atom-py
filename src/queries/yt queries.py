from youtubesearchpython import SearchVideos
from ast import literal_eval

topic = None

search = SearchVideos(topic, offset = 1, mode = "json", max_results = maxVal)

obj = literal_eval(search.result()) # Convert JSON string to dictionary

i = 0
for elems in obj['search_result'][i]: # iterate over dictionary and grab links
    if elems == 'link':
        if i != maxVal - 1:
            for link in obj['search_result'][i]:
                print(obj['search_result'][i]['link'])
                if i == maxVal - 1:
                    break
                else:
                    i += 1
                    continue



    

