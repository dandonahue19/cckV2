cckV2

# make virtual env using python 3.5>
# install dependencies in requirements.txt
`source vEnv/bin/active`
`pip install -r requirements.txt`

# install client dependencies from package.json
# run in frontend folder
`npm install`

# build frontend package
# build alias defined in package.json
`npm run build`

# start vue server for hot reloading frontend changes
# serve alias defined in package.json
`npm run server`

# push process to background or open new shell window

# apply db migrations (this step creates db tables and applies model changes to those tables)
`python manage.py migrate`

# start api on django dev server 
# run in server folder in virtual env
`python manage.py runserver`

# visit site at localhost:8080
# visit django admin page localhost:8000/admin
