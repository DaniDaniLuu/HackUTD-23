from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

#importing our routes
# note that you should change these imports later according to our own route names.
from routes import input_bp, calc_bp, analyze_bp
app.register_blueprint(input_bp.bp)
app.register_blueprint(calc_bp.bp)
app.register_blueprint(analyze_bp.bp)




if __name__ == '__main__':
    app.run(debug=True)