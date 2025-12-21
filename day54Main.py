from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bye")
def bye_world():
    return "<p>Goodbye, World!</p>"

#username değişkeni tanımlayarak kullanıcı adını dinamik olarak alır
@app.route('/user/<username>/<int:age>')
def show_user_profile(username, age):
    return f'Hello : {username} how are you? You are {age} years old.'

if __name__ == "__main__":
    app.run(debug=True) #debug=True ile uygulama hata ayıklama modunda çalışır.
    # Bu, kodda yapılan değişikliklerin otomatik olarak algılanmasını sağlar.