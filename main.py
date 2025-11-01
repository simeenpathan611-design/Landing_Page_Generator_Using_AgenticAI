from crew.crew_setup import create_crew
from jinja2 import Environment, FileSystemLoader
import streamlit as st
import os

st.set_page_config(page_title="Landing Page Generator", layout="wide")
st.title("AI-Powered Landing Page Generator")
st.markdown("This application generates high-converting landing pages using a specialized crew of AI agents.")

product_description = st.text_area("Enter Product Description", height=150,placeholder="eg: A revolutionary new fitness app that personalizes workouts and tracks progress in real-time.")
generate_btn = st.button("Generate Landing Page")

if generate_btn and product_description.strip():
    with st.spinner("Generating landing page..."):
        try:
            crew = create_crew()
            results = crew.kickoff(inputs={"product_description":product_description})

            content = results.get("Generate Landing Page Content", "")
            layout = results.get("Design Layout", "")
            seo_optimized_content = results.get("Optimize SEO", "")
            branded_content = results.get("Ensure Branding", "")
            proofread_content = results.get("Proofread Content", "")


        # Save to HTML using Jinja2
            env = Environment(loader=FileSystemLoader('.'))
            template = env.get_template('templates/landing_page_template.html')

            html_output = template.render(
                title="AI Generated Landing Page",
                headline="",
                subheadline="",
                features=[],
                call_to_action="",
                body=proofread_content
                
            )

            os.makedirs('output', exist_ok=True)
            output_path = os.path.join('output', 'landing_page.html')   
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(html_output)

            st.success("Landing page generated successfully!")
            st.markdown("### Generated Landing Page Content")

            with st.expander("Preview Landing Page HTML"):
                st.components.v1.html(html_output,height=600,scrolling=True) 
        
        except Exception as e:
            st.error(f"An error occurred: {e}")
else:
    st.info("Please enter a product description to generate a landing page.")
    