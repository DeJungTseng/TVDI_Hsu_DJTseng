from flask import Flask

app = Flask(__name__)

# route : 路徑，running on the location 
@app.route("/")
def hello_world():
    return '''
        <h1>喔齁齁齁齁</h1>
        <h2>天線寶寶說尼豪</h2>
        <ul>
        <li>喵咪喵喵</li>
        <li>啾啾啾啾</li>
        </ul>'''

@app.route("/name")
def hello_world1():
    return '''
        <h1>唉油油油</h1>
        <h2>鼻要</h2>
        <ul >
            <li><a href="/">About</a></li>
            <li><a href="/meow">News</a></li>
            <li><a href="">Story</a></li>
            <li><a href="">Online</a></li>
            <li><a href="">Services</a></li>
            <li><a href="">Contact</a></li>
        </ul>'''

@app.route("/meow")
def hello_world2():
    return '''
        <div class="construction">
            <h1>尼點進了喵</h1>
            <h2>We are sustainable construction</h2>
            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Expedita eos sapiente numquam culpa nulla, recusandae deserunt vitae blanditiis adipisci atque corrupti harum enim delectus nostrum? Assumenda illo amet optio temporibus.
            </p>
            <a href="/name">Read more</a>
        </div>'''