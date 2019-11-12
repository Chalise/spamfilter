.PHONY: clean

clean:
	rm -rf build
	rm -rf /var/www/spamfilter

build:
	npm run-script build

deployment: build
	cp -r build /var/www/spamfilter
