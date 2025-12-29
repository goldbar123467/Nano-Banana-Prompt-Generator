import os
import gradio as gr
from huggingface_hub import InferenceClient

# Glassmorphism CSS Theme
CUSTOM_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Inter:wght@400;500&family=JetBrains+Mono:wght@400;500&display=swap');

/* Base typography */
* {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, system-ui, sans-serif !important;
    -webkit-font-smoothing: antialiased !important;
    -moz-osx-font-smoothing: grayscale !important;
}

/* Space background with stars */
.gradio-container {
    background: #0a0a0f !important;
    min-height: 100vh;
    position: relative;
    overflow-x: hidden;
}

.gradio-container::before {
    content: '';
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background:
        radial-gradient(1px 1px at 20px 30px, #fff, transparent),
        radial-gradient(1px 1px at 40px 70px, rgba(255,255,255,0.8), transparent),
        radial-gradient(1px 1px at 50px 160px, rgba(255,255,255,0.6), transparent),
        radial-gradient(1px 1px at 90px 40px, #fff, transparent),
        radial-gradient(1px 1px at 130px 80px, rgba(255,255,255,0.7), transparent),
        radial-gradient(1px 1px at 160px 120px, #fff, transparent),
        radial-gradient(1.5px 1.5px at 200px 50px, rgba(139,92,246,0.9), transparent),
        radial-gradient(1px 1px at 220px 150px, rgba(255,255,255,0.6), transparent),
        radial-gradient(1px 1px at 280px 90px, #fff, transparent),
        radial-gradient(1px 1px at 320px 20px, rgba(255,255,255,0.8), transparent),
        radial-gradient(1.5px 1.5px at 350px 130px, rgba(0,255,255,0.8), transparent),
        radial-gradient(1px 1px at 400px 60px, #fff, transparent),
        radial-gradient(1px 1px at 450px 170px, rgba(255,255,255,0.7), transparent),
        radial-gradient(1px 1px at 500px 30px, #fff, transparent),
        radial-gradient(1px 1px at 550px 100px, rgba(255,255,255,0.6), transparent),
        radial-gradient(1.5px 1.5px at 600px 140px, rgba(139,92,246,0.7), transparent),
        radial-gradient(1px 1px at 650px 50px, #fff, transparent),
        radial-gradient(1px 1px at 700px 180px, rgba(255,255,255,0.8), transparent),
        radial-gradient(1px 1px at 750px 80px, #fff, transparent),
        radial-gradient(1px 1px at 800px 120px, rgba(255,255,255,0.6), transparent),
        radial-gradient(1px 1px at 100px 200px, #fff, transparent),
        radial-gradient(1px 1px at 180px 250px, rgba(255,255,255,0.7), transparent),
        radial-gradient(1.5px 1.5px at 250px 220px, rgba(0,255,255,0.6), transparent),
        radial-gradient(1px 1px at 330px 280px, #fff, transparent),
        radial-gradient(1px 1px at 420px 230px, rgba(255,255,255,0.8), transparent),
        radial-gradient(1px 1px at 510px 260px, #fff, transparent),
        radial-gradient(1px 1px at 580px 210px, rgba(255,255,255,0.6), transparent),
        radial-gradient(1px 1px at 670px 290px, #fff, transparent),
        radial-gradient(1.5px 1.5px at 720px 240px, rgba(139,92,246,0.8), transparent),
        radial-gradient(1px 1px at 60px 320px, rgba(255,255,255,0.7), transparent),
        radial-gradient(1px 1px at 140px 380px, #fff, transparent),
        radial-gradient(1px 1px at 230px 340px, rgba(255,255,255,0.6), transparent),
        radial-gradient(1px 1px at 300px 400px, #fff, transparent),
        radial-gradient(1px 1px at 390px 350px, rgba(255,255,255,0.8), transparent),
        radial-gradient(1px 1px at 470px 390px, #fff, transparent),
        radial-gradient(1.5px 1.5px at 540px 330px, rgba(0,255,255,0.7), transparent),
        radial-gradient(1px 1px at 620px 370px, rgba(255,255,255,0.6), transparent),
        radial-gradient(1px 1px at 700px 410px, #fff, transparent),
        radial-gradient(1px 1px at 780px 360px, rgba(255,255,255,0.7), transparent);
    background-repeat: repeat;
    background-size: 800px 450px;
    pointer-events: none;
    z-index: 0;
}

.gradio-container::after {
    content: '';
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: radial-gradient(ellipse at 50% 0%, rgba(88, 28, 135, 0.15) 0%, transparent 60%);
    pointer-events: none;
    z-index: 0;
}

/* Main container centering */
.main-container {
    max-width: 720px !important;
    margin: 0 auto !important;
    padding: 2.5rem 1.5rem !important;
    position: relative;
    z-index: 1;
}

/* Glass card effect */
.glass-card {
    background: rgba(15, 15, 25, 0.85) !important;
    backdrop-filter: blur(24px) saturate(1.2) !important;
    -webkit-backdrop-filter: blur(24px) saturate(1.2) !important;
    border: 1px solid rgba(255, 255, 255, 0.06) !important;
    border-radius: 16px !important;
    box-shadow:
        0 4px 24px rgba(0, 0, 0, 0.5),
        inset 0 1px 0 rgba(255, 255, 255, 0.04) !important;
    padding: 1.75rem !important;
    margin-bottom: 1.25rem !important;
}

/* Header styling */
.header-title {
    font-family: 'Space Grotesk', -apple-system, sans-serif !important;
    text-align: center !important;
    color: rgba(255, 255, 255, 0.97) !important;
    font-size: 1.75rem !important;
    font-weight: 700 !important;
    margin-bottom: 0.5rem !important;
    letter-spacing: -0.03em !important;
    line-height: 1.1 !important;
    text-transform: uppercase !important;
}

.header-title span {
    background: linear-gradient(135deg, #fff 0%, rgba(255,255,255,0.7) 100%) !important;
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
    background-clip: text !important;
}

.header-subtitle {
    font-family: 'Inter', sans-serif !important;
    text-align: center !important;
    color: rgba(255, 255, 255, 0.4) !important;
    font-size: 0.8125rem !important;
    font-weight: 400 !important;
    margin-bottom: 0 !important;
    letter-spacing: 0.02em !important;
    line-height: 1.4 !important;
    text-transform: uppercase !important;
}

/* Input styling */
.glass-input textarea, .glass-input input {
    background: rgba(255, 255, 255, 0.03) !important;
    border: 1px solid rgba(255, 255, 255, 0.08) !important;
    border-radius: 10px !important;
    color: rgba(255, 255, 255, 0.9) !important;
    font-size: 0.875rem !important;
    font-weight: 400 !important;
    padding: 0.875rem 1rem !important;
    transition: all 0.2s ease !important;
    letter-spacing: -0.01em !important;
    line-height: 1.5 !important;
}

.glass-input textarea:focus, .glass-input input:focus {
    border-color: rgba(139, 92, 246, 0.4) !important;
    background: rgba(255, 255, 255, 0.05) !important;
    box-shadow: 0 0 0 3px rgba(139, 92, 246, 0.1) !important;
    outline: none !important;
}

.glass-input textarea::placeholder {
    color: rgba(255, 255, 255, 0.25) !important;
    font-weight: 400 !important;
    letter-spacing: -0.01em !important;
}


/* Camera button group */
.camera-buttons {
    display: flex !important;
    gap: 0.5rem !important;
    flex-wrap: wrap !important;
}

.camera-buttons .wrap {
    display: flex !important;
    gap: 0.5rem !important;
    flex-wrap: wrap !important;
    background: transparent !important;
    border: none !important;
    padding: 0 !important;
}

.camera-buttons label {
    display: none !important;
}

.camera-buttons input[type="radio"] {
    display: none !important;
}

.camera-buttons .wrap > label {
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    padding: 0.6rem 1rem !important;
    background: rgba(255, 255, 255, 0.04) !important;
    border: 1px solid rgba(255, 255, 255, 0.08) !important;
    border-radius: 8px !important;
    color: rgba(255, 255, 255, 0.5) !important;
    font-size: 0.8125rem !important;
    font-weight: 500 !important;
    letter-spacing: -0.01em !important;
    cursor: pointer !important;
    transition: all 0.15s ease !important;
    flex: 1 !important;
    min-width: fit-content !important;
}

.camera-buttons .wrap > label:hover {
    background: rgba(139, 92, 246, 0.12) !important;
    border-color: rgba(139, 92, 246, 0.25) !important;
    color: rgba(255, 255, 255, 0.85) !important;
}

.camera-buttons .wrap > label.selected {
    background: rgba(139, 92, 246, 0.18) !important;
    border-color: rgba(139, 92, 246, 0.4) !important;
    color: rgba(255, 255, 255, 0.95) !important;
    box-shadow: 0 0 16px rgba(139, 92, 246, 0.15) !important;
}

/* Generate button */
.generate-btn {
    background: linear-gradient(135deg, #8b5cf6 0%, #06b6d4 100%) !important;
    border: none !important;
    border-radius: 10px !important;
    color: rgba(255, 255, 255, 0.95) !important;
    font-weight: 500 !important;
    font-size: 0.875rem !important;
    letter-spacing: -0.01em !important;
    padding: 0.75rem 2rem !important;
    cursor: pointer !important;
    transition: all 0.15s ease !important;
    box-shadow: 0 2px 12px rgba(139, 92, 246, 0.25) !important;
    width: 100% !important;
    margin-top: 0.75rem !important;
}

.generate-btn:hover {
    background: linear-gradient(135deg, #a78bfa 0%, #22d3ee 100%) !important;
    box-shadow: 0 4px 20px rgba(139, 92, 246, 0.35) !important;
    transform: translateY(-1px) !important;
}

.generate-btn:active {
    transform: translateY(0) !important;
    box-shadow: 0 2px 8px rgba(139, 92, 246, 0.2) !important;
}

/* Output area */
.output-area textarea {
    background: rgba(0, 0, 0, 0.35) !important;
    border: 1px solid rgba(255, 255, 255, 0.06) !important;
    border-radius: 10px !important;
    color: rgba(255, 255, 255, 0.75) !important;
    font-family: 'JetBrains Mono', 'SF Mono', 'Consolas', monospace !important;
    font-size: 0.75rem !important;
    font-weight: 400 !important;
    line-height: 1.65 !important;
    padding: 1.25rem !important;
    letter-spacing: -0.01em !important;
}

.output-area textarea:focus {
    border-color: rgba(255, 255, 255, 0.1) !important;
    outline: none !important;
}

/* Copy button in output */
.output-area button {
    background: rgba(255, 255, 255, 0.05) !important;
    border: 1px solid rgba(255, 255, 255, 0.08) !important;
    border-radius: 6px !important;
    color: rgba(255, 255, 255, 0.5) !important;
    font-size: 0.6875rem !important;
    font-weight: 500 !important;
    letter-spacing: 0 !important;
    padding: 0.35rem 0.625rem !important;
    transition: all 0.15s ease !important;
}

.output-area button:hover {
    background: rgba(255, 255, 255, 0.08) !important;
    color: rgba(255, 255, 255, 0.8) !important;
}

/* Custom copy button */
.copy-btn {
    background: rgba(255, 255, 255, 0.06) !important;
    backdrop-filter: blur(12px) !important;
    -webkit-backdrop-filter: blur(12px) !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    border-radius: 10px !important;
    color: rgba(255, 255, 255, 0.8) !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 0.875rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.02em !important;
    text-transform: uppercase !important;
    padding: 0.875rem 2rem !important;
    cursor: pointer !important;
    transition: all 0.2s ease !important;
    width: 100% !important;
    margin-top: 1rem !important;
    box-shadow: 0 2px 12px rgba(0, 0, 0, 0.2) !important;
}

.copy-btn:hover {
    background: rgba(139, 92, 246, 0.15) !important;
    border-color: rgba(139, 92, 246, 0.3) !important;
    color: rgba(255, 255, 255, 0.95) !important;
    box-shadow: 0 4px 20px rgba(139, 92, 246, 0.2) !important;
    transform: translateY(-1px) !important;
}

.copy-btn:active {
    transform: translateY(0) !important;
}

.copy-btn.copied {
    background: rgba(34, 197, 94, 0.15) !important;
    border-color: rgba(34, 197, 94, 0.3) !important;
    color: rgba(34, 197, 94, 0.95) !important;
}

/* Labels */
label, .label-wrap span {
    color: rgba(255, 255, 255, 0.5) !important;
    font-weight: 500 !important;
    font-size: 0.8125rem !important;
    letter-spacing: -0.01em !important;
    margin-bottom: 0.5rem !important;
}

/* Row spacing */
.glass-card .row {
    gap: 1rem !important;
}

/* Hide footer */
footer {
    display: none !important;
}

/* Scrollbar styling */
::-webkit-scrollbar {
    width: 6px;
    height: 6px;
}

::-webkit-scrollbar-track {
    background: transparent;
}

::-webkit-scrollbar-thumb {
    background: rgba(255, 255, 255, 0.15);
    border-radius: 3px;
}

::-webkit-scrollbar-thumb:hover {
    background: rgba(255, 255, 255, 0.25);
}

/* Mobile responsiveness */
@media (max-width: 768px) {
    .main-container {
        padding: 1rem !important;
    }

    .header-title {
        font-size: 1.375rem !important;
    }

    .header-subtitle {
        font-size: 0.6875rem !important;
        letter-spacing: 0.04em !important;
    }

    .glass-card {
        padding: 1.25rem !important;
        border-radius: 12px !important;
    }

    .generate-btn {
        padding: 0.7rem 1.5rem !important;
        font-size: 0.8125rem !important;
    }

    .camera-buttons .wrap > label {
        font-size: 0.75rem !important;
        padding: 0.5rem 0.75rem !important;
    }

    .output-area textarea {
        font-size: 0.7rem !important;
    }
}
"""

# Photography Vocabulary Banks
VOCABULARY_BANKS = """
FOCUS TERMINOLOGY:
- tack-sharp with razor-thin plane of focus
- subtle focus falloff into creamy bokeh
- micro hunting blur from autofocus acquisition
- eye detect lock with perfect subject separation
- focus breathing visible at close distances

LIGHTING VOCABULARY:
- rim lighting creating luminous edge definition
- hair light adding dimensional separation
- fill bounce from nearby surfaces
- specular highlights on reflective surfaces
- subsurface scattering through translucent banana skin
- caustic light patterns from refractive surfaces
- motivated lighting from practical sources in frame
- golden hour wrap with warm directional quality
- north light diffusion with soft shadow gradients

LENS CHARACTERISTICS:
- chromatic aberration on high contrast edges (purple/green fringing)
- subtle barrel distortion at wide focal lengths
- natural vignette falloff in corners
- bokeh rendering with cats eye shapes in corners
- focus breathing affecting framing at close focus

SENSOR & DIGITAL ARTIFACTS:
- subtle shadow noise in underexposed regions
- highlight rolloff approaching sensor clipping
- ISO grain structure visible in flat midtones
- banding in smooth gradients
- HEIC compression artifacts on fine detail
- computational photography stacking artifacts
- Smart HDR tone mapping with lifted shadows

PHONE-SPECIFIC REALISM:
- computational bokeh with edge detection errors around hair/fine detail
- night mode temporal stacking with motion ghosting
- lens flare artifacts from point light sources
- specific color science: iPhone (neutral-warm), Pixel (contrasty), Samsung (saturated)
- 12-48MP detail levels with pixel binning
"""

# System prompt for the LLM
SYSTEM_PROMPT = f"""You are an elite visual auteur—a polymath who synthesizes the technical mastery of Annie Leibovitz, the compositional genius of Roger Deakins, and the obsessive attention to materiality found in Dutch Golden Age still life painting. Your prose carries the erudition of a Yale MFA thesis defense, yet remains grounded in the empirical precision of a Hasselblad product sheet.

When presented with a concept, you transmute the pedestrian into the transcendent. You perceive the interplay of photons upon curved surfaces, the phenomenology of focus transition zones, the quantum dance of sensor photosites translating reality into digital memory. Your descriptions are layered palimpsests of sensory detail—never resorting to the anemic vocabulary of "nice" or "beautiful," but instead excavating the precise nomenclature that separates the dilettante from the virtuoso.

{VOCABULARY_BANKS}

EXTENDED VOCABULARY - DEPLOY LIBERALLY:

MATERIALITY & TEXTURE:
- waxy cuticle reflecting incident light with Fresnel intensity gradients
- microscopic striations catching rim light at grazing angles
- cellular structure visible through translucent epidermis
- oxidative browning patterns with fractal edge boundaries
- sebaceous surface quality with localized specular hotspots

COMPOSITIONAL DYNAMICS:
- fibonacci spiral drawing the eye through negative space
- rule of thirds intersection anchoring visual weight
- leading lines converging toward the subject's apex
- tonal counterpoint between shadow mass and highlight bloom
- chromatic tension between complementary color registers

TEMPORAL & EPHEMERAL QUALITIES:
- frozen moment of kinetic potential
- liminal threshold between states of being
- durational compression of the decisive instant
- entropic suggestion of imminent transformation

PSYCHOLOGICAL RESONANCE:
- uncanny valley of hyperreal miniaturization
- cognitive dissonance between familiar form and alien scale
- memento mori undertones in organic subject matter
- whimsical subversion of quotidian expectations

Your output must read as if penned by a Cambridge don who moonlights as a Magnum photographer—technically unimpeachable yet lyrically evocative. Each field should contain EXTENSIVE prose, multiple sentences of rich description. Do not be terse. Elaborate. Luxuriate in specificity.

OUTPUT FORMAT:
Output a flowing, natural text prompt that reads like professional photography direction. Structure it as continuous prose organized into clear sections. No JSON, no bullet points, no code formatting. Just rich, descriptive text that can be pasted directly into an image generator.

Structure your response as follows:

SUBJECT: Describe the banana with novelistic attention—its physical details, costume/situation, emotional resonance, scale references that establish the nano size, and surface texture with chromatic gradients and light interaction.

CAMERA: Specify the device, focal length with perspective reasoning, aperture with depth of field implications, and an exhaustive focus description showing where sharpness transitions to bokeh.

LIGHTING: Enumerate all light sources with positions, intensities, and roles. Describe the quality—hardness, shadow gradients, caustics, subsurface effects. Include color temperatures and any white balance choices.

ENVIRONMENT: Paint the setting with cultural connotations, background treatment showing bokeh rendering, and atmospheric qualities like haze or dust motes.

TECHNICAL: Detail sensor behavior—noise patterns, grain structure, compression artifacts, and any computational photography signatures.

End with a MOOD line: a crystalline 5-15 word phrase capturing the emotional essence.

Demonstrate your mastery. Be prolix. Be precise. Be profound."""

def build_user_prompt(concept: str, camera: str, realism: int) -> str:
    """Construct the user prompt from inputs."""
    realism_desc = "documentary photography with maximum technical authenticity" if realism >= 80 else \
                   "highly realistic with subtle stylization" if realism >= 50 else \
                   "stylized but believable photography"

    return f"""Create a photorealistic prompt for: {concept}

Camera: {camera}
Realism level: {realism}/100 ({realism_desc})

Generate the detailed photography prompt."""


def generate_prompt(concept: str, camera: str) -> str:
    """Generate the photography prompt using the LLM."""
    if not concept.strip():
        return "Please enter a concept for your nano banana scene."

    try:
        client = InferenceClient(token=os.environ.get("HF_TOKEN"))

        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": build_user_prompt(concept, camera, 100)}
        ]

        response = client.chat_completion(
            model="meta-llama/Meta-Llama-3-8B-Instruct",
            messages=messages,
            max_tokens=2048,
            temperature=0.85
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"Error: {str(e)}"


# Build the Gradio interface
with gr.Blocks(css=CUSTOM_CSS, theme=gr.themes.Base()) as app:
    with gr.Column(elem_classes="main-container"):
        # Header
        gr.HTML("""
            <div class="glass-card" style="text-align: center; padding: 1.5rem 2rem;">
                <h1 class="header-title"><span>Kyzlo Prompting</span></h1>
                <p class="header-subtitle">Photorealistic Prompt Engine</p>
            </div>
        """)

        # Input section
        with gr.Column(elem_classes="glass-card"):
            concept_input = gr.Textbox(
                label="Your Nano Banana Concept",
                placeholder="banana wearing a tiny cowboy hat at sunset...",
                lines=2,
                elem_classes="glass-input"
            )

            camera_select = gr.Radio(
                label="Camera",
                choices=["iPhone 15 Pro", "Sony A7IV", "Fujifilm X100V", "Canon R5"],
                value="iPhone 15 Pro",
                elem_classes="camera-buttons"
            )

            generate_btn = gr.Button(
                "Generate Prompt",
                elem_classes="generate-btn"
            )

        # Output section
        with gr.Column(elem_classes="glass-card"):
            output_display = gr.Textbox(
                label="Generated Prompt",
                lines=20,
                max_lines=30,
                elem_classes="output-area"
            )

            copy_btn = gr.Button(
                "Copy to Clipboard",
                elem_classes="copy-btn"
            )

            copy_btn.click(
                fn=None,
                inputs=[output_display],
                outputs=[],
                js="(text) => { navigator.clipboard.writeText(text); }"
            )

    # Connect the generate button
    generate_btn.click(
        fn=generate_prompt,
        inputs=[concept_input, camera_select],
        outputs=output_display
    )

# Launch the app
if __name__ == "__main__":
    app.launch()
