from crewai import Crew
from crew.tasks import (
    generate_content_task,
    design_layout_task,
    optimize_seo_task,
    ensure_branding_task,
    proofread_content_task,
)
from crew.agents import (
    content_agent,
    layout_agent,
    seo_agent,
    branding_agent,
    proofreading_agent,
)

def create_crew() -> Crew:
    crew = Crew(
        name="Landing Page Generator Crew",
        description="A crew specialized in generating high-converting landing pages.",
        tasks=[
            generate_content_task,
            design_layout_task,
            optimize_seo_task,
            ensure_branding_task,
            proofread_content_task,
        ],
        agents=[
            content_agent,
            layout_agent,
            seo_agent,
            branding_agent,
            proofreading_agent,
        ],
        verbose=True,
    )
    return crew
