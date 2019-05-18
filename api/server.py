from flask import Flask, request, jsonify
from flask_caching import Cache

from sites import Check

config = {
    "CACHE_TYPE": "simple",
    "CACHE_DEFAULT_TIMEOUT": 300
}

app = Flask(__name__)
app.config.from_mapping(config)
cache = Cache(app)

@app.route('/api')
async def get():
    email = request.args.get('email')
    checker = Check(email, false, false)
    instagram_response = await checker.instagram_check()
    twitter_response = await checker.twitter_check()
    snapchat_response = await checker.snapchat_check()
    facebook_response = await checker.facebook_check()
    youtube_response = await checker.yougoogle_check()
    google_response = await checker.yougoogle_check()
    twitch_response = await checker.twitch_check()
    return {'instagram': instagram_response,
        'twitter':twitter_response,'snapchat':snapchat_response,'facebook':facebook_response,'youtube':youtube_response,'google':google_response,'twitch':twitch_response}

@app.route('/api')
@cache.cached(timeout=50)
async def start():
    result = get()
    return jsonify(result)

@app.route('/')
def index():
    return 'Nothing to see here.'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')

