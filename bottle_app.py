from bottle import request, route, get, post, run, jinja2_view, HTTPError
import amazon_review_classifier.review_classifier as review_classifier
import seed_disperser.seed_disperser as seed_disperser

@route('/')
@jinja2_view('index.html')
def index():
	paths = [
		{'link': '/classify', 'name': 'Amazon review classifier'},
        {'link': '/seed-disperser', 'name': 'Seed disperser'}
	]
	return dict(paths=paths)

@get('/classify')
@jinja2_view('classification.html')
def classify():
	review = request.query.review

	if review:
		probaList = review_classifier.getProbaList(review)
		return dict(probaList=probaList, review=review)
	else:
		return {}
	

@post('/seed-disperser')
def disperse():
    length = int(request.forms.get('length'))
    width = int(request.forms.get('width'))

    canopy = int(request.forms.get('canopy'))
    tree_stratum = int(request.forms.get('tree_stratum'))
    understorey = int(request.forms.get('understorey'))
    shrub_layer = int(request.forms.get('shrub_layer'))
    
    seeds_stocks = {
    'canopy' : canopy,
    'tree_stratum' : tree_stratum,
    'understorey' : understorey,
    'shrub_layer' : shrub_layer
    }

    verify_disperse_params(length, width, seeds_stocks)
    
    fig, ax = seed_disperser.disperse_seeds(seeds_stocks, length, width)
    svg_data = seed_disperser.get_svg(fig)

    return svg_data

@get('/seed-disperser')
@jinja2_view('seed_disperser.html')
def seed_disperser_index():
	return {}
    # https://stackoverflow.com/questions/25069898/display-mpld3-chart-in-html-with-django
    # save temp img file and return img https://stackoverflow.com/questions/5515278/plot-matplotlib-on-the-web

def verify_disperse_params(length, width, seeds_stocks):
    seeds_count = length * width * 3
    seed_sum = sum(seeds_stocks.values())

    if (seed_sum != seeds_count) :
        raise HTTPError(status=400, body="Bad parameters, seed count does not equals length * with * 3")

# run(host='localhost', port=8092, reloader=True, debug=True)
# to run via command line : python -m bottle --debug --reload --bind localhost:8092 bottle_app
