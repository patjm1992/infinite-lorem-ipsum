from flask import Flask, render_template
import markov

# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/generate')
def generate():
	word_ct = 150

	text = markov.main(word_ct)
	text_2 = markov.main(word_ct)
	text_3 = markov.main(word_ct * 2)
	word_list = text.split()

	p1 = text
	p2 = text_2
	p3 = text_3

	return render_template('index.html', p1=p1, p2=p2, p3=p3)


if __name__ == '__main__':
	app.run(host='0.0.0.0')
