import requests

url = "https://wearedevs.net/api/obfuscate"

script = input("Write A Script//Escreva Um Script: ")
data = {
    "script" : script
}

request = requests.post(url, data=data)
response = request.json()

scripot = response["obfuscated"]

with open("obfuscated.txt", "w") as script:
    script.write(scripot)
    print("Script Saved//Script Salvo")