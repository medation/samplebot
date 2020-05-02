# The conversationnal instance of covidbot


## How to install and run

Create & Activate virtual environment

```
virtualenv -p python3 <env_name>
```

```
cd <env_name> && source bin/activate
```

Install dependencies

```
pip install -r requirements.txt
```

```
python -m spacy download fr_core_news_sm
python -m spacy download fr
```

This will install the bot and all of its requirements.

Execute 

```
rasa train
rasa run --enable-api -p <port_nlu>
rasa actions -p <port_core>
```

## Overview of the files

`data/core` - contains stories 

`data/nlu` - contains example NLU training data

`actions.py` - contains custom action/api code

`domain.yml` - the domain file 

`config.yml` - the Rasa config file

`endpoints.yml` - the Rasa endpoints file ( actions & redis )
