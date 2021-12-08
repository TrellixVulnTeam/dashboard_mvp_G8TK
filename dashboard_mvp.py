
import streamlit as st
import plotly.figure_factory as ff

df = [dict(Task="MySQL", Start='2017-01-01', Finish='2017-02-02', Resource='🔥🔥🔥🔥🔥', Description='https://app.clickup.com/t/2575789/DEV-5552'),
      dict(Task="MySQL", Start='2017-02-15', Finish='2017-03-15', Resource='🔥🔥🔥🔥', Description='https://app.clickup.com/t/2575789/DEV-5339'),
      dict(Task="YouTube", Start='2017-01-23', Finish='2017-02-17', Resource='🔥🔥🔥', Description='https://app.clickup.com/t/2575789/DEV-4545'),
      dict(Task="YouTube", Start='2017-01-17', Finish='2017-01-25', Resource='🔥', Description='https://app.clickup.com/t/2575789/DEV-4545'),
      dict(Task="Facebook Ads", Start='2017-03-10', Finish='2017-03-20', Resource='🔥🔥', Description='https://app.clickup.com/t/2575789/DEV-4545'),
      dict(Task="Facebook Ads", Start='2017-04-01', Finish='2017-04-20', Resource='🔥🔥🔥🔥🔥', Description='https://app.clickup.com/t/2575789/DEV-4440'),
      dict(Task="Facebook Ads", Start='2017-05-18', Finish='2017-06-18', Resource='🔥🔥🔥🔥', Description='https://app.clickup.com/t/2575789/DEV-5699'),
      dict(Task="Shopify", Start='2017-01-14', Finish='2017-03-14', Resource='🔥🔥', Description='https://app.clickup.com/t/2575789/DEV-4445')]

colors = {'🔥🔥🔥🔥🔥': 'rgb(220, 0, 0)',
          '🔥🔥🔥🔥': 'rgb(231, 84, 128)',
          '🔥🔥🔥': 'rgb(255,230,0)',
          '🔥🔥': 'rgb(255, 204, 0)',
         '🔥': 'rgb(255,255,51)',
         }

fig = ff.create_gantt(df, title='Tickets by Integration & Priority - Gantt View', colors=colors, index_col='Resource', show_colorbar=True,
                      group_tasks=True)

st.plotly_chart(fig, use_container_width=True)
st.header("Small Gantt Chart Mock Up with Dummy data")
st.write("When you hover over the ticket bars, you'll get the link to the ClickUp ticket.")
st.write("On the right top corner you can make the chart full screen.")
