run-debug:
	flask --debug run
run-demo:
	gunicorn3 -e SCRIPT_NAME=/hackaday/adventure --bind 0.0.0.0:8028 app:app
