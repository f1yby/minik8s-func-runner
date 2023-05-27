SRC = src
REPO ?= lwsg
IMAGES := $(notdir $(wildcard $(SRC)/*))
DOCKER_BUILD = docker build
DOCKER_BUILDFLAG = -t
DOCKER_IMAGE_REMOVE = docker image rm


.PHONY: all
all: images

.PHONY: images
images:
	$(foreach image,$(IMAGES),$(DOCKER_BUILD) $(DOCKER_BUILDFLAG) $(REPO)/$(image) $(SRC)/$(image);)


.PHONY: clean
clean: clean_images

.PHONY: clean_images
clean_images:
	$(foreach image,$(IMAGES),$(DOCKER_IMAGE_REMOVE) $(REPO)/$(image);)