GITHUB=https://api.github.com/markdown

html: *.txt
	$(eval TARGET := $(addsuffix .html,$(basename $<)))
	python txt2json.py < $< | curl $(GITHUB) -sLk -XPOST -d @- > $(TARGET)
	python insert.py index.tmpl < $(TARGET) > index.html
	rm $(TARGET)
