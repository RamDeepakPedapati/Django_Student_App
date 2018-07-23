import MySQLdb
import click
import openpyxl
import json
import requests


@click.group()

def request():
    "Commands for weather info"
    pass


@request.command()
@click.argument('cityid')
def getcityinfo(cityid):
    url = "http://api.openweathermap.org/data/2.5/weather?id="+cityid+"&appid=1d65a56ababbf74875637da19c78ca78"
    print(url)
    response = requests.get(url)
    json_data = json.loads(response.text)
    print(json_data)

request()