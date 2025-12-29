# Nano Banana Prompt Generator

## Purpose

A HuggingFace Space that generates hyper-realistic photography prompts for Gemini's nano banana image generation trend. Our edge is professional photography vocabulary that makes outputs look like actual iPhone or DSLR shots.

## Core Concept

Users describe a vibe or scenario. We output a detailed JSON prompt packed with real camera terminology, lighting vocabulary, and sensor artifacts that trick Gemini into photorealistic output.

## Tech Stack

- Gradio for the interface
- Mistral or Llama 3.1 via HuggingFace Inference API for prompt generation
- Single app.py file
- requirements.txt with gradio and huggingface_hub

## UI Requirements

Web3 glassmorphism aesthetic throughout. Think frosted glass panels, subtle gradients, soft glows, translucent containers. Use Gradio's custom CSS injection to achieve this. Dark background with glass card overlays. Accent color should be banana yellow with cyan highlights.

## User Flow

User enters a simple idea like "banana at a coffee shop" or "banana as a wizard." They can optionally select a camera type from iPhone 15 Pro, Sony A7IV, Fujifilm X100V, or Canon R5. They can adjust a realism slider from stylized to documentary. They hit generate and receive a fully detailed JSON prompt ready to paste into Gemini.

## Output Format

The generated JSON must include these sections: subject with description and scale reference and surface texture, camera with device and focal length and aperture and focus description, lighting with source and quality and color temperature, environment with setting and background treatment and atmosphere, technical with noise characteristics and white balance and compression artifacts, and finally an overall mood descriptor.

## Vocabulary Banks

The language model must draw from professional photography terminology.

For focus terminology use words like tack-sharp, razor-thin plane of focus, focus falloff, micro hunting blur, eye detect lock, subject separation.

For lighting use terms like rim lighting, hair light, fill bounce, specular highlights, subsurface scattering on the banana skin, caustic light patterns, motivated lighting, practical sources, golden hour wrap, north light diffusion.

For lens characteristics include chromatic aberration on high contrast edges, subtle barrel distortion, natural vignette falloff, bokeh rendering with cats eye shapes in corners, focus breathing.

For sensor and digital artifacts reference subtle shadow noise, highlight rolloff, ISO grain structure, banding in gradients, HEIC compression, computational photography stacking artifacts, Smart HDR tone mapping.

For phone-specific realism mention computational bokeh with edge detection errors, night mode temporal stacking, lens flare from point light sources, the specific color science of iPhone or Pixel or Samsung.

## System Prompt for the LLM

The model should act as a professional photography director who specializes in macro and product photography. It takes simple concepts and expands them into technically detailed shooting specifications. It never uses generic terms like beautiful lighting or nice bokeh. Every descriptor must be specific and technical. The output must feel like a real photographer's shot notes.

## Important Constraints

Keep the interface minimal. One text input, camera dropdown, realism slider, generate button, output display with copy button. No cluttered options. The glassmorphism should feel premium not busy. Response time matters so use streaming if possible.
