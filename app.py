{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "d9133e2c",
   "metadata": {},
   "source": [
    "##### Creating the streamlit app"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ecc0c8de",
   "metadata": {},
   "outputs": [],
   "source": [
    "## Github Link: https://github.com/swatichauhan08/job-recommendation"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "fbab7ad6",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (3598374932.py, line 67)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  Input \u001b[0;32mIn [6]\u001b[0;36m\u001b[0m\n\u001b[0;31m    with st.beta_expander(\"Additional Information\")\u001b[0m\n\u001b[0m    ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import streamlit.components.v1 as stc\n",
    "import requests\n",
    "\n",
    "base_url = \"https://raw.githubusercontent.com/swatichauhan08/job-recommendation/main/Recommendation%20Model.py\"\n",
    "\n",
    "def get_data(url):\n",
    "    resp.requests.get(url)\n",
    "    return resp.json()\n",
    "\n",
    "html_template = \"\"\"\n",
    "<div>\n",
    "<h4>{}</h4>\n",
    "<h4>{}</h4>\n",
    "<h4>{}</h4>\n",
    "<h4>{}</h4>\n",
    "</div>\n",
    "\"\"\"\n",
    "resume_html = \"\"\"\n",
    "<div style = 'color:#fff'>\n",
    "{}\n",
    "</div>\n",
    "\"\"\"\n",
    "    \n",
    "def main():\n",
    "    menu = [\"Home\",\"About\"]\n",
    "    choice = st.sidebar.selectbox(\"Menu\",menu)\n",
    "    \n",
    "    st.title(\"Job Search Portal - IT\")\n",
    "    \n",
    "    if choice == \"Home\":\n",
    "        st.subheader(\"Home\")\n",
    "        with st.form(key = 'searchform'):\n",
    "            nav1,nav2,nav3,nav4,nav5,nav6 = st.beta_columns([3,2,1])\n",
    "            \n",
    "            with nav1:\n",
    "                search_term = st.text_input(\"Search Candidates\")\n",
    "            with nav2:\n",
    "                search_term = st.text_input(\"Location\")\n",
    "            with nav3:\n",
    "                search_term = st.text_input(\"Years of Experience\")\n",
    "            with nav4:\n",
    "                search_term = st.text_input(\"Salary\")\n",
    "            with nav5:\n",
    "                st.text(\"Search\")\n",
    "                submit_search = st.form_submit_button(label = 'Search')\n",
    "        st.success(\"You searched for {} in {}\".format(search_term,location))\n",
    "        \n",
    "        col1,col2 = st.beta_columns([2,1])\n",
    "        with col1:\n",
    "            if submit_search:\n",
    "                search_url = base_url.format(search_term,location)\n",
    "                # st.write(search_url)\n",
    "                data = get_data(search_url)\n",
    "                num_results = len(data)\n",
    "                st.subheader(\"Showing {} of candidates\".format(num_results))\n",
    "                \n",
    "                for i in data:\n",
    "                    job_category = i['category']\n",
    "                    job_location = i['location']\n",
    "                    job_exp = i['experience']\n",
    "                    job_resume = i['resume']\n",
    "                    job_salary = i['salary']\n",
    "                  #  job_company = i['company']\n",
    "                    st.markdown(html_template.format(job_category,job_location,job_exp,job_salary,\n",
    "                                                     unsafe_allow_html = True)\n",
    "                with st.beta_expander(\"Additional Information\")\n",
    "                                stc.html(resume_html.format(job_resume),scrolling = True)\n",
    "    else:\n",
    "        st.subheader(\"About\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "66e4bcb1",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
