import streamlit as st
import streamlit.components.v1 as stc
import requests

base_url = "https://raw.githubusercontent.com/swatichauhan08/job-recommendation/main/Recommendation%20Model.py"

def get_data(url):
    resp.requests.get(url)
    return resp.json()

html_template = """
<div>
<h4>{}</h4>
<h4>{}</h4>
<h4>{}</h4>
<h4>{}</h4>
</div>
"""
resume_html = """
<div style = 'color:#fff'>
{}
</div>
"""
    
def main():
    menu = ["Home","About"]
    choice = st.sidebar.selectbox("Menu",menu)
    
    st.title("Job Search Portal - IT")
    
    if choice == "Home":
        st.subheader("Home")
        with st.form(key = 'searchform'):
            nav1,nav2,nav3,nav4,nav5,nav6 = st.beta_columns([3,2,1])
            
            with nav1:
                search_term = st.text_input("Search Candidates")
            with nav2:
                search_term = st.text_input("Location")
            with nav3:
                search_term = st.text_input("Years of Experience")
            with nav4:
                search_term = st.text_input("Salary")
            with nav5:
                st.text("Search")
                submit_search = st.form_submit_button(label = 'Search')
        st.success("You searched for {} in {}".format(search_term,location))
        
        col1,col2 = st.beta_columns([2,1])
        with col1:
            if submit_search:
                search_url = base_url.format(search_term,location)
                # st.write(search_url)
                data = get_data(search_url)
                num_results = len(data)
                st.subheader("Showing {} of candidates".format(num_results))
                
                for i in data:
                    job_category = i['category']
                    job_location = i['location']
                    job_exp = i['experience']
                    job_resume = i['resume']
                    job_salary = i['salary']
                  #  job_company = i['company']
                    st.markdown(html_template.format(job_category,job_location,job_exp,job_salary,
                                                     unsafe_allow_html = True)
    else:
        st.subheader("About")
