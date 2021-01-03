# Automate Stuffs with Python

Just some random scripts that can help you in your routine

## Regular Expression Project

This project apply a regex syntax to find emails and phones numbers in pdf file, passing the data to a csv file and, also, you can attach this file in a email.

To run the code, you can follow this steps.

First, create `.env` file after you clone the project. Just run in terminal:

```
make env
```

Open the `.env` file and set your own email and password, like this:

```
EMAIL_USER='your_email@gmail.com'
EMAIL_PASSWORD='your_password'
```

Make sure the receiver email will be able to receive messages from a python script. To do this, activate [less secure apps](https://myaccount.google.com/lesssecureapps) to send emails.

Install dependencies and open a poetry virtual env. If you donte have any poetry installed in your machine, take a look in [documentation](https://python-poetry.org/):

```
poetry install
poetry shell
```

To create the csv_file, run:

```
make csv_file
```

And than, send the email:

```
make send_email
```

If you want to debug your email message, you can find a little test running in one terminal:

```
make email_debug
```

And, in another terminal, send a email message:

```
make send_email_debugmode
```

Something like this will appear in the first terminal:

```
---------- MESSAGE FOLLOWS ----------
b'Subject: Just a test'
b'From: your_email@gmail.com'
b'To: your_email@gmail.com'
b'Content-Type: text/plain; charset="utf-8"'
b'Content-Transfer-Encoding: 7bit'
b'MIME-Version: 1.0'
b'X-Peer: 127.0.0.1'
b''
b'This is the body of my test, sending email to myself!'
------------ END MESSAGE ------------

```