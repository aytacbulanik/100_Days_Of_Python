from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p> \
            <h1 style='color: blue; text-align: center;'>Hello, World!</h1> Merhaba</p>" \
              "<img src='https://media.giphy.com/media/ASd0Ukj0y3qMM/giphy.gif' alt='giphy'>"

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