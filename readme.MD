Python sort and Manipulate

In the Python file, you have a program that performs a GET request on the route http://coderbyte.com/api/challenges/json/date-list and then sort the object keys alphabetically.
However, the sorting should be case-insensitive, and the original data structure should be preserved (e.g., lists shpud remain lists, dictionaries should remain dictionaries). Keep in mind that while the JSON format uses null, in Python, this is represented as None.

Next, remove any duplicate dictionaries from lists. Two dictionaries are considered duplicates if they have the same key and values in the same order. Only the first occurrence should be preserved when an list contains duplicate dictionaries.

finally, remove any dictionary properties with all values set to an empy string or None (equivalent to null in JSON), and print a list of modified dictionaries. Be sure to call json.dumps on the final list to convert it back to JSON format, where None in Python will be represented as null.

Example input:

[{"name":"John","age":30,"city":"New York","country":"USA","Hobbies":["reading","swimming","hiking","swimming"],"occupation":"programmer","favorite_foods":{"Breakfast":"pancakes","Lunch":"","dinner":"pasta","Snack":""},"gear":{"type":"","material":"","color":null},"affiliations":["","",""],"friends":[{"name":"Jane","age":28,"city":"New York","country":"USA","occupation":null},{"name":"Tom","age":32,"city":"London","country":"UK","occupation":"teacher"},{"name":"Jane","age":28,"city":"New York","country":"USA","occupation":null}]}]

Example Output:
[{"age": 30, "city": "New York", "country": "USA", "favorite_foods": {"Breakfast": "pancakes", "dinner": "pasta"}, "friends": [{"age": 28, "city": "New York", "country": "USA", "name": "Jane"}, {"age": 32, "city": "London", "country": "UK", "name": "Tom", "occupation": "teacher"}], "gear": {}, "Hobbies": ["reading", "swimming", "hiking"], "name": "John", "occupation": "programmer"}]

FOR YATING:

if api doesn't work for you, here's the data:

[
{
"name": "HarryPotter",
"age": 18,
"house": "",
"wand": {
"wood": "Holly",
"core": "Phoenixfeather",
"length": 11
},
"friends": [
{
"name": "HermioneGranger",
"age": 18,
"house": "Gryffindor",
"wand": {
"wood": "Vine",
"core": "Dragonheartstring",
"length": 10.75
},
"occupation": null
},
{
"name": "RonWeasley",
"age": 18,
"house": "Gryffindor",
"wand": {
"wood": "Willow",
"core": "Unicornhair",
"length": 14
},
"occupation": "student"
},
{
"name": "HermioneGranger",
"age": 18,
"house": "Gryffindor",
"wand": {
"wood": "Vine",
"core": "Dragonheartstring",
"length": 10.75
},
"occupation": null
}
],
"enemies": [
"LordVoldemort",
"DracoMalfoy"
],
"patronus": "Stag"
},
{
"name": "HermioneGranger",
"age": 18,
"house": "Gryffindor",
"wand": {
"wood": "",
"core": "",
"length": null
},
"friends": [
{
"name": "HarryPotter",
"age": 18,
"house": "Gryffindor",
"wand": {
"wood": "Holly",
"core": "Phoenixfeather",
"length": 11
},
"occupation": "student"
},
{
"name": "RonWeasley",
"age": 18,
"house": "Gryffindor",
"wand": {
"wood": "Willow",
"core": "Unicornhair",
"length": 14
},
"occupation": "student"
},
{
"name": "LunaLovegood",
"age": 18,
"house": "Ravenclaw",
"wand": {
"wood": "Unknown",
"core": "Unknown",
"length": "Unknown"
},
"occupation": "student"
}
],
"enemies": [
"",
""
],
"patronus": "Otter"
},
{
"name": "RonWeasley",
"age": 18,
"house": "Gryffindor",
"wand": {
"wood": "Willow",
"core": "Unicornhair",
"length": 14
},
"friends": [
{
"name": "HarryPotter",
"age": 18,
"house": ""
},
{
"name": "HermioneGranger",
"age": 18,
"house": "Gryffindor"
},
{
"name": "HermioneGranger",
"age": 18,
"house": "Gryffindor"
}
],
"enemies": [
{
"name": "DracoMalfoy",
"age": 18,
"house": "Slytherin"
},
{
"name": "VincentCrabbe",
"age": 18,
"house": "Slytherin"
}
],
"patronus": "JackRussellTerrier"
},
{
"name": "GinnyWeasley",
"age": null,
"house": "Gryffindor",
"wand": {
"wood": "Yew",
"core": "Phoenixfeather",
"length": 9
},
"friends": [
{
"name": "HarryPotter",
"age": 18,
"house": "Gryffindor",
"occupation": "Auror"
},
{
"name": "LunaLovegood",
"age": 17,
"house": "Ravenclaw",
"occupation": "Magizoologist"
},
{
"name": "NevilleLongbottom",
"age": 18,
"house": "Gryffindor",
"occupation": "ProfessorofHerbology"
}
],
"enemies": [
{
"name": "TomRiddle",
"alias": "LordVoldemort"
},
{
"name": "BellatrixLestrange",
"alias": "Bella"
}
],
"patronus": "Horse"
},
{
"name": "DracoMalfoy",
"age": 18,
"house": "Slytherin",
"wand": {
"wood": "Hawthorn",
"core": "Unicornhair",
"length": 10
},
"friends": [
{
"name": "VincentCrabbe",
"age": 18,
"city": "England",
"country": "UK",
"occupation": null
},
{
"name": "GregoryGoyle",
"age": 18,
"city": "England",
"country": "UK",
"occupation": null
}
],
"enemies": [
{
"name": "HarryPotter",
"age": 17,
"house": "Gryffindor",
"occupation": null
},
{
"name": "HermioneGranger",
"age": 17,
"house": "Gryffindor",
"occupation": null
},
{
"name": "RonWeasley",
"age": 17,
"house": "Gryffindor",
"occupation": null
}
],
"patronus": null
}
]
