DEPLOYMENT_DIR = /var/www/
NAME = spamfilter

.PHONY: clean spotless deployment

clean:
	rm -rf build

spotless: clean
	rm -rf /var/www/spamfilter

build: node_modules
	npm run-script build

deployment: spotless build
	mkdir -p /var/www
	cp -r build /var/www/spamfilter
	restorecon -R /var/www

node_modules:
	npm install
