from crewai import Task
from crew.agents import content_agent, layout_agent, seo_agent, branding_agent, proofreading_agent

generate_content_task = Task(
    description=(
        "Generate creative Landing Page Content for {product_description}. "
        "Include headline, subheadline, body text, and call-to-action."
    ),
    agent=content_agent,
    expected_input="Product description and target audience details",
    expected_output="A complete landing page copy with headline, subheadline, body text, and call-to-action"
)

design_layout_task = Task(
    description=(
        "Design a visually appealing and user-friendly landing page layout. "
        "Include sections such as header, features, and call-to-action."
    ),
    agent=layout_agent,
    expected_input="Landing page content",
    expected_output="A structured layout design for the landing page with clear sections"
)

optimize_seo_task = Task(
    description=(
        "Optimize the landing page content for SEO. "
        "Include relevant keywords naturally in the text."
    ),
    agent=seo_agent,
    expected_input="Landing page content",
    expected_output="SEO-optimized landing page content with relevant keywords integrated"
)

ensure_branding_task = Task(
    description=(
        "Ensure the landing page content and design align with brand identity. "
        "Maintain consistent tone, style, and visual elements."
    ),
    agent=branding_agent,
    expected_input="Landing page content and layout",
    expected_output="Brand-aligned landing page content and layout with consistent tone and visuals"
)

proofread_content_task = Task(
    description=(
        "Proofread the landing page content for grammatical accuracy, clarity, and quality. "
        "Make necessary corrections to ensure professionalism."
    ),
    agent=proofreading_agent,
    expected_input="Final landing page content",
    expected_output="Proofread and polished landing page content free of grammatical and clarity issues"
)