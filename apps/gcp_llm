#############################################################################
######################### SETTING UP GCP ENVIRONMENT ########################
#############################################################################

import vertexai
from vertexai.language_models import TextGenerationModel
from vertexai.preview.generative_models import GenerationConfig, GenerativeModel


PROJECT_ID = "lbplc-reboot24lon-883"
REGION = 'europe-west2'  # London
vertexai.init(project=PROJECT_ID, location=REGION)


# Text Bison 002 (palm)
TEXTBISON_PARAMETERS_PT = {
    "temperature":0.8,
    "top_k": 40,
}
def textbison_llm_pt(
        prompt,
        TEXTBISON_PARAMETERS_PT=TEXTBISON_PARAMETERS_PT,
):
    TEXTBISON_MODEL_PT = TextGenerationModel.from_pretrained("text-bison@002")
    response = TEXTBISON_MODEL_PT.predict(prompt, **TEXTBISON_PARAMETERS_PT).text
    return response

# Gemini-1.0
GEMINI_PARAMETERS_PT = GenerationConfig(
    temperature=0.9,
    top_p=1.0,
    top_k=40,
    max_output_tokens=8192,
)
def gemini_llm_pt(
        prompt,
        GEMINI_PARAMETERS_PT=GEMINI_PARAMETERS_PT,
):
    GEMINI_MODEL_PT = GenerativeModel("gemini-1.0-pro")
    response = GEMINI_MODEL_PT.generate_content(
        prompt,
        generation_config=GEMINI_PARAMETERS_PT,
    ).candidates[0].content.parts[0].text
    return response