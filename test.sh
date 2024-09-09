SET ENV="test"
clear && pytest ./test/ -s
rm -rf .pytest_cache __pycache__ 