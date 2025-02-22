from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    projects = [
        {'name': 'Soon Golf', 'logo': 'static/images/logo1.png', 'link': 'https://long-as-python.itch.io/soongolf'},
        {'name': 'Apriori Worm', 'logo': 'static/images/logo2.png', 'link': 'https://long-as-python.itch.io/apriori-puzzle'},
        {'name': 'Abstract Fishing', 'logo': 'static/images/logo3.png', 'link': 'https://long-as-python.itch.io/abstract-fishing'},
        {'name': 'Zoo keeper', 'logo': 'static/images/logo4.png', 'link': 'https://teamon.itch.io/zoo-keeper'},
        {'name': 'Cooking Rise', 'logo': 'static/images/logo5.png', 'link': 'https://magicus-games.itch.io/cooking-rice'},
        {'name': 'CALDERA ESCAPE', 'logo': 'static/images/logo6.png', 'link': 'https://noctis-requiem.itch.io/caldera-escape'},
        {'name': 'Fluent knife', 'logo': 'static/images/logo7.png', 'link': 'https://noctis-requiem.itch.io/fluent-knife'},
        {'name': 'Last Shogun', 'logo': 'static/images/logo8.png', 'link': 'https://noctis-requiem.itch.io/lastshogun'},
        {'name': 'Piggy To The Stars', 'logo': 'static/images/logo9.png', 'link': 'https://noctis-requiem.itch.io/piggy-to-the-stars'},
        {'name': 'Story Protocol', 'logo': 'static/images/logo10.png', 'link': 'https://noctis-requiem.itch.io/story-protocol-legacy-of-the-warrior'},
        {'name': 'Wormhole Alchemist', 'logo': 'static/images/logo11.png', 'link': 'https://noctis-requiem.itch.io/wormhole-alchemist'},
        {'name': 'Flappy Piggy', 'logo': 'static/images/logo12.png', 'link': 'https://noctis-requiem.itch.io/flappy-piggy'},
        {'name': 'Infinit blocks', 'logo': 'static/images/logo13.png', 'link': 'https://cryplex.itch.io/infinit-blocks'},
        {'name': 'Shogun tower', 'logo': 'static/images/logo14.png', 'link': 'https://cryplex.itch.io/shogun-tower'},
        {'name': 'My shell bubble', 'logo': 'static/images/logo15.png', 'link': 'https://myshellbubble.surge.sh/'}
    ]
    return render_template('index.html', projects=projects)

if __name__ == '__main__':
    app.run(debug=True)
