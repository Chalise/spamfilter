.PHONY: all


all:
	@(echo "Installing required repositories and packages..")
	curl -sL https://rpm.nodesource.com/setup_13.x | sudo bash - 
	yum install -y epel-release 
	yum install -y nodejs nginx python3 python-pip
	pip install pipenv
	pipenv install
	@(echo "Setting up API")
	pipenv shell
	supervisord
	supervisorctl start api
	@(echo "Setting up web client..")
	\cp -f nginx/spamfilter /etc/nginx/nginx.conf
	if [[ ! ( -f /etc/pki/tls/private/server.key && -f /etc/pki/tls/certs/server.crt ) ]] ; \
        then \
            echo "Generating new server certificates"; \
            openssl req -x509 -nodes -subj '/CN=localhost' -days 365 -newkey rsa:2048 -keyout /etc/pki/tls/private/server.key -out /etc/pki/tls/certs/server.crt; \
        fi
	cd ui && make deployment
	service nginx restart
	cd ..
	@(echo "Deployment complete!")
