# Bowling Game

## previus requeriments

- **python 3.6** or superior 
- **virtualenv**

## create and activate virtualenv

### create 
`virtualenv env --python=3.6`
    
### activate
`source env/bin/activate`

## install dependencies 
`pip install -r requeriments.txt`

## set variables in settings file
- copy and rename file `settings.cfg.sample` to `settings.cfg`
- set variable `DEBUG = False` in settings file `settings.cfg` to run in production mode

## run server 
`python run.py`

##endpoint to calculate score
### url
`POST /api/v1/score` 

### request example
```javascript
{
    "rolls": "XXXXXXXXXXXX"
}
```

### responser example
```javascript
{
    "score": 300
}
```