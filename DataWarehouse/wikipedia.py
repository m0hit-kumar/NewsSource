import wikipedia
wikipedia.set_lang('en')
res = wikipedia.search("new year")
print(res)

# it will get data
result = wikipedia.summary("new year")
print(result)
