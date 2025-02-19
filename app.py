from flask import Flask, render_template, request, redirect, url_for, session
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure secret key

@app.route('/')
def index():
    scraped_content = session.pop('scraped_content', None)
    return render_template('index.html', scraped_content=scraped_content)

@app.route('/scrape_blog', methods=['POST'])
def scrape_blog():
    blog_url = request.form['blog_url']
    response = requests.get(blog_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    paragraphs = soup.find_all('p')
    blog_content = '\n'.join([p.get_text() for p in paragraphs])
    
    session['scraped_content'] = blog_content
    
    return redirect(url_for('index'))

@app.route('/save_note', methods=['POST'])
def save_note():
    note = request.form['note']
 
    print(note)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)