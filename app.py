from flask import Flask, render_template, request
import praw
import random

app = Flask(__name__)
def get_meme_image_from_keyword(keyword: str):
    # Initialize Reddit client
    reddit = praw.Reddit(
        client_id="IjV9yWii1sPp-4R52Ps_4A",
        client_secret="LSwmQG3Briq18S4HJwUEDUMJdsQpdA",
        user_agent="script:lucbday:v1.0 (by u/East-Cap-7653)"
    )

    # Search for posts in r/memes containing the keyword
    subreddit = reddit.subreddit("memes")
    search_results = subreddit.search(keyword, limit=10)
    search_results = [
        submission for submission in search_results
        if not submission.over_18 and submission.url.endswith(('.jpg', '.jpeg', '.png', '.gif'))]
    submission = random.choice(search_results)
    return submission.url  # Return only the image URL
    

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/meme', methods=['GET', 'POST'])
def meme():
    if request.method == 'POST':
        if 'random' in request.form:
            random_keywords = ['funny', 'cats', 'dogs', 'relatable', 'gaming', 'sports', 'comical', 'puppy', 'volleyball', 'school', 'dark', 'fun', 'happy', 'brainrot', 'skibidi', 'sigma', 'music']
            keyword = random.choice(random_keywords)
            meme_image_url = get_meme_image_from_keyword(keyword)
            return render_template('index.html', meme_image_url=meme_image_url)
        keyword = request.form['keyword']
        meme_image_url = get_meme_image_from_keyword(keyword)
        if meme_image_url:
            return render_template('index.html', meme_image_url=meme_image_url)
    return render_template('index.html', meme_image_url=None)

if __name__ == '__main__':
    app.run( host='0.0.0.0', port=5000, debug=True)
