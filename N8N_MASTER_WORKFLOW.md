# One-click video generation workflow

The website's **Generate Video** button now orchestrates the n8n stages in order:

1. **Workflow 1 — Script & Scenes**
   - POST `/webhook/generate-video`
   - Receives the user's prompt.
   - Creates the Supabase `video_jobs` row.
   - Generates Gemini script and scenes.
   - Returns `job_id`.

2. **Workflow 2 — Images & Voice**
   - POST `/webhook/generate-assets`
   - Sends the same `job_id`.
   - Generates scene images.
   - Generates ElevenLabs narration.
   - Uploads the generated assets.

3. **Workflow 3 — Render Preparation**
   - POST `/webhook/prepare-render`
   - Sends the same `job_id`.
   - Builds the timing manifest.
   - Creates SRT subtitles.
   - Marks the job `render_ready`.

4. **Final renderer**
   - Must combine the uploaded scene images + scene audio + SRT into one MP4.
   - The renderer must upload the MP4 to public/object storage and obtain `final_video_url`.

5. **Workflow 4 — Finalize**
   - POST `/webhook/finalize-video`
   - Body contains `job_id` and the real `final_video_url`.
   - Saves the final URL and marks the job `completed`.

## Why Workflow 4 is not called automatically yet

The current Workflow 3 is a preparation workflow, not an MP4 renderer. It does not return a final MP4 URL. Calling Workflow 4 before a real `final_video_url` exists would fail its validation.

## Production webhook used by the frontend

`https://founder-workstation.taila75704.ts.net:8443/webhook/generate-video`

The frontend also calls:

- `https://founder-workstation.taila75704.ts.net:8443/webhook/generate-assets`
- `https://founder-workstation.taila75704.ts.net:8443/webhook/prepare-render`

Do not put Supabase service-role keys, Gemini keys, ElevenLabs keys, or other secrets into the GitHub Pages frontend.

## Browser/CORS

Because the frontend calls n8n from a browser, the n8n endpoint/reverse proxy must allow the deployed GitHub Pages origin. If the browser reports a CORS error, fix CORS/reverse-proxy configuration on the n8n side rather than exposing credentials in the frontend.
