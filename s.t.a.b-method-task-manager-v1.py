import streamlit as st

# Set page title and layout
st.set_page_config(page_title="S.T.A.B Method Task Manager", layout="wide")
st.title("S.T.A.B Method Task Manager")

# Define the data structure for the S.T.A.B Method tasks (from your table)
tasks_data = [
    {
        "section": "Spending & Segmentation",
        "color": "#90EE90",  # Light green for the section
        "tasks": [
            {
                "task": "1. Review campaign spend vs results",
                "subtasks": [
                    {
                        "description": "a. Are there any campaigns that are ready to scale? (good conversion metrics with a low search impression share < 65%)",
                        "frequency": {"Every 72 Hours": False, "Weekly": False, "Monthly": True, "90 Days": False}
                    },
                    {
                        "description": "b. Are there any campaigns that need extra optimisations? (bad conversion metrics ie: no conversions, high CPA, low ROAS) Make a note and complete further optimisations",
                        "frequency": {"Every 72 Hours": False, "Weekly": True, "Monthly": False, "90 Days": False}
                    }
                ]
            },
            {
                "task": "2. Review ad group spend vs results",
                "subtasks": [
                    {
                        "description": "a. Are there any ad groups that need to be moved into a separate campaign? (good conversion metrics & but low spend)",
                        "frequency": {"Every 72 Hours": False, "Weekly": False, "Monthly": True, "90 Days": False}
                    },
                    {
                        "description": "b. Are there any ad groups that need extra optimisations? (bad conversion metrics ie: no conversions, high CPA, low ROAS) Make a note and complete further optimisations",
                        "frequency": {"Every 72 Hours": False, "Weekly": True, "Monthly": False, "90 Days": False}
                    }
                ]
            }
        ]
    },
    {
        "section": "Targeting",
        "color": "#FF6347",  # Tomato red for the section
        "tasks": [
            {
                "task": "3. Keyword Targeting",
                "subtasks": [
                    {
                        "description": "Complete a Search term audit",
                        "frequency": {"Every 72 Hours": True, "Weekly": False, "Monthly": False, "90 Days": False},
                        "additional_info": [
                            "> and add extra negative keywords to limit unrelated search terms",
                            "> and add any converting or highly relevant search terms as new [exact match] keywords"
                        ]
                    }
                ]
            },
            # Add more tasks under Targeting (like Keyword Review, etc.) as needed
        ]
    }
    # Add remaining sections (Ads & Landing Pages, Bidding, Quality Control Checks) similarly
]

# Create a table-like layout using Streamlit columns
st.markdown("### Task Checklist")

# Frequency headers
cols = st.columns([4, 1, 1, 1, 1, 2])
cols[0].markdown("**Task**")
cols[1].markdown("**Every 72 Hours**")
cols[2].markdown("**Weekly**")
cols[3].markdown("**Monthly**")
cols[4].markdown("**90 Days**")
cols[5].markdown("**Optimisation Notes**")

# Iterate through sections and tasks to build the UI
for section in tasks_data:
    # Section header with background color
    st.markdown(
        f"<h3 style='background-color: {section['color']}; padding: 10px;'>{section['section']}</h3>",
        unsafe_allow_html=True
    )

    # Iterate through tasks in the section
    for task in section["tasks"]:
        # Create a row for each task
        with st.expander(task["task"], expanded=False):
            # Display subtasks
            for subtask in task["subtasks"]:
                cols = st.columns([4, 1, 1, 1, 1, 2])
                cols[0].markdown(subtask["description"])

                # Frequency checkboxes (non-editable, just for display)
                cols[1].markdown("✅" if subtask["frequency"]["Every 72 Hours"] else "⬜")
                cols[2].markdown("✅" if subtask["frequency"]["Weekly"] else "⬜")
                cols[3].markdown("✅" if subtask["frequency"]["Monthly"] else "⬜")
                cols[4].markdown("✅" if subtask["frequency"]["90 Days"] else "⬜")

                # Optimisation notes input
                notes_key = f"notes_{section['section']}_{task['task']}_{subtask['description']}"
                cols[5].text_area("", key=notes_key, placeholder="Add optimisation notes here...", label_visibility="collapsed")

                # Display additional info (like the bullet points under "Complete a Search term audit")
                if "additional_info" in subtask:
                    for info in subtask["additional_info"]:
                        st.markdown(f"  {info}")

# Add a button to export notes (placeholder for future functionality)
if st.button("Export Notes"):
    st.write("Export functionality coming soon!")
