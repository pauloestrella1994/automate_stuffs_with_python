env:
	cp local.env .env

email_debug:
	python -m smtpd -c DebuggingServer -n localhost:1025

send_email_debugmode:
	python regular_expressions/project/send_email_debugmode.py