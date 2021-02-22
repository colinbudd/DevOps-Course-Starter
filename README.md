# DevOps Apprenticeship: Project Exercise

## Getting started

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from a bash shell terminal:

### On macOS and Linux

```bash
source setup.sh
```

### On Windows (Using PowerShell)

```powershell
.\setup.ps1
```

### On Windows (Using Git Bash)

```bash
source setup.sh --windows
```

### Poetry

Install poetry.

## Execution

You have three choices for running the app:

1. Local execution
1. With Vagrant
1. With Docker

### Running the app locally

Start the app with:

```bash
flask run
```

You should see output similar to the following:

```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```

Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

### Running the app with Vagrant

```bash
vagrant up
```

## Notes

### .env

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like developement mode (which also enables features like hot reloading when you make a file change).

When running `setup.sh`, the `.env.template` file will be copied to `.env` if the latter does not exist.

### Trello Secrets

The `.env` file also holds Trello secrets. Edit this file to set the following values:

* TRELLO_TOKEN
* TRELLO_KEY
* TRELLO_BOARD_NAME
* TRELLO_BOARD_ID
