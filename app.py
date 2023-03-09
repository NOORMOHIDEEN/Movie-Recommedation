from flask import Flask,render_template
from bs4 import BeautifulSoup as SOUP 
import re 
import requests as HTTP

app = Flask(__name__)
 
app.debug = True

@app.route('/')
def form():
    return render_template('index.html')
 
@app.route('/enjoy')
def enjoy():
    urlhere = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'
    arr=movie(urlhere,"Enjoy")  
    return render_template("enjoy.html",url=urlhere,arr=arr)

@app.route('/anger')
def anger():
    urlhere = 'http://www.imdb.com/search/title?genres=family&title_type=feature&sort=moviemeter, asc'
    arr=movie(urlhere,"Anger")  
    return render_template("enjoy.html",url=urlhere,arr=arr)




def movie(urlhere,emotion):
    response = HTTP.get(urlhere) 
    data = response.text


    # Parsing the data using 
    # BeautifulSoup 
    soup = SOUP(data, "lxml") 
          
    # Extract movie titles from the 
    # data using regex 
    title = soup.find_all("a", attrs = {"href" : re.compile(r'\/title\/tt+\d*\/')}) 
    count = 0	
    k=0
    arr=[]
    if(emotion == "Disgust" or emotion == "Anger" or emotion=="Surprise"):
        for i in title:
            # Splitting each line of the 
            # IMDb data to scrape movies 
            tmp = str(i).split('>')
            
            if(len(tmp) == 3):
                arr.append(tmp[1][:-3])

            if(count > 13):
                break
            count += 1
            
    else:
        for i in title:
            tmp = str(i).split('>') 
                
            if(len(tmp) == 3): 
                arr.append(tmp[1][:-3])
                  
            if(count > 11):
                break
            count+=1  
    return arr
app.run(host='localhost', port=5000)