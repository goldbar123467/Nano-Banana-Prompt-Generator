# Build Instructions

## Step 1 - Project Setup

Create a HuggingFace Space directory structure. You need app.py as the main application and requirements.txt for dependencies. Nothing else.

## Step 2 - Requirements

Include gradio and huggingface_hub in requirements. Pin gradio to version 4 or higher for the latest features.

## Step 3 - Glassmorphism CSS

Inject custom CSS into the Gradio app using the css parameter. The aesthetic must include a dark gradient background moving from deep purple to near black. All containers should have frosted glass effect using backdrop-filter blur, rgba backgrounds with low opacity around 0.1 to 0.2, subtle white or cyan border with low opacity, border-radius of 16 to 24 pixels, and soft box shadow with colored glow. The primary accent is banana yellow hex FFE135. Secondary accent is electric cyan hex 00FFFF. Text should be white with high readability. Buttons need glass effect with yellow glow on hover. The output JSON display should be in a monospace font inside a glass card with subtle syntax-style coloring.

## Step 4 - Interface Layout

Use Gradio Blocks for custom layout control. Create a centered container with max width around 800 pixels. Add a glassy header with the title Nano Banana Prompt Lab and a small banana emoji. Below that place the input textbox with placeholder text like "banana wearing a tiny cowboy hat" and style it with glass effect. Next row has the camera dropdown with options iPhone 15 Pro and Sony A7IV and Fujifilm X100V and Canon R5 and default to iPhone. Same row has a slider labeled Realism from 0 to 100 defaulting to 75. Generate button below styled as a glowing glass pill shape. Output area is a large textbox or JSON display component styled as a glass card. Add a copy to clipboard button next to or below the output.

## Step 5 - Model Integration

Use the HuggingFace Inference API with the InferenceClient from huggingface_hub. Choose Mistral 7B Instruct or Mixtral 8x7B for quality. The model selection should work without needing an API key when running on HF Spaces with Pro subscription. Structure the call as a chat completion with system prompt and user message.

## Step 6 - System Prompt Construction

Build the system prompt to include all vocabulary banks from the claude.md specification. Tell the model it is a professional photography director. Instruct it to output only valid JSON with no markdown code fences and no explanation text before or after. The JSON structure must match the schema defined in claude.md with subject and camera and lighting and environment and technical and mood sections.

## Step 7 - User Prompt Construction

Take the user input and combine it with their camera selection and realism level. Format it as a clear instruction like "Create a photorealistic prompt for: user input here. Camera: their selection. Realism level: their slider value where 100 is documentary photography and 0 is slightly stylized."

## Step 8 - Response Handling

Parse the model response as JSON. If parsing fails, display the raw text with an error note. If successful, pretty print the JSON with indentation in the output display. Make sure the copy button copies the raw JSON string ready for pasting into Gemini.

## Step 9 - Error States

Handle API errors gracefully with a glass-styled error message. If the model returns invalid JSON, show a warning but still display what was returned so the user can manually fix it.

## Step 10 - Final Polish

Add a subtle animated gradient or glow effect to the background if possible without heavy performance impact. Ensure mobile responsiveness so the glass cards stack properly on small screens. Test that the copy functionality works across browsers.

## Deployment Notes

When pushing to HuggingFace Spaces, the app should auto-detect the gradio SDK. Make sure the Space is set to public for discoverability. Add a good README with example outputs and a thumbnail that shows off the glassmorphism UI.
