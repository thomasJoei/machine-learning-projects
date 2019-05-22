from joblib import dump, load
import os.path

currentDir = os.path.dirname(os.path.abspath(__file__))
clf = load( currentDir + '/data/bayes_classifier.joblib') 

categoryDict = {
"Automotive": "Automotive",
"Beauty": "Beauty",
"Books": "Books",
"Clothing_Shoes_and_Jewelry": "Clothing, Shoes and Jewelry",
"Digital_Music": "Digital Music",
"Electronics": "Electronics",
"Grocery_and_Gourmet_Food": "Grocery and Gourmet Food",
"Home_and_Kitchen": "Home and Kitchen",
"Sports_and_Outdoors": "Sports and Outdoors",
"Toys_and_Games": "Toys and Games",
}

def getProbaList(review):
	probas = clf.predict_proba([review])[0]
	
	# category keys in alphabetical order (same as the classifier is outputting them)
	categorySortedKeys = sorted(categoryDict.keys())
	details = map(lambda catKey,proba: {'name': categoryDict.get(catKey), 'key': catKey, 'proba':  round(proba * 100, 3) }, categorySortedKeys, probas)

	return sorted(details, key = lambda i: i['proba'], reverse=True) 
