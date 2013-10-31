def mtgCardRequest(cardname):

	import requests
	import json

	#TCGplayer, this gives 3 outputs. Low, Median, High
	tcgplayer_response = requests.get('http://magictcgprices.appspot.com/api/tcgplayer/price.json?cardname=%s' % (cardname))
	tcg_data = json.loads(tcgplayer_response.text)

	#set variable for each different api location
	tcg_low = tcg_data[0]
	tcg_mid = tcg_data[1]
	tcg_high = tcg_data[2]

	all_prices = {
		'Low' : tcg_low,
		'Median' : tcg_mid,
		'High' : tcg_high
	}

	return all_prices

if __name__ == "__main__":
	import sys
	# cardname = sys.argv[1]
	# cardset = sys.argv[2]
	cardname = raw_input("What card do you want? ")
	print mtgCardRequest(cardname)
