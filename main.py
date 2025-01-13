from sqlalchemy import create_engine, text
import pandas as pd
import streamlit as st
from sentence_transformers import SentenceTransformer


def connect_db():
    connection_string = (
        "postgresql://db-ebape_owner:TAL8FBZH1iCp@"
        "ep-blue-dust-a59whnj4.us-east-2.aws.neon.tech/db-ebape?"
        "sslmode=require&options=endpoint%3Dep-blue-dust-a59whnj4"
    )
    engine = create_engine(connection_string)
    return engine.connect()

def run_query(conn, query_embedding):
    query = text('''
    SELECT abstract FROM papers ORDER BY embedding <=> :query_embedding LIMIT 5           
    ''')        

    df1 = pd.read_sql(sql=query, con=conn, params={"query_embedding":query_embedding})

    return df1

def show_dashboard():
    st.header("Teste")

    model = SentenceTransformer('all-MiniLM-L6-v2')

    st.text_input("Type an expression: ", key="query")

    query = st.session_state.query.lower()

    if query:
        embedding = model.encode(query)
        embedding_str = str(embedding.tolist())
        print(embedding_str)

        conn = connect_db()
        df1 = run_query(conn, embedding_str)

        st.write(df1)
        
if __name__ == "__main__":
    show_dashboard()
