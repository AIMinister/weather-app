# -------- CONFIG --------
PACKAGE_NAME=weather-app-vkyei

# -------- CLEAN --------
clean:
	rm -rf dist build *.egg-info

# -------- BUILD --------
build: clean
	uv build

# -------- INSTALL LOCAL --------
install:
	pip install dist/*.whl

# -------- PUBLISH TO PYPI --------
publish:
	uv run twine upload dist/*
	