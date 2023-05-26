SRC = src
DEST = build
ENCODER = tools/encoder
SRC_EXAMPLE = examples
FILES_EXAMPLE := $(wildcard $(SRC_EXAMPLE)/*)
DEST_EXAMPLE = $(DEST)/examples

.PHONY: error
error:
	@echo "Please choose one of the following targets: example, image, clean"

$(DEST_EXAMPLE):
	mkdir -p $(DEST_EXAMPLE)

.PHONY: example
example: $(FILES_EXAMPLE) $(DEST_EXAMPLE)
	$(foreach file,$(FILES_EXAMPLE),$(ENCODER) $(file) > $(DEST_EXAMPLE)/$(notdir $(file)).base64;)

.PHONY: image
image:
	docker build -t lwsg/func-runner $(SRC)

.PHONY: clean
clean:
	rm -rf $(DEST)

