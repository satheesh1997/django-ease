doc:
	rm -rf docs && cd docs_src && make html && sphinx-build -b rinoh source _build/rinoh && cp -r build/html ../docs
	touch docs/.nojekyll