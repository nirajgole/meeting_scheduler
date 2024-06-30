import streamlit as st
import argparse as arg
from datetime import datetime, timedelta

from psycopg2 import sql as sql, connect, errors as psyerr

st.set_page_config(layout="wide")
# admin login
parser = arg.ArgumentParser(description="Process some integers!")
parser.add_argument("user_name")

args = parser.parse_args()
st.write(f"Hello {args.user_name}!")


# t = st.time_input("Set an alarm for", datetime.time(8, 45))
# st.write("Alarm is set for", t)
# tabs
tab1, tab2, tab3 = st.tabs(["Schedule", "Insights", "Analytics"])

with tab1:
    pass


def connect_to_db():
    return connect(**st.secrets["postgres"])


st.write("Add user")
user_name = st.text_input("Enter Name")

if st.button("Add new member"):
    conn = None
    try:
        conn = connect_to_db()
        with conn.cursor() as cursor:
            insert_query = f"""INSERT INTO
                calendar.user
                (username)
                VALUES
                ('{user_name}')"""
            cursor.execute(sql.SQL(insert_query))
            conn.commit()
        st.success("Data inserted successfully!")
    except psyerr.UniqueViolation:
        st.error("Username already exists.")
    finally:
        if conn is not None:
            conn.close()


# # Perform query.
# try:
#     people_df = conn.query("SELECT * FROM calendar.user;")
#     # df.hide_index = True
#     # lst = [row.username for row in df.itertuples()]
#     people_list = people_df["username"].tolist()
# except Exception as e:
#     st.write(e)

# options = st.multiselect(
#     "With whom you are meeting.",
#     people_list,
#     people_list[0],
# )


st.write("-------------------------------------------------")

st.write("Add Meeting")

# start = st.time_input("Set an alarm for", datetime.time(8, 45))
# st.write("Alarm is set for", t)
st.write(datetime.now())
meet_title = st.text_input("Enter meeting title.")

try:
    st_conn = st.connection("postgresql", type="sql")
    people_df = st_conn.query("""
                              select
username,
title,
meet_from,
meet_to,
case
when ('2024-06-29 18:08:50' between meet_from and meet_to) or ('2024-06-29 18:08:50' between meet_from and meet_to) then 0
else 1
end
as available
from calendar."user"
left join calendar.schedule cs ON "user".id = cs.user_id
left join calendar.meeting ON meeting.id = cs.meeting_id
                              """)
    people_list = people_df["username"].tolist()
except Exception as e:
    st.write(e)
selected_people = st.multiselect(
    "With whom you are meeting.",
    # people_list,
    people_list,
    people_list[0],
)

# st.write(selected_people)

current_time = datetime.now()

meet_start_date = st.date_input(
    "Meeting start date", current_time, min_value=current_time
)
meet_start_time = st.time_input("Meeting start time", current_time)
meet_end_date = st.date_input("Meeting end date", current_time, min_value=current_time)
default_end_time = (
    current_time + timedelta(minutes=10)
    if meet_end_date == meet_start_date
    else current_time
)

meet_end_time = st.time_input("Meeting end time", default_end_time)

meet_start = datetime.combine(meet_start_date, meet_start_time)
meet_end = datetime.combine(meet_end_date, meet_end_time)

# if st.button('Check availability'):

if st.button("Check availability of members"):
    # st.table(people_df)
    st.table(people_df.query(f"available==1 and username in ({selected_people})"))


if st.button("Create meeting"):
    conn = None
    try:
        conn = connect_to_db()
        with conn.cursor() as cursor:
            insert_query = f"""INSERT INTO
                calendar.meeting
                (title,meet_from,meet_to)
                values
                ('{meet_title}','{meet_start}','{meet_end}')
                """
            cursor.execute(insert_query)
            conn.commit()
        st.success("Data inserted successfully!")
    except psyerr.UniqueViolation:
        st.error("Username already exists.")
    finally:
        if conn is not None:
            conn.close()
