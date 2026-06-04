import streamlit as st
import datetime
from task_manager import TaskManager
from factories.task_factory import TaskFactory
from strategies.sort_by_name import SortByName
from strategies.sort_by_priority import SortByPriority

if 'manager' not in st.session_state:
    st.session_state.manager = TaskManager()

tm = st.session_state.manager

st.set_page_config(page_title="AI-Native Task Manager", layout="wide")

with st.sidebar:
    st.header("➕ Create New Task")
    
    task_type = st.selectbox("Task Type", ["simple", "deadline", "recurring"])
    
    with st.form("add_task_form", clear_on_submit=True):
        title = st.text_input("Task Title")
        desc = st.text_input("Description (Optional)")
        priority_str = st.select_slider("Priority", options=["Low", "Medium", "High"], value="Medium")
        
        priority_map = {"High": 1, "Medium": 2, "Low": 3}
        priority = priority_map[priority_str]
        
        extra_kwargs = {}
        
        if task_type == "deadline":
            due_date = st.date_input("Due Date", datetime.date.today())
            due_time = st.time_input("Due Time", datetime.time(12, 0))
            extra_kwargs["due_date"] = datetime.datetime.combine(due_date, due_time)
            
        elif task_type == "recurring":
            extra_kwargs["interval_days"] = st.number_input("Interval (Days)", min_value=1, value=1, step=1)
            next_run_date = st.date_input("Next Run Date", datetime.date.today())
            extra_kwargs["next_run"] = datetime.datetime.combine(next_run_date, datetime.time.min)
        
        if st.form_submit_button("Add Task"):
            if title:
                new_task = TaskFactory.create_task(
                    task_type, 
                    title=title, 
                    description=desc, 
                    priority=priority, 
                    **extra_kwargs
                )
                tm.add_task(new_task)
                st.success(f"Task '{title}' added!")
                st.rerun()
            else:
                st.error("Title is required.")

st.title("🎯 Task Manager Dashboard")

all_tasks = tm.get_all_tasks()
completed = [t for t in all_tasks if t.is_completed()]

col1, col2, col3 = st.columns(3)
col1.metric("Total Tasks", len(all_tasks))
col2.metric("Completed", len(completed))
col3.metric("Pending", len(all_tasks) - len(completed))

st.divider()

st.subheader("📋 Task List")
sort_mode = st.radio("Sort by:", ["Name", "Priority"], horizontal=True)

if sort_mode == "Name":
    tm.set_sort_strategy(SortByName())
else:
    tm.set_sort_strategy(SortByPriority())

if not all_tasks:
    st.info("No tasks available. Add one from the sidebar!")
else:
    for t in tm.get_all_tasks():
        status_icon = "✅" if t.is_completed() else "⏳"
        with st.expander(f"{status_icon} {t.get_info()}"):
            c1, c2 = st.columns([4, 1])
            c1.write(f"ID: {t.get_id()}")
            if not t.is_completed():
                if c2.button("Done", key=f"btn_{t.get_id()}"):
                    tm.mark_task_completed(t.get_id())
                    st.rerun()
