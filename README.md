# graylist
API to list your servers

**Disclaimer**: this is the very very very first version(if it's possible to say that). 
I just wanted to share something that works and improve it as the time pass.

## How to install and run locally##
### Prepare your local mongodb and add some values ###
1 - Start mongodb<br>
2 - Connect to your mongodb: `$ mongo`<br>
3 - Add some values to your db<br>
```
> db.servers.insert( { project: 'my_project', server: 'server1' } );
> db.servers.insert( { project: 'my_project', server: 'server2' } );
> db.servers.insert( { project: 'my_project', instance: 'backend', server: 'backend1' } );
> db.servers.insert( { project: 'my_project', instance: 'backend', server: 'backend2' } );
```

### Installing and runnning the app ###
1 - Create a new virtualenv<br>
2 - `pip install -r requirements.txt`<br>
3 - `python src app.py`<br>
4 - Open your browser and try some url:

http://127.0.0.1:8000/project/myproject<br>
http://127.0.0.1:8000/project/myproject/instance/backend
