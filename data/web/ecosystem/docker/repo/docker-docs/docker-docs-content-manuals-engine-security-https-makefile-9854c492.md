---
                    {
  "source": "docsrepo",
  "label": "docker-docs",
  "repo_url": "https://github.com/docker/docs.git",
  "ref": "main",
  "commit": "202475fe91af5b37340ed5bfe7f4c35bcce85e2c",
  "path_in_repo": "content/manuals/engine/security/https/Makefile",
  "description": "Docker documentation website content (docker/docs repo).",
  "license": "Docker documentation (see docker/docs repository for license)",
  "collected_at": "2025-12-15T17:38:12.985819+00:00"
}
                    ---
                    # content/manuals/engine/security/https/Makefile


HOST:=boot2docker

makescript:
	./parsedocs.sh > make_certs.sh

build: clean makescript
	docker build -t makecerts .

cert: build
	docker run --rm -it -v $(CURDIR):/data -e HOST=$(HOST) -e YOUR_PUBLIC_IP=$(shell ip a | grep "inet " | sed "s/.*inet \([0-9.]*\)\/.*/\1/" | xargs echo | sed "s/ /,IP:/g") makecerts

certs: cert

run:
	sudo dockerd -D --tlsverify --tlscacert=ca.pem --tlscert=server-cert.pem --tlskey=server-key.pem -H=0.0.0.0:6666 --pidfile=$(pwd)/docker.pid --graph=$(pwd)/graph

client:
	sudo docker --tls --tlscacert=ca.pem --tlscert=cert.pem --tlskey=key.pem   -H=$(HOST):6666 version
	sudo docker --tlsverify --tlscacert=ca.pem --tlscert=cert.pem --tlskey=key.pem   -H=$(HOST):6666 info
	sudo curl https://$(HOST):6666/images/json --cert ./cert.pem --key ./key.pem --cacert ./ca.pem

clean:
	rm -f ca-key.pem ca.pem ca.srl cert.pem client.csr extfile.cnf key.pem server-cert.pem server-key.pem server.csr extfile.cnf
