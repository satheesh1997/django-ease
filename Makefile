doc:
	rm -rf documentation && cd docs && make html && sphinx-build -b rinoh source _build/rinoh && cp -r build/html ../documentation