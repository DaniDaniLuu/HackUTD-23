from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

#importing our routes
# note that you should change these imports later according to our own route names.
from routes import index, user, post
app.register_blueprint(index.bp)
app.register_blueprint(user.bp)
app.register_blueprint(post.bp)




if __name__ == '__main__':
    app.run(debug=True)