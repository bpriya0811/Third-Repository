from pathlib import Path
import streamlit as st 
from PIL import Image

#Path setting 
current_dir = Path(__file__).parent if '__file__' in locals() else Path.cwd()
css_file = current_dir/'style.css'
resume_file = current_dir/'resume.pdf'
image_file = current_dir/'profilepic.png'

st.set_page_config(
    page_icon='📄',
    page_title='Digital Resume'
)

#load csv,jpg files
with open(css_file) as f:
    st.markdown('<style>{}</style>'.format(f.read()),unsafe_allow_html=True)

with open(resume_file, 'rb') as pdf_file:
    pdf_byte = pdf_file.read()
    image_file=Image.open(image_file)

#Main section

col1,col2 = st.columns(2, gap='small')
with col1:
    st.image(image_file,width=280)

with col2:
    st.title('Priyanka Ramesh Bamane')
    st.write('Business Analyst | Full Stack Developer')
    st.download_button(label='Download my Resume',data=pdf_byte, file_name='Priyanka Bamane.pdf',mime='applocation/octet-stream')
    st.write('brpiya0811@gmail.com')

#Social Media Links 
social_media = {
    'LinkedIn': 'https://www.linkedin.com/in/priya-bamane/',
    'Github':'https://github.com/bpriya0811',
    'Nokari':'#'
}
#st.write('#')
cols = st.columns(len(social_media)) 
for index, (platform,link) in enumerate(social_media.items()):
    cols[index].write(f'[{platform}]({link})')

#Summary 
st.subheader('Summary',divider='violet')
st.write('Dynamic and results-driven MBA graduate specializing in Business Analytics and Information Systems, with a solid background in Python Full Stack Development. My unique blend of technical and analytical skills allows me to turn data insights into actionable strategies, optimizing processes and driving business growth. I am passionate about leveraging technology to solve real-world challenges and am eager to bring my expertise to a forward-thinking organization that values innovation and strategic impact.')

#Qualification
#st.write('#')
st.subheader('Qualification',divider='violet')
st.write('✔️**Masters of Business Administration |Business Analytics, Information System | Nov 2022 - Sep 2024 |** ')
st.write('Chhatrapati Shahu Institute of Business Education and Research, Kolhapur')
st.write('✔️**Certification Course | Python Full Stack Development |**')
st.write('Shreekrupa Institute, Kolhapur')
st.write('✔️**Bachlors of Commerce | Accountacy | June 2019 - June 2022 |**')
st.write('R.B.Madkholkar College, Chandgad, Kolhapur')

#Skilla
st.subheader('Hard Skills',divider='violet')
st.write("""
         - Programming : C, HTML, CSS, Python, Bootstrap,React, Java, VBA, Django
         - Data Visualization : Python, R, PowerBi, Excel, SPSS 
         - Modelling : Linear Regression, Decision Tree, Random Forest, Super Vector Machine,Classification, Clustering, KNN Algorithm
         - Database : SQL, PLSQL
         - System : Project Management, Knowledge Management, Software Engineering""")

#work history
st.subheader('Work History', divider='violet')

st.write("**Younity Community Pvt. Ltd.| Business Development Specialist | Aug, 2024 to Aug, 2024 |**")
st.write("""
         - Building Sustainable Revenue System
         - Strategizing Growth 
         - B2C Communication""")

st.write("**Shreekrupa Institute, Kolhapur| Python Full Stack Developer | Jan 2024, to June, 2024 |**")
st.write("""
         - Created engaging web applications to support teaching and learning activities.
         - Worked with teaching staff to translate their needs into functional software solutions.
         - Developed dashboards to present educational data and performance metrics.""")

st.write("**Dhanlaxmi Cashew Industries, Kolhapur | HR Intern | Nov, 2023 to Dec, 2023 |**")
st.write("""
         - Analyzed HR metrics and employee data 
         - Created detailed report""")

#Projects
st.subheader('Projects and Reports',divider='violet')
st.write("""
         - :blue[Retail] Analysis Hub:bar_chart: : https://retailanalyzer.streamlit.app/
         - :red[Data] at Your Fingertips : https://datatodecisions.streamlit.app/""")





