import streamlit as st
import pandas as pd

# Title of the app
st.title("S.T.A.B Method Task Manager")

# Frequency selection
frequency = st.selectbox(
    "Select Task Frequency",
    ["Every 72 Hours", "Weekly", "Monthly", "90 Days"]
)

# Define tasks based on your table (simplified for brevity)
tasks = {
    "Spending & Segmentation": {
        "Every 72 Hours": [
            {"task": "Review campaign spend vs results", "subtasks": []}
        ],
        "Weekly": [
            {"task": "Review campaign spend vs results", "subtasks": [
                "Are there any campaigns that need extra optimisations? (bad conversion metrics ie: no conversions, high CPA, low ROAS)"
            ]},
            {"task": "Review ad group spend vs results", "subtasks": [
                "Are there any ad groups that need extra optimisations? (bad conversion metrics ie: no conversions, high CPA, low ROAS)"
            ]}
        ],
        "Monthly": [
            {"task": "Review campaign spend vs results", "subtasks": [
                "Are there any campaigns that are ready to scale? (good conversion metrics with a low search impression share < 65%)"
            ]},
            {"task": "Review ad group spend vs results", "subtasks": [
                "Are there any ad groups that need to be moved into a separate campaign? (good conversion metrics & but low spend)"
            ]}
        ],
        "90 Days": []
    },
    "Targeting": {
        "Every 72 Hours": [
            {"task": "Complete a Search term audit", "subtasks": [
                "Add extra negative keywords to limit unrelated search terms",
                "Add any converting or highly relevant search terms as new [exact match] keywords"
            ]}
        ],
        "Weekly": [
            {"task": "Keyword Review", "subtasks": [
                "Identify keywords with a high CPC compared to the account average",
                "Identify keywords with a high cost per conversion compared to the account average",
                "Identify keywords with a status warning (low search volume, below first page bid, rarely shown due to low quality score)"
            ]},
            {"task": "Keyword Status Checks", "subtasks": [
                "Do any keywords have a quality score below 5/10?",
                "Do any keywords have a 'below first page bid estimate' warning?",
                "Do any keywords have a 'rarely shown due to low quality score' warning?",
                "Do any keywords have a 'low search volume' warning?"
            ]}
        ],
        "Monthly": [
            {"task": "Auction Insights Report Review", "subtasks": [
                "Check for new competitors or increased competitor spend if CPC has increased"
            ]},
            {"task": "Location based results", "subtasks": [
                "Review location performance and add exclusions or bid optimisations",
                "Check for searches from non-targeted locations and exclude them"
            ]}
        ],
        "90 Days": [
            {"task": "Demographic Performance", "subtasks": [
                "Review demographics and add exclusions or bid optimisations by age",
                "Review demographics and add exclusions or bid optimisations by income"
            ]}
        ]
    },
    # Add "Ads & Landing Pages" and "Bidding" sections similarly
}

# Display tasks based on selected frequency
st.subheader(f"Tasks for {frequency}")
for section, freq_tasks in tasks.items():
    if freq_tasks.get(frequency):
        st.write(f"### {section}")
        for task in freq_tasks[frequency]:
            st.write(f"- **{task['task']}**")
            for subtask in task["subtasks"]:
                checked = st.checkbox(subtask)
            notes = st.text_area(f"Notes for {task['task']}", key=f"{task['task']}_{frequency}")

# Export functionality (optional)
if st.button("Export Tasks"):
    # Logic to export tasks as CSV or PDF can be added here
    st.write("Export feature coming soon!")

# Run with: streamlit run script.py
