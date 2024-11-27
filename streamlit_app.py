import streamlit as st

st.title("You've Found Strategy Kit")
st.write("Blue Dot Energy Membership Map")
st.write(
    "Take a look at some data viz"
)
# Dashboard options
dashboard_options = {
    "Blue Dotters by ZIP": "https://public.tableau.com/views/BlueDotMembersbyZIPCode/BlueDotNEMembers?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link?:embed=y&:showVizHome=no",
    "Nebraska Voters by Party": "https://public.tableau.com/views/NebraskaVotersbyParty2024/Sheet1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link?:embed=y&showVizHome=no",
    "Campaign Analytics (draft)": "https://public.tableau.com/views/CampaignAnalytics-broadcast/Sheet2?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link?:embed=y&showVizHome=no",
}

# Dropdown to select a Tableau dashboard
selected_dashboard = st.selectbox(
    "Select a Dashboard to View:", list(dashboard_options.keys())
)

# Embed the selected dashboard
st.components.v1.iframe(dashboard_options[selected_dashboard], width=800, height=650)


# Footer
st.write(
    "Powered by [Streamlit](https://streamlit.io/), Tableau Public and StrategyKit."
)
