import httplib

coinUserInput = raw_input('\nEnter the coin name\n')
#ask user for a coin; store result as a string
def getCoinData(coinName):
	hostConnection = httplib.HTTPSConnection('api.coinmarketcap.com')
	#new HTTPS connection to CoinMarketCap's API
	hostConnection.connect()
	#open connection
	coinConverted = coinName.lower()
	#convert user input string to lowercase
	baseURL = '/v1/ticker/'                           
	#this is the location that contains ticker data for every coin they list
	coinURL = baseURL+coinConverted+'/'
	#concatenate the base URL wit h the user input string to generate a path that will retrieve the coin data from CoinMarketCap
	hostConnection.request('GET',coinURL)
	#send CoinMarketCap a GET request for the coin using the URL we just created
	hostResponse = hostConnection.getresponse()
	#receive the response and store it in a variable
	data = hostResponse.read()
	#read the response as a string and store the string in a variable
	hostConnection.close()
	#close the connection to CoinMarketCap
	print data
	#show the user the coin data
	sendAnotherRequest = raw_input('\nWould you like to search again? (Please enter y or n and press enter) \n')
	#ask the user if they want to run the search again and store their response in a variable
	if sendAnotherRequest == 'y':
		anotherCoin = raw_input('\nEnter the coin name\n')
		#ask user for a coin; store result as a string
		getCoinData(anotherCoin)
		#if the user has entered y, run the search again
	else:
		print 'Thank you for using this tool'
		quit()
		#thank the user
getCoinData(coinUserInput)
#run the program initially
