import sys, logging, time, random
import web
from Temperature import Temperature
from Application import Application

# Mapping between the urls used by the frontend to objects on the backend
urls = ( '/', 'Application')

def init_loggers():
	# tune down logging inside Intellect
	logger = logging.getLogger('intellect')
	logger.setLevel(logging.ERROR)
	consoleHandler = logging.StreamHandler(stream=sys.stdout)
	consoleHandler.setFormatter(logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s%(message)s'))
	logger.addHandler(consoleHandler)	

	# set up logging for the example
	logger = logging.getLogger('ArrowSelection')
	logger.setLevel(logging.DEBUG)

	consoleHandler = logging.StreamHandler(stream=sys.stdout)
	consoleHandler.setFormatter(logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s%(message)s'))
	logger.addHandler(consoleHandler)


def init_webserver():
	#
	app = web.application(urls, globals())	
	app.run()


def main():
	init_loggers()

	# Initialize the rule engine framework
	logging.getLogger('ArrowSelection').debug('Creating reasoning engine.')

	# Initialize the web server and listen to requests
	init_webserver()


if __name__ == '__main__':
	main() 