import streamlit as st

# Set page layout
st.set_page_config(layout="wide")

# Sidebar for page navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Select Page", ["Search Optimization", "Shopping"])

# Function to display tasks in a table-like format
def display_tasks(tasks_data, page_title):
    st.title(page_title)
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
                    notes_key = f"notes_{section['section']}_{task['task']}_{subtask['description']}_{page_title}"
                    cols[5].text_area("", key=notes_key, placeholder="Add optimisation notes here...", label_visibility="collapsed")

                    # Display additional info (like the bullet points under "Complete a Search term audit")
                    if "additional_info" in subtask:
                        for info in subtask["additional_info"]:
                            st.markdown(f"  {info}")

    # Add a button to export notes (placeholder for future functionality)
    if st.button("Export Notes", key=f"export_{page_title}"):
        st.write("Export functionality coming soon!")

# Data for Search Optimization page (from previous content)
search_optimization_data = [
    {
        "section": "Spending & Segmentation",
        "color": "#90EE90",  # Light green
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
        "color": "#FF6347",  # Tomato red
        "tasks": [
            {
                "task": "3. Keyword Targeting",
                "subtasks": [
                    {
                        "description": "a. Complete a Search term audit",
                        "frequency": {"Every 72 Hours": True, "Weekly": False, "Monthly": False, "90 Days": False},
                        "additional_info": [
                            "> and add extra negative keywords to limit unrelated search terms",
                            "> and add any converting or highly relevant search terms as new [exact match] keywords"
                        ]
                    }
                ]
            },
            {
                "task": "4. Keyword Review",
                "subtasks": [
                    {
                        "description": "a. Identify keywords that are under performing, and make the decision to either pause or focus on with further optimisations",
                        "frequency": {"Every 72 Hours": False, "Weekly": True, "Monthly": False, "90 Days": False},
                        "additional_info": [
                            "> Keywords with a high CPC compared to the account average",
                            "> Keywords which have a high cost per conversion compared to the account average",
                            "> Keywords with a status warning (low search volume, below first page bid, rarely shown due to low quality score)"
                        ]
                    },
                    {
                        "description": "b. If you are running 'Call Only Ads' or 'Call Extensions' review the call extensions report and filter by search keywords",
                        "frequency": {"Every 72 Hours": False, "Weekly": True, "Monthly": False, "90 Days": False},
                        "additional_info": [
                            "> For Search Keywords with a high CPC & no phone calls: Do these need to be paused/excluded",
                            "> Which Search Keywords are providing the highest quality phone calls: Do these need more budget"
                        ]
                    }
                ]
            },
            {
                "task": "5. Auction Insights Report Review",
                "subtasks": [
                    {
                        "description": "a. If you are seeing an increased CPC check this report to see if there are new competitors or have competitors increased their spend",
                        "frequency": {"Every 72 Hours": False, "Weekly": False, "Monthly": True, "90 Days": False}
                    }
                ]
            },
            {
                "task": "6. Keyword Status Checks",
                "subtasks": [
                    {
                        "description": "a. Do any keywords have a keyword quality score of below 5/10",
                        "frequency": {"Every 72 Hours": False, "Weekly": True, "Monthly": False, "90 Days": False},
                        "additional_info": [
                            "> add changes to ad copy to help with KW targeting and quality score",
                            "> add landing page updates to help with KW targeting",
                            "> Review landing page load time https://pagespeed.web.dev/"
                        ]
                    },
                    {
                        "description": "b. Do any keywords have a 'below first page bid estimate' warning",
                        "frequency": {"Every 72 Hours": False, "Weekly": True, "Monthly": False, "90 Days": False}
                    },
                    {
                        "description": "c. Do any keywords have a 'rarely shown due to low quality score' warning",
                        "frequency": {"Every 72 Hours": False, "Weekly": True, "Monthly": False, "90 Days": False}
                    },
                    {
                        "description": "d. Do any keywords have a 'low search volume' warning",
                        "frequency": {"Every 72 Hours": False, "Weekly": True, "Monthly": False, "90 Days": False}
                    }
                ]
            },
            {
                "task": "7. Location based results",
                "subtasks": [
                    {
                        "description": "a. Review location performance and add exclusions or bid optimisations (if required)",
                        "frequency": {"Every 72 Hours": False, "Weekly": False, "Monthly": True, "90 Days": False}
                    },
                    {
                        "description": "b. Check to see if there are any searches from non-targeted locations (and exclude locations)",
                        "frequency": {"Every 72 Hours": False, "Weekly": False, "Monthly": True, "90 Days": False}
                    }
                ]
            },
            {
                "task": "8. Device results",
                "subtasks": [
                    {
                        "description": "a. Review device performance and add exclusions or bid optimisations (if required)",
                        "frequency": {"Every 72 Hours": False, "Weekly": False, "Monthly": True, "90 Days": False}
                    }
                ]
            },
            {
                "task": "9. Audience Performance",
                "subtasks": [
                    {
                        "description": "a. Review observation audiences and add exclusions (or bid optimisations if not using smart bidding)",
                        "frequency": {"Every 72 Hours": False, "Weekly": False, "Monthly": True, "90 Days": False}
                    },
                    {
                        "description": "b. If your added audiences are below 80% of traffic check add new audiences",
                        "frequency": {"Every 72 Hours": False, "Weekly": False, "Monthly": True, "90 Days": False}
                    }
                ]
            },
            {
                "task": "10. Demographic Performance",
                "subtasks": [
                    {
                        "description": "a. Review demographics and add exclusions (or bid optimisations if not using smart bidding)",
                        "frequency": {"Every 72 Hours": False, "Weekly": False, "Monthly": False, "90 Days": True},
                        "additional_info": [
                            "> by age",
                            "> by income (not available worldwide)"
                        ]
                    }
                ]
            },
            {
                "task": "11. When ads appeared",
                "subtasks": [
                    {
                        "description": "a. Review performance by day of the week and exclude any days with consistent & significant under performance and exclude (if not using smart bidding)",
                        "frequency": {"Every 72 Hours": False, "Weekly": False, "Monthly": False, "90 Days": True}
                    },
                    {
                        "description": "a. Review performance by hour of the day and look to increase your budget if your spending is not sufficient for the whole day (or for Ad schedule)",
                        "frequency": {"Every 72 Hours": False, "Weekly": False, "Monthly": False, "90 Days": True}
                    }
                ]
            }
        ]
    },
    {
        "section": "Ads & Landing Pages",
        "color": "#ADD8E6",  # Light blue
        "tasks": [
            {
                "task": "12. Review your current split test results for Ads by Ad Groups",
                "subtasks": [
                    {
                        "description": "a. Review your split tests in each under performing ad group and pause the ad with a significantly lower CTR & Conversion rate (if not significant allow the test to run for another 30 days)",
                        "frequency": {"Every 72 Hours": False, "Weekly": False, "Monthly": True, "90 Days": False}
                    },
                    {
                        "description": "b. If you paused an ad duplicate the 'winning ad' and make only 1 change so you can start another split test",
                        "frequency": {"Every 72 Hours": False, "Weekly": False, "Monthly": True, "90 Days": False}
                    }
                ]
            },
            {
                "task": "13. Quality Check for your Ads",
                "subtasks": [
                    {
                        "description": "a. Check to see if any ads are disapproved or have a 'rarely shown' warning. If any exist make changes & re-submit ad for review",
                        "frequency": {"Every 72 Hours": False, "Weekly": True, "Monthly": False, "90 Days": False}
                    }
                ]
            },
            {
                "task": "14. Review your Ad Assets",
                "subtasks": [
                    {
                        "description": "a. Do you have any underperforming Ad Assets that need to be updated",
                        "frequency": {"Every 72 Hours": False, "Weekly": False, "Monthly": True, "90 Days": False},
                        "additional_info": [
                            "> sitelink extensions",
                            "> callout extensions",
                            "> structured snippet extension",
                            "> call extension",
                            "> lead form extension",
                            "> location extensions (GMB linking)",
                            "> affiliate location extensions",
                            "> price extension",
                            "> promotion extension",
                            "> image extensions"
                        ]
                    }
                ]
            },
            {
                "task": "15. Landing Page Review",
                "subtasks": [
                    {
                        "description": "a. If you are sending ads to different landing pages review your Conversion rates by landing pages. If any landing pages have a significantly lower conversion rate look at updating/changing the landing pages",
                        "frequency": {"Every 72 Hours": False, "Weekly": False, "Monthly": False, "90 Days": True}
                    }
                ]
            }
        ]
    },
    {
        "section": "Bidding",
        "color": "#FFD700",  # Gold
        "tasks": [
            {
                "task": "16. Campaign Bidding Review",
                "subtasks": [
                    {
                        "description": "a. Is there enough Conversion Data to switch to Max Conversions or Max Conversion Value? (check below)",
                        "frequency": {"Every 72 Hours": False, "Weekly": False, "Monthly": False, "90 Days": True},
                        "additional_info": [
                            "> Is there an average of at least 1 primary conversion per day over the past 30 days?",
                            "> Have weekly conversions been increasing each week for the past 4-6 weeks?"
                        ]
                    },
                    {
                        "description": "b. If you are using a tCPA / tROAS, is the current campaign bidding target still the best option? Or is it limiting performance? (check these metrics to see if you need to adjust your target)",
                        "frequency": {"Every 72 Hours": False, "Weekly": False, "Monthly": True, "90 Days": True},
                        "additional_info": [
                            "> Is there a drop in total conversions / conversion value",
                            "> Has the campaign spend reduced significantly",
                            "> Are the impressions dropping too much"
                        ]
                    }
                ]
            }
        ]
    },
    {
        "section": "Quality Control Checks",
        "color": "#D3D3D3",  # Light gray
        "tasks": [
            {
                "task": "17. Quality Control Checks",
                "subtasks": [
                    {
                        "description": "a. Are all conversion actions working",
                        "frequency": {"Every 72 Hours": False, "Weekly": False, "Monthly": True, "90 Days": False}
                    },
                    {
                        "description": "b. Is your budget on track",
                        "frequency": {"Every 72 Hours": False, "Weekly": False, "Monthly": True, "90 Days": False}
                    },
                    {
                        "description": "c. Is your payment method working",
                        "frequency": {"Every 72 Hours": False, "Weekly": False, "Monthly": True, "90 Days": False}
                    },
                    {
                        "description": "d. Are there any active 'auto apply' recommendations in the account",
                        "frequency": {"Every 72 Hours": False, "Weekly": False, "Monthly": True, "90 Days": False}
                    },
                    {
                        "description": "e. Are there any notifications from Google that need to be actioned",
                        "frequency": {"Every 72 Hours": False, "Weekly": False, "Monthly": True, "90 Days": False}
                    }
                ]
            }
        ]
    }
]

# Data for Shopping page (new content)
shopping_data = [
    {
        "section": "Spending & Segmentation",
        "color": "#90EE90",  # Light green
        "tasks": [
            {
                "task": "1. Review campaign spend vs results",
                "subtasks": [
                    {
                        "description": "a. Are there any campaigns that are ready to scale? (good conversion metrics with a low search impression share < 65%)",
                        "frequency": {"Every 72 Hours": False, "Weekly": False, "Monthly": True, "90 Days": False}
                    },
                    {
                        "description": "a. Are there any campaigns that need extra optimisations? (bad conversion metrics ie: no conversions, high CPA, low ROAS) Make a note and complete further optimisations",
                        "frequency": {"Every 72 Hours": False, "Weekly": True, "Monthly": False, "90 Days": False}
                    }
                ]
            },
            {
                "task": "2. Review ad group/product category spend vs results",
                "subtasks": [
                    {
                        "description": "a. Are there any ad groups or product categories that need to be moved into a separate campaign? (good conversion metrics & but low spend)",
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
        "color": "#FF6347",  # Tomato red
        "tasks": [
            {
                "task": "3. Keyword Targeting",
                "subtasks": [
                    {
                        "description": "a. Complete a Search term audit",
                        "frequency": {"Every 72 Hours": True, "Weekly": False, "Monthly": False, "90 Days": False},
                        "additional_info": [
                            "> and add extra negative keywords to limit unrelated search terms"
                        ]
                    }
                ]
            },
            {
                "task": "4. Product & Product Title Review",
                "subtasks": [
                    {
                        "description": "a. Identify Products that are under performing, and make the decision to either pause or focus on with further optimisations. Optimise by:",
                        "frequency": {"Every 72 Hours": False, "Weekly": False, "Monthly": True, "90 Days": False},
                        "additional_info": [
                            "> Use all 150 characters with most important details in the first 70 characters",
                            "> Include Product Title, relevant search terms/keywords, brand name, product type & modifiers (like gender, size, colour or materials) in your product title",
                            "> Review search terms to find keywords to add to your product titles"
                        ]
                    },
                    {
                        "description": "b. Test your Product Images to find best performing product images for CTR & Conversion rates. Tests include:",
                        "frequency": {"Every 72 Hours": False, "Weekly": False, "Monthly": True, "90 Days": False},
                        "additional_info": [
                            "> Do product based or lifestyle image perform better",
                            "> Do different product angles or colours perform better"
                        ]
                    },
                    {
                        "description": "c. Review Disapproved Products in Merchant Centre Next to see if there are any disapproved products (& fix issues)",
                        "frequency": {"Every 72 Hours": False, "Weekly": False, "Monthly": True, "90 Days": False}
                    }
                ]
            },
            {
                "task": "5. Optimise Your Product Feed",
                "subtasks": [
                    {
                        "description": "a. Review Products by Product/Listing Group (Review data from 7, 14, 30 days & 60 or 90 days if available)",
                        "frequency": {"Every 72 Hours": False, "Weekly": False, "Monthly": True, "90 Days": False}
                    },
                    {
                        "description": "> Identify Products with poor performance by conversion rate (Update the product title or potentially exclude if continual under performance)",
                        "frequency": {"Every 72 Hours": False, "Weekly": False, "Monthly": True, "90 Days": False}
                    },
                    {
                        "description": "> Identify Products with poor performance by declining impressions or low CTR (Update these product titles by checking your search term audit to see if you can increase your position (& CTR) by adding or updating keyword focus)",
                        "frequency": {"Every 72 Hours": False, "Weekly": False, "Monthly": True, "90 Days": False}
                    },
                    {
                        "description": "> Identify Products with high spend but poor performance by low ROAS (exclude underperforming products)",
                        "frequency": {"Every 72 Hours": False, "Weekly": False, "Monthly": True, "90 Days": False}
                    }
                ]
            },
            {
                "task": "6. Product Competition Review",
                "subtasks": [
                    {
                        "description": "a. If you are seeing an increased CPC or declining conversions check GMC Next > Analytics > Products",
                        "frequency": {"Every 72 Hours": False, "Weekly": False, "Monthly": True, "90 Days": False},
                        "additional_info": [
                            "> Are your 'Ad' clicks, impressions or CTR decreasing significantly",
                            "> Is there an increase in Competitor spending",
                            "> Have any competitors lowered their pricing"
                        ]
                    }
                ]
            },
            {
                "task": "7. Google Shopping Experience: Store Quality",
                "subtasks": [
                    {
                        "description": "a. Review your 'Store Quality' Metrics in GMC Next",
                        "frequency": {"Every 72 Hours": False, "Weekly": False, "Monthly": True, "90 Days": False},
                        "additional_info": [
                            "> Is your desktop & mobile website speed <2 seconds",
                            "> Is your image resolution score above 75%",
                            "> Do you have enough images per offer (goal is 6-8)",
                            "> Do you have a listed returns policy",
                            "> Do you have listed shipping costs & delivery times",
                            "> Do you have enough reviews to get a listed store ranking",
                            "> Do you have all payment options activated"
                        ]
                    }
                ]
            },
            {
                "task": "8. Product Status Checks",
                "subtasks": [
                    {
                        "description": "a. Do any products have current status warnings? ie: not eligible, eligible (limited)",
                        "frequency": {"Every 72 Hours": False, "Weekly": True, "Monthly": False, "90 Days": False},
                        "additional_info": [
                            "> If so, make changes required"
                        ]
                    },
                    {
                        "description": "b. If you are bidding by CPC, are any products limited due to low bid?",
                        "frequency": {"Every 72 Hours": False, "Weekly": True, "Monthly": False, "90 Days": False}
                    }
                ]
            },
            {
                "task": "9. Location based results",
                "subtasks": [
                    {
                        "description": "a. Review location performance and add exclusions or bid optimisations (if required)",
                        "frequency": {"Every 72 Hours": False, "Weekly": False, "Monthly": True, "90 Days": False}
                    },
                    {
                        "description": "b. Check to see if there are any searches from non-targeted locations (and exclude locations)",
                        "frequency": {"Every 72 Hours": False, "Weekly": False, "Monthly": True, "90 Days": False}
                    }
                ]
            },
            {
                "task": "10. Device results",
                "subtasks": [
                    {
                        "description": "a. Review device performance and add exclusions or bid optimisations (if required)",
                        "frequency": {"Every 72 Hours": False, "Weekly": False, "Monthly": True, "90 Days": False}
                    }
                ]
            },
            {
                "task": "11. Audience Performance",
                "subtasks": [
                    {
                        "description": "a. Review observation audiences and add exclusions (or bid optimisations if not using smart bidding)",
                        "frequency": {"Every 72 Hours": False, "Weekly": False, "Monthly": True, "90 Days": False}
                    },
                    {
                        "description": "b. If your added audiences are below 80% of traffic check add new audiences",
                        "frequency": {"Every 72 Hours": False, "Weekly": False, "Monthly": True, "90 Days": False}
                    }
                ]
            },
            {
                "task": "12. Demographic Performance",
                "subtasks": [
                    {
                        "description": "a. Review demographics and add exclusions (or bid optimisations if not using smart bidding)",
                        "frequency": {"Every 72 Hours": False, "Weekly": False, "Monthly": False, "90 Days": True},
                        "additional_info": [
                            "> by age",
                            "> by income (not available worldwide)"
                        ]
                    }
                ]
            },
            {
                "task": "13. When ads appeared",
                "subtasks": [
                    {
                        "description": "a. Review performance by day of the week and exclude any days with consistent & significant under performance and exclude (if not using smart bidding)",
                        "frequency": {"Every 72 Hours": False, "Weekly": False, "Monthly": False, "90 Days": True}
                    },
                    {
                        "description": "a. Review performance by hour of the day and look to increase your budget if your spending is not sufficient for the whole day (or for Ad schedule)",
                        "frequency": {"Every 72 Hours": False, "Weekly": False, "Monthly": False, "90 Days": True}
                    }
                ]
            }
        ]
    },
    {
        "section": "Ads & Landing Pages",
        "color": "#ADD8E6",  # Light blue
        "tasks": [
            {
                "task": "14. Landing Page Review",
                "subtasks": [
                    {
                        "description": "a. If you are sending ads to different landing/product pages review your Conversion rates by landing pages. If any landing pages have a significantly lower conversion rate look at updating/changing the landing pages",
                        "frequency": {"Every 72 Hours": False, "Weekly": False, "Monthly": False, "90 Days": True}
                    },
                    {
                        "description": "b. Review your product pages:",
                        "frequency": {"Every 72 Hours": False, "Weekly": False, "Monthly": False, "90 Days": True},
                        "additional_info": [
                            "> Do your product pages have price transparency (clear price & shipping costs)",
                            "> Do your product pages have clear policies for returns & delivery",
                            "> Do your product pages have a sizing guide",
                            "> Do your product pages include credibility markers like testimonials & product reviews"
                        ]
                    },
                    {
                        "description": "c. Review landing page load time https://pagespeed.web.dev/",
                        "frequency": {"Every 72 Hours": False, "Weekly": False, "Monthly": False, "90 Days": True}
                    }
                ]
            }
        ]
    },
    {
        "section": "Bidding",
        "color": "#FFD700",  # Gold
        "tasks": [
            {
                "task": "15. Campaign Bidding Review",
                "subtasks": [
                    {
                        "description": "a. Is there enough Conversion Data to switch to Max Conversions or Max Conversion Value? (check below)",
                        "frequency": {"Every 72 Hours": False, "Weekly": False, "Monthly": False, "90 Days": True},
                        "additional_info": [
                            "> Is there an average of at least 1 primary conversion per day over the past 30 days?",
                            "> Have weekly conversions been increasing each week for the past 4-6 weeks?"
                        ]
                    },
                    {
                        "description": "b. If you are using a tCPA / tROAS, is the current campaign bidding target still the best option? Or is it limiting performance? (check these metrics to see if you need to adjust your target)",
                        "frequency": {"Every 72 Hours": False, "Weekly": False, "Monthly": True, "90 Days": True},
                        "additional_info": [
                            "> Is there a drop in total conversions / conversion value",
                            "> Has the campaign spend reduced significantly",
                            "> Are the impressions dropping too much"
                        ]
                    }
                ]
            }
        ]
    },
    {
        "section": "Quality Control Checks",
        "color": "#D3D3D3",  # Light gray
        "tasks": [
            {
                "task": "16. Quality Control Checks",
                "subtasks": [
                    {
                        "description": "a. Are all conversion actions working",
                        "frequency": {"Every 72 Hours": False, "Weekly": False, "Monthly": True, "90 Days": False}
                    },
                    {
                        "description": "b. Is your budget on track",
                        "frequency": {"Every 72 Hours": False, "Weekly": False, "Monthly": True, "90 Days": False}
                    },
                    {
                        "description": "c. Is your payment method working",
                        "frequency": {"Every 72 Hours": False, "Weekly": False, "Monthly": True, "90 Days": False}
                    },
                    {
                        "description": "d. Are there any active 'auto apply' recommendations in the account",
                        "frequency": {"Every 72 Hours": False, "Weekly": False, "Monthly": True, "90 Days": False}
                    },
                    {
                        "description": "e. Are there any notifications from Google that need to be actioned",
                        "frequency": {"Every 72 Hours": False, "Weekly": False, "Monthly": True, "90 Days": False}
                    },
                    {
                        "description": "e. Are there any notifications from GMC that need to be actioned",
                        "frequency": {"Every 72 Hours": False, "Weekly": False, "Monthly": True, "90 Days": False}
                    }
                ]
            }
        ]
    }
]

# Display the selected page
if page == "Search Optimization":
    display_tasks(search_optimization_data, "Search Optimization")
elif page == "Shopping":
    display_tasks(shopping_data, "Shopping")
