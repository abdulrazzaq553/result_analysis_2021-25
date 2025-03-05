import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Custom CSS for styling and sidebar aesthetics
st.markdown(
    """
    <style>
    .stApp {
        font-family: 'Arial', sans-serif;
    }
    @media (prefers-color-scheme: dark) {
        .stApp {
            background-color: #2E2E2E !important;
        }
    }
    @media (prefers-color-scheme: light) {
        .stApp {
            background-color: #f0f2f6 !important;
        }
    }
    h1, h2, h3, h4, h5, h6 {
        color: #2e86c1;
        animation: fadeIn 2s;
    }
    @keyframes fadeIn {
        0% { opacity: 0; }
        100% { opacity: 1; }
    }
    .stSelectbox > div > div {
        font-size: 18px !important;
        border: 2px solid #0000FF !important;
    }
    .stRadio > div > label {
        font-size: 18px !important;
        color: #2e86c1 !important;
    }
    /* Sidebar Styling */
    @media (prefers-color-scheme: light) {
        [data-testid="stSidebar"] {
            font-size: 18px !important;  /* Increase font size */
            font-weight: bold !important;  /* Make text bold */
            color: #ffffff !important;  /* White text color */
            
            border-radius: 10px !important;  /* Rounded corners */
            padding: 10px !important;  /* Add padding */
            margin: 3px !important;
        }
    }
    /* Dark Theme Sidebar */
    @media (prefers-color-scheme: dark) {
        [data-testid="stSidebar"] {
            background-color: #2E2E2E !important;
            padding: 20px;
            border-right: 3px solid #2e86c1;
        }
    }
    /* Sidebar text styling */
    [data-testid="stSidebar"] .css-1d391kg { 
        font-size: 18px;
        color: #2e86c1;
    }
    
    div[data-testid="stTabs"] button {
        
       /* Adjust tab styles to fit on mobile */
    div[data-baseweb="tab-list"] button {
        font-size: 14px !important;  /* Reduce font size slightly */
        font-weight: bold !important;  /* Keep text bold */
        color: #ffffff !important;  /* White text color */
        background-color: #4CAF50 !important;  /* Green background */
        border-radius: 8px !important;  /* Slightly rounded corners */
        padding: 6px 8px !important;  /* Reduce padding */
        margin: 2px !important;  /* Reduce margin */
        min-width: 70px !important;  /* Decrease width for better fit */
        
       
    }
    
    div[data-testid="stTabs"] button:hover {
        background-color: #45a049 !important;  /* Darker green on hover */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Load data
sem_1 = pd.read_csv('Semester_1.csv')
sem_2 = pd.read_csv('Semester_2.csv')
sem_3 = pd.read_csv('Semester_3.csv')
sem_4 = pd.read_csv('Semester_4.csv')
sem_5 = pd.read_csv('Semester_5.csv')
sem_6 = pd.read_csv('Semester_6.csv')
sem_7 = pd.read_csv('Semester_7.csv')

# Merge all semester data
total = pd.concat([sem_1, sem_2, sem_3, sem_4, sem_5, sem_6, sem_7])

total['Semester'].replace({'Winter Semester 2020-2021':'Winter Semester 2021-2022'}, inplace=True)
total['Semester'].replace({'Winter Semester 2021-2022':'1st_Sem', 'Spring Semester 2021-2022':'2nd_Sem',
                            'Winter Semester 2022-2023':'3rd_Sem', 'Spring Semester 2022-2023':'4th_Sem',
                            'Winter Semester 2023-2024':'5th_Sem', 'Spring Semester 2023-2024':'6th_Sem',
                            'Winter Semester 2024-25':'7th_Sem'}, inplace=True)
total['gender'].replace({'F':'Female','M':'Male'}, inplace=True)

# Streamlit App Layout
st.header("🎓 Student Performance (BSCS 2021-25)")
st.markdown("**Dept. of Computer Science, UAF**")
st.markdown("**This dashboard provides an analysis of student performance from the 1st to the 7th semester.**")
st.subheader("⚙️ Filter Options 🔧")
st.markdown("🔖 Select a Tab to Explore 📊") 
tab1, tab2, tab3, tab4, tab5,tab6 = st.tabs(["🏠 Home",  "👤 Individual", "🏆 Top Grades", "📊 Top Marks",'Courses📚',"📈 Overall"])

with tab1:
    st.subheader("Student Result Analysis Dashboard🎓")
    st.markdown(""" =>This dashboard provides insights into the academic performance of BSCS Section-B (2021-25) students. Use the tabs above to navigate through different sections and explore the results:

- **👤 Individual:** Analyze the performance of individual students across all semesters or a specific semester. View marks, grades, and identify which semesters or courses have A's, B's, C's, and other grades.

- **🏆 Top Grades:** Explore the highest-performing students based on grades, either across all semesters or per semester.

- **📊 Top Marks:** Identify students with the highest marks, either overall or for each semester.

- **📚 Courses:** Analyze course-wise performance for all semesters or a specific semester. View the distribution of student grades across different courses, along with a separate categorization for additional or extra-enrolled courses.

- **📈 Overall:** Gain a comprehensive overview of performance across all semesters, including total grade calculations categorized by male and female students.
""")

    
    st.info("**Note:** This dashboard is for informational purposes only. For official records, please refer to the university LMS. 📚")
    st.write("---")
    st.markdown("#### Developed with 💜 by *Abdul Razzaq 🏴*")
    st.markdown("""
    **Let's Connect:**  
    📧 [Email](mailto:arazzaq7789@gmail.com)  
    **Feedback?**  
    I'd love to hear from you! 💬
    """)
    st.write("---")
    st.markdown('<style> div[data-baseweb="select"] > div { color: red !important; } </style>', unsafe_allow_html=True)

# Filter by
with tab6:
    st.subheader("📈 Overall Performance")
    Choose_Semesters = ["Choose_Semester"] + ['All_Semester'] + total['Semester'].unique().tolist()
    sel1 = st.selectbox("Select Semester ✨", Choose_Semesters, key="overall_sem")

    if sel1 == 'All_Semester':
        st.subheader("All Semesters Results 📋")
        st.warning("⚠️ Grades from extra enrolled courses are also included in the calculation.")
        for sem in total['Semester'].unique():
            sem_data = total[total['Semester'] == sem]
            st.subheader(f"{sem} Results 🔍:")
            
            col1, col2 = st.columns(2)
            with col1:
                fig, ax = plt.subplots(figsize=(10, 8))
                sns.countplot(data=sem_data, x='Grade', hue='gender', palette='hls', ax=ax)
                plt.legend(fontsize=14)
                plt.title(f"Grade Distribution in {sem} 📊", fontsize=16)
                st.pyplot(fig)
            with col2:
                st.dataframe(sem_data.groupby(['gender', 'Grade']).size().unstack())

            # Download Button for Semester Data
            csv = sem_data.to_csv(index=False)
            st.download_button(
                label=f"📥 Download {sem} Data",
                data=csv,
                file_name=f"{sem}_performance.csv",
                mime="text/csv"
            )

    elif sel1 == 'Choose_Semester':
        st.header('Please choose a semester 🚩')
    else:
        total_filtered = total[total['Semester'] == sel1]
        st.subheader(f"Results for {sel1} 📝")
        st.warning("⚠️ Grades from extra enrolled courses are also included in the calculation.")
        col1, col2 = st.columns(2)
        with col1:
            fig, ax = plt.subplots(figsize=(10, 8))
            sns.countplot(data=total_filtered, x='Grade', hue='gender', palette='hls', ax=ax)
            plt.legend(fontsize=14)
            plt.title(f"Grade Distribution in {sel1} 📊", fontsize=16)
            st.pyplot(fig)
        with col2:
            st.dataframe(total_filtered.groupby(['gender', 'Grade']).size().unstack())

        # Additional Dataframes
        col3, col4 = st.columns(2)
        with col3:
            st.subheader("Sorted by Course and Grade 🔤")
            bba = total_filtered.sort_values(['Course', 'Grade'])
            st.dataframe(bba)
        with col4:
            st.subheader("Grade Counts 📈")
            grade_counts = total_filtered['Grade'].value_counts().reset_index()
            grade_counts.columns = ['Grade', 'Count']
            st.dataframe(grade_counts)

        # Download Button for Filtered Data
        csv = total_filtered.to_csv(index=False)
        st.download_button(
            label=f"📥 Download {sel1} Data",
            data=csv,
            file_name=f"{sel1}_performance.csv",
            mime="text/csv"
        )
    st.write("---")
    st.markdown("#### Developed with 💜 by *Abdul Razzaq 🏴*")
    st.markdown("""
    **Let's Connect:**  
    📧 [Email](mailto:arazzaq7789@gmail.com)  
    **Feedback?**  
    I'd love to hear from you! 💬
    """)
    st.write("---")
    st.markdown('<style> div[data-baseweb="select"] > div { color: red !important; } </style>', unsafe_allow_html=True)

# Individual Section
with tab2:
    
    st.subheader("👤 Individual Student Performance")
    Choose_Students = st.selectbox("Select Student 🌟",["Choose Your Name"]+total['NAME'].unique().tolist(), key="individual_select")
    if Choose_Students=='Choose Your Name':
        st.info("Please choose a student's name from the dropdown to view their performance.")
    else:

        razzaq = total.drop_duplicates(subset=['Registration NO', 'NAME', 'gender', 'Course'], keep='last')
        filter_name = total[total['NAME'] == Choose_Students].reset_index(drop=True)
        filter_name.drop('gender', axis=1, inplace=True)
        filtered_data = razzaq[razzaq['NAME'].str.contains(Choose_Students, case=False, na=False)]
        student_marks = filtered_data.groupby('NAME')['Marks'].sum()

        st.subheader(f"Total Marks of {Choose_Students} 🏅")
        st.dataframe(student_marks)

    # Download Button for Filtered Data
        csv = filter_name.to_csv(index=False)
        st.download_button(
            label="📥 Download Filtered Data",
            data=csv,
            file_name=f"{Choose_Students}_performance.csv",
            mime="text/csv"
        )

        choose_sem = st.radio("Select Semester 🗓️", ['Overall'] + total['Semester'].unique().tolist(), horizontal=True, key="individual_sem")
        grades = st.radio("Select Grades 🎯", ["All"] + filter_name['Grade'].unique().tolist(), horizontal=True, key="individual_grades")
    
        if choose_sem == 'Overall':
            st.subheader(f"Results of {Choose_Students} (All Semesters) 🌐")
            st.warning("⚠️ Marks and grades from extra enrolled courses are also included in the calculation.")
            for sem in total['Semester'].unique():
                sem_data = filter_name[filter_name['Semester'] == sem]
                st.subheader(f"{sem} Results:")
                if grades == 'All':
                    st.dataframe(sem_data)
                else:
                    st.dataframe(sem_data[sem_data['Grade'] == grades])
        else:
            filter_name = filter_name[filter_name['Semester'] == choose_sem]
            st.warning("⚠️ Marks and grades from extra enrolled courses are also included in the calculation.")
            st.subheader(f"Results for {Choose_Students} in {choose_sem} 🔎")
            if grades == 'All':
                st.dataframe(filter_name)
            else:
                st.dataframe(filter_name[filter_name['Grade'] == grades])

    # Grades Count and Pie Chart
        st.subheader("Grades Overview 📊")
        st.warning("⚠️ Grades from both attempts (before and after course improvement(Extra_enroll))  are included in the calculation.")
        col1, col2 = st.columns(2)
        with col1:
            grade_counts = filter_name['Grade'].value_counts().reset_index()
            grade_counts.columns = ['Grade', 'Count']
            st.dataframe(grade_counts)
        with col2:
            fig, ax = plt.subplots(figsize=(8, 8))
            x = grade_counts['Grade']
            y = grade_counts['Count']
            ax.pie(grade_counts['Count'], labels=grade_counts['Grade'], autopct='%0.1f%%', textprops={'fontsize': 20})
            ax.set_title(f"Grade Distribution for {Choose_Students} 🎨")
            plt.legend([f"{label}: {value}" for label, value in zip(x, y)])
            st.pyplot(fig)
    st.write("---")
    st.markdown("#### Developed with 💜 by *Abdul Razzaq 🏴*")
    st.markdown("""
    **Let's Connect:**  
    📧 [Email](mailto:arazzaq7789@gmail.com)  
    **Feedback?**  
    I'd love to hear from you! 💬
    """)
    st.write("---")
    st.markdown('<style> div[data-baseweb="select"] > div { color: red !important; } </style>', unsafe_allow_html=True)

# Top Grades Section
with tab3:
    st.subheader("🏆 Top Grades")
    def get_top_students(data, grade):
        grade_data = data[data['Grade'] == grade]
        top_students = grade_data['NAME'].value_counts().head(6).reset_index()
        top_students.columns = ['Student Name', f'{grade} Count']
        return top_students

    Choose_Semesters = ['All_Semesters'] + sorted(total['Semester'].unique().tolist())
    selected_semester = st.selectbox("Select Semester 🗓️", Choose_Semesters, key="top_grades_sem")
    st.warning("⚠️ Grades from both attempts (before and after course improvement(Extra_enroll)) are included in the calculation.")

    grades = ['A', 'B', 'C', 'D', 'F']
    for grade in grades:
        if selected_semester == 'All_Semesters':
            top_students = get_top_students(total, grade)
        else:
            sem_data = total[total['Semester'] == selected_semester]
            top_students = get_top_students(sem_data, grade)

        col1, col2 = st.columns(2)
        with col1:
            st.write(f"**Top 6 Students with Most {grade}'s in {selected_semester}** ⭐")
            st.dataframe(top_students)
        with col2:
            fig, ax = plt.subplots(figsize=(8, 8))
            x = top_students['Student Name']
            y = top_students[f'{grade} Count']
            ax.pie(top_students[f'{grade} Count'], labels=top_students['Student Name'], autopct='%1.1f%%',
                   wedgeprops={'linewidth': 1, 'edgecolor': 'black'},
                   colors=sns.color_palette('coolwarm', len(top_students)), startangle=140,
                   textprops={'fontsize': 12})
            ax.set_title(f'Top 6 Students with {grade} (All Semesters) 🌟', fontsize=14, fontweight='bold')
            ax.set_aspect('equal')
            plt.legend([f'{Label} => {Value}' for Label, Value in zip(x, y)], title="Students", loc="best", fontsize=12)
            st.pyplot(fig)
    st.write("---")
    st.markdown("#### Developed with 💜 by *Abdul Razzaq 🏴*")
    st.markdown("""
    **Let's Connect:**  
    📧 [Email](mailto:arazzaq7789@gmail.com)  
    **Feedback?**  
    I'd love to hear from you! 💬
    """)
    st.write("---")
    st.markdown('<style> div[data-baseweb="select"] > div { color: red !important; } </style>', unsafe_allow_html=True)

# Top Marks Section
with tab4:
    def get_top_marks_students(data):
        razzaq = data.drop_duplicates(subset=['Registration NO', 'NAME', 'gender', 'Course'], keep='last')
        marks_data = razzaq.groupby('NAME')['Marks'].sum().reset_index()
        top_students1 = marks_data.sort_values(by='Marks', ascending=False).reset_index(drop=True)
        top_students = marks_data.sort_values(by='Marks', ascending=False).head(11).reset_index(drop=True)
        return top_students

    st.subheader("📊 Top 10 Students with Highest Total Marks")
    Choose_Semesters = ['All_Semesters'] + sorted(total['Semester'].unique().tolist())
    selected_semester = st.selectbox("Select Semester 🗓️", Choose_Semesters, key="marks_semester")
    
    if selected_semester == 'All_Semesters':
        top_marks_students = get_top_marks_students(total)
        st.write("**Top 10 Students with Highest Marks (All Semesters):**")
        st.dataframe(top_marks_students, use_container_width=True, height=250, key="top-marks-all")
        if not top_marks_students.empty:
            fig, ax = plt.subplots(figsize=(10, 5))
            fig, ax = plt.subplots(figsize=(10, 5))
            sns.barplot(x=top_marks_students['Marks'], y=top_marks_students['NAME'], palette='viridis', ax=ax)
            ax.set_xlabel('Total Marks', fontsize=14)
            ax.set_ylabel('Student Name', fontsize=14)
            ax.set_title(f'Top 10 Students with Highest Marks in {selected_semester}', fontsize=16, fontweight='bold')
            plt.xticks(fontsize=12)
            plt.yticks(fontsize=12)
 
# Annotate each bar with its value
            for p in ax.patches:
                width = p.get_width()
    # Position the text at the end of each bar, with a small offset for clarity
                ax.text(width + 1, p.get_y() + p.get_height() / 2, f'{width:.0f}', 
                        ha='left', va='center', fontsize=12, color='black')

            st.pyplot(fig)

    
            okk = total.drop_duplicates(subset=['Registration NO', 'NAME', 'gender', 'Course'], keep='last')
            overall = okk.groupby(['NAME','gender'])['Marks'].sum().sort_values(ascending=False).reset_index().head(62)
            st.subheader(f"Overall Total Marks of {selected_semester}🏅")
            import plotly.express as px
            import streamlit as st

# Suppose `overall` is your DataFrame with 'NAME', 'Marks', and 'gender'

            fig,ax=plt.subplots(figsize=(30,9))
            sns.lineplot(
                overall, 
                x='NAME', 
                y='Marks', 
                hue='gender',
                markers=True,
                lw=3,
                ax=ax
                
            )
            plt.xticks(rotation=90, fontsize=20)
            plt.yticks(fontsize=30)
            plt.legend(fontsize=42)
            plt.grid()
            st.pyplot(fig)

            st.subheader(f"Overall Total Marks of {selected_semester}🏆")
            st.dataframe(overall)
    else:
        total_sem = total[total['Semester'] == selected_semester]
        top_marks_students = get_top_marks_students(total_sem)
        st.write(f"**Top 10 Students with Highest Marks in {selected_semester}:**")
        
        st.warning(f"⚠️ Note: Marks of Extra Enrolled Courses in {selected_semester} are included in the Calculation.")
        st.dataframe(top_marks_students, use_container_width=True, height=250, key=f"top-marks-{selected_semester}")

    # Visualization
        if not top_marks_students.empty:
            total = total[total['Semester'] == selected_semester]
            top_marks_students = get_top_marks_students(total)
            fig, ax = plt.subplots(figsize=(10, 5))
            fig, ax = plt.subplots(figsize=(10, 5))
            sns.barplot(x=top_marks_students['Marks'], y=top_marks_students['NAME'], palette='viridis', ax=ax)
            ax.set_xlabel('Total Marks', fontsize=14)
            ax.set_ylabel('Student Name', fontsize=14)
            ax.set_title(f'Top 10 Students with Highest Marks in {selected_semester}', fontsize=16, fontweight='bold')
            plt.xticks(fontsize=12)
            plt.yticks(fontsize=12)
 
# Annotate each bar with its value
            for p in ax.patches:
                width = p.get_width()
    # Position the text at the end of each bar, with a small offset for clarity
                ax.text(width + 1, p.get_y() + p.get_height() / 2, f'{width:.0f}', 
                        ha='left', va='center', fontsize=12, color='black')

            st.pyplot(fig)

    
            okk = total.drop_duplicates(subset=['Registration NO', 'NAME', 'gender', 'Course'], keep='last')
            overall = okk.groupby(['NAME','gender'])['Marks'].sum().sort_values(ascending=False).reset_index().head(62)
            st.subheader(f"Overall Total Marks of {selected_semester}🏅")
            
            import plotly.express as px
            import streamlit as st

# Suppose `overall` is your DataFrame with 'NAME', 'Marks', and 'gender'
            fig,ax=plt.subplots(figsize=(30,9))
            sns.lineplot(
                overall, 
                x='NAME', 
                y='Marks', 
                hue='gender',
                markers=True,
                lw=3,
                ax=ax
                
            )
            plt.xticks(rotation=90, fontsize=20)
            plt.yticks(fontsize=30)
            plt.legend(fontsize=42)
            plt.grid()
            

# Force Plotly to show every category in the order they appear in `overall`
           
# Increase figure size so the labels are less likely to get skipped
            


            st.pyplot(fig)

            st.subheader(f"Overall Total Marks of {selected_semester}🏆")
            grade_remove=overall.drop('gender',axis=1)
            st.dataframe(grade_remove)
    st.write("---")
    st.markdown("#### Developed with 💜 by *Abdul Razzaq 🏴*")
    st.markdown("""
    **Let's Connect:**  
    📧 [Email](mailto:arazzaq7789@gmail.com)  
    **Feedback?**  
    I'd love to hear from you! 💬
    """)
    st.write("---")
    st.markdown('<style> div[data-baseweb="select"] > div { color: red !important; } </style>', unsafe_allow_html=True)

# Courses Section
with tab5:
    st.subheader("📚 Courses")
    Choose_Semesters = ["Choose_Semester"] + total['Semester'].unique().tolist()
    sel1 = st.selectbox("Select Semester 🗓️", Choose_Semesters, key="courses_sem")

    if sel1 == 'Choose_Semester':
        st.warning("⚠️ Note: Please select a semester")
    else:
        sem_data = total[total['Semester'] == sel1]
        course_counts = sem_data['Course'].value_counts().reset_index(name='Count')
        course_counts.rename(columns={'index': 'Course'}, inplace=True)

        main_courses = course_counts['Course'][:6].tolist()
        extra_courses = course_counts['Course'][6:].tolist()

        st.subheader(f"Here are the Courses of {sel1} ✨")
        select_course = st.radio("Select Course", main_courses, horizontal=True, key="main_course")
        if extra_courses:  # show extra courses only if there are any extra courses available
            st.warning(f"⚠️ Extra Enrolled Students also registered for these Courses in {sel1}:")
            select_course1 = st.radio("Extra_Enroll_Course", ["None"] + extra_courses, index=0, horizontal=True, key="extra_course")

        col1, col2 = st.columns(2)
        with col1:
            # Filter and sort the main course results by Marks in descending order
            total1 = sem_data[sem_data['Course'] == select_course]
            total1 = total1.sort_values('Marks', ascending=False).reset_index(drop=True)
            # Get top 12 students and top 10 subset for bar chart
            top12_total1 = total1
            top12_total2 = total1.head(10)
            st.subheader(f"Result of {select_course} 🎓")
            st.dataframe(top12_total1[['NAME', 'Marks', 'Grade']])
            
            # Download Button for Filtered Data (top 12)
            csv = top12_total1.to_csv(index=False)
            st.download_button(
                label=f"📥 Download {select_course} Top 12 Data",
                data=csv,
                file_name=f"{select_course}_top12_performance.csv",
                mime="text/csv"
            )

        with col2:
            # For the extra course, show the full sorted data
            if extra_courses and select_course1 != "None":
                total2 = sem_data[sem_data['Course'] == select_course1]
                total2 = total2.sort_values('Marks', ascending=False).reset_index(drop=True)
                st.subheader(f"Result of {select_course1} 🔍")
                st.warning(f"⚠️ Note: This result includes only students who extra enrolled in {select_course1} during {sel1}.")
                st.dataframe(total2[['NAME', 'Marks', 'Grade']])
                
                # Download Button for Filtered Data
                csv = total2.to_csv(index=False)
                st.download_button(
                    label=f"📥 Download {select_course1} Data",
                    data=csv,
                    file_name=f"{select_course1}_performance.csv",
                    mime="text/csv"
                )
            else:
                st.info("ℹ️ No extra course selected or available.")

        st.subheader(f"Top 10 Students in {select_course} 📊")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.barplot(data=top12_total2, x='NAME', y='Marks', palette='viridis', ax=ax)
        plt.xticks(rotation=45, ha='right', fontsize=12)
        plt.title("Marks of Top 10 Students", fontsize=16)
        plt.xlabel("Student Name", fontsize=14)
        plt.ylabel("Marks", fontsize=14)

        # Annotate each bar with its value (marks)
        for bar in ax.patches:
            height = bar.get_height()
            ax.annotate(f'{height:.0f}',
                        (bar.get_x() + bar.get_width() / 2., height),
                        ha='center', va='bottom', fontsize=12, color='black',
                        xytext=(0, 5), textcoords='offset points')

        st.pyplot(fig)

        # Pie Chart for Grades for the main course
        st.subheader(f"Grade Distribution in {select_course} 🎨")
        col3, col4 = st.columns(2)
        with col3:
            grade_counts = top12_total1['Grade'].value_counts().reset_index()
            grade_counts.columns = ['Grade', 'Count']
            fig, ax = plt.subplots(figsize=(8, 8))
            ax.pie(grade_counts['Count'], labels=grade_counts['Grade'], autopct='%0.1f%%', textprops={'fontsize': 20})
            ax.set_title(f"Total Grades in {select_course}")
            plt.legend([f"{label}:{value}" for label, value in zip(grade_counts['Grade'], grade_counts['Count'])])
            st.pyplot(fig)
        with col4:
            st.dataframe(grade_counts)

        # Line Plot for Marks (for the main course)
        st.subheader(f"Marks of {select_course} 📈")
        fig, ax = plt.subplots(figsize=(23, 8))
        sns.lineplot(
            data=top12_total1,
            x='NAME',
            y='Marks',
            hue='gender',
            marker='*',       # custom marker style
            lw=3,             # thicker line for clarity
            ax=ax   
        )
        plt.xticks(rotation=90, fontsize=20)
        plt.yticks(fontsize=30)
        plt.legend(fontsize=12)
        plt.grid()
        st.pyplot(fig)
    st.write("---")
    st.markdown("#### Developed with 💜 by *Abdul Razzaq 🏴*")
    st.markdown("""
    **Let's Connect:**  
    📧 [Email](mailto:arazzaq7789@gmail.com)  
    **Feedback?**  
    I'd love to hear from you! 💬
    """)
    st.write("---")
    st.markdown('<style> div[data-baseweb="select"] > div { color: red !important; } </style>', unsafe_allow_html=True)

# Footer

