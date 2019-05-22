from bottle import request, route, run, jinja2_view
from amazon_review_classifier.review_classifier import getProbaList

@route('/')
@jinja2_view('index.html')
def index():
	paths = [
		{'link': '/classify', 'name': 'Amazon review classifier'}
	]
	return dict(paths=paths)

@route('/classify')
@jinja2_view('classification.html')
def classify():
	review = request.query.review

	if review:
		probaList = getProbaList(review)
		return dict(probaList=probaList, review=review)
	else:
		return {}
	

# run(host='localhost', port=8092, reloader=True, debug=True)
# to run via command line : ython -m bottle --debug --reload --bind localhost:8092 bottle_app
