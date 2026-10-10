from fastapi import FastAPI
from numpy.random import sample

from models import Project, Developer

app=FastAPI()
@app.post('/developer')
def create_developer(developer:Developer):
    return {"message":"Developer created seccessfully", "developer":developer}


@app.post('/project')
def create_project(project:Project):
    return {"message":"Project created seccessfully!","project":project}

@app.get('/project')
def get_projects():
    developer=Developer(name="Uvejs Bossi",experience=2)
    sample_project:Project=Project(title="HR Managment System", description="This is a sample project",
                                   languages=["Python","JavaScripe","SQL"],lead_developer=developer)
    return {"projects":[sample_project]}
