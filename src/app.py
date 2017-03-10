from flask import Flask
from database import Database
from utils import query_servers, query_result_to_str
app = Flask(__name__)

Database.initialize()


@app.route('/')
def index():
    return 'List your servers'


@app.route('/project/<project>')
def show_servers_project(project):
        query_result = query_servers({'project':project})
        return query_result_to_str(query_result)


@app.route('/project/<project>/instance/<instance>')
def show_servers_instance(project, instance):
    query_result = query_servers({'project': project, 'instance': instance})

    return query_result_to_str(query_result)

if __name__ == '__main__':
    app.run(debug=True, port=8000)