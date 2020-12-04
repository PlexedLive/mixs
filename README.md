# Data analysis
- Project name: mixs
- Description: Audio signal splitter
- Data Source: MUSDB18
- Type of analysis: Machine/Deep Learning

# This is the production branch

# Startup the project

The initial setup.

Create virtualenv and install the project:
```bash
  $ sudo apt-get install virtualenv python-pip python-dev
  $ deactivate; virtualenv ~/venv ; source ~/venv/bin/activate ;\
    pip install pip -U; pip install -r requirements.txt
```

Unittest test:
```bash
  $ make clean install test
```

Check for mixs in gitlab.com/{group}.
If your project is not set please add it:

- Create a new project on `gitlab.com/{group}/mixs`
- Then populate it:

```bash
  $ ##   e.g. if group is "{group}" and project_name is "mixs"
  $ git remote add origin git@gitlab.com:{group}/mixs.git
  $ git push -u origin master
  $ git push -u origin --tags
```

Functional test with a script:
```bash
  $ cd /tmp
  $ mixs-run
```
# Install
Go to `gitlab.com/{group}/mixs` to see the project, manage issues,
setup you ssh public key, ...

Create a python3 virtualenv and activate it:
```bash
  $ sudo apt-get install virtualenv python-pip python-dev
  $ deactivate; virtualenv -ppython3 ~/venv ; source ~/venv/bin/activate
```

Clone the project and install it:
```bash
  $ git clone gitlab.com/{group}/mixs
  $ cd mixs
  $ pip install -r requirements.txt
  $ make clean install test                # install and test
```
Functional test with a script:
```bash
  $ cd /tmp
  $ mixs-run
```

# Continuous integration
## Github
Every push of `master` branch will execute `.github/workflows/pythonpackages.yml` docker jobs.
## Gitlab
Every push of `master` branch will execute `.gitlab-ci.yml` docker jobs.
