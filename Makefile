DOCKER_IMAGE = my_docker
DOCKER_ARGS := --rm -v $(CURDIR):$(CURDIR) -w $(CURDIR)
DOCKER_RUN = docker run -t $(DOCKER_ARGS) $(DOCKER_IMAGE)

enter_container: build_image
		docker run -it $(DOCKER_ARGS) $(DOCKER_IMAGE)

run: build_image
		$(DOCKER_RUN) $(command)

run_pwd: build_image
		$(DOCKER_RUN) pwd

build_image:
		docker build -t $(DOCKER_IMAGE) .
