"""Frameworks for running multiple Streamlit applications as a single app.
    https://github.com/upraneelnihar/streamlit-multiapps
"""
import streamlit as st

class MultiApp:
    """Framework for combining multiple streamlit applications.
    Usage:
        def foo():
            st.title("Hello Foo")
        def bar():
            st.title("Hello Bar")
        app = MultiApp()
        app.add_app("Foo", foo)
        app.add_app("Bar", bar)
        app.run()
    It is also possible keep each application in a separate file.
        import foo
        import bar
        app = MultiApp()
        app.add_app("Foo", foo.app)
        app.add_app("Bar", bar.app)
        app.run()
    """
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        """Adds a new application.
        Parameters
        ----------
        func:
            the python function to render this app.
        title:
            title of the app. Appears in the dropdown in the sidebar.
        """
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):

        # Set width of the sidebar
        st.markdown(
            """
            <style>
            [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
                width: 200px;
            }
            [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
                width: 500px;
                margin-left: -500px;
            }
            </style>
            """,
            unsafe_allow_html=True,)

        app = st.sidebar.selectbox(
            'Go To',
            self.apps,
            format_func=lambda app: app['title'])

        app['function']()