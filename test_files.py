import os
def test_ebookerpy():
	assert os.path.exists("ebooker.py")
def test_docs():
	assert os.path.exists("docs")
def test_readmemd():
	assert os.path.exists("README.md")
def test_webfiles():
	assert os.path.exists("docs/index.html")
	assert os.path.exists("docs/stylesheet.css")