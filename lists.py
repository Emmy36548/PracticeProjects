thisdict = {
	"name":"Emily",
	"age":25,
	"college":"Engineering",
	"fruits": ["apples", "kiwi"]
}
print(len(thisdict))
thisdict.update({"language": "English"})
thisdict.get("name")
del thisdict["age"]
print(thisdict.items())