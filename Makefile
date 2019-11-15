.PHONY: all


all:
	@(echo "Installing required repositories and packages..")
	curl -sL https://rpm.nodesource.com/setup_13.x | sudo bash - 
	yum install -y epel-release 
	yum install -y git nodejs nginx python3 python-pip
	pip install pipenv
        pipenv install
	@(echo "Setting up front end..")
	\cp -f nginx/spamfilter /etc/nginx/nginx.conf
	if [[ ! ( -f /etc/pki/tls/private/server.key && -f /etc/pki/tls/certs/server.crt ) ]] ; \
        then \
            echo "Generating new server certificates"; \
            openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/pki/tls/private/server.key -out /etc/pki/tls/certs/server.crt
        fi
	cd ui && make deployment
	service nginx restart
	cd ..
	@(echo "Deployment complete!")
	@(echo "At the project root, run 'pipenv shell' to import development environment,")
	@(echo "then start the api with 'supervisorctl start api'")
