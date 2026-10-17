import streamlit as st
import requests
import pandas as pd

st.title("Project Managment App")
st.header("Add a Developer")
dev_name=st.text_input("Developer Name", key="1")
dev_exeperience=st.number_input("Exeperience (Years)", min_value=0, max_value=50, value=0, key="ex1")

if st.button("Create Developer"):
    dev_data={"name":dev_name,"experience":dev_exeperience}
    response=requests.post("http://127.0.0.1:8000/developer", json=dev_data)
    st.json({"json":response.json(),"status":response.status_code})


st.header("Add a Project")
proj_title=st.text_input("Project Title")
proj_desc=st.text_area("Project Description")
proj_langs=st.text_input("Languages Used ")
lead_dev_name=st.text_input("dev name", key="2")
lead_dev_exp=st.number_input("Exp (Years)", min_value=0, max_value=50, value=0, key="ex2")

if st.button("Create Project"):
    lead_dev_data={"name":lead_dev_name,"exeperience":lead_dev_exp}
    proj_data={"title":proj_title,"description":proj_desc,
               "languages":proj_langs.split(","),
               "lead_developer":lead_dev_data}
    response=requests.post("http://127.0.0.1:8000/project", json=proj_data)
    st.json({"json":response.json(),"status":response.status_code})

st.header("project dashboard")
if st.button("get projects"):
    response=requests.get("http://127.0.0.1:8000/project")
    project_data=response.json()['projects']

    if project_data:
        project_df=pd.DataFrame(project_data)
        st.subheader("Projects Overview")
        st.dataframe(project_df)

        st.subheader("Project Details")
        for project in project_data:
            st.markdown(f"### {project['title']}")
            st.markdown(f"**Description:** {project['description']}")
            st.markdown(f"Language Used:{', '.join(project['languages'])}")
            st.markdown(f"Developer Name: {project['lead_developer']['name']}")
            st.markdown("----")

    else:
        st.warning("No project found")


