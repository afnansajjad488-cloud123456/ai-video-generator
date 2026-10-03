# n8n production endpoints

## Workflow 1 — Script & Scenes
POST https://founder-workstation.taila75704.ts.net:8443/webhook/generate-video

Body:
{
  "prompt": "your topic",
  "language": "Urdu",
  "duration": 30,
  "aspect_ratio": "16:9",
  "resolution": "1080p",
  "style": "documentary",
  "voice": ""
}

## Workflow 2 — Images & Voice
POST https://founder-workstation.taila75704.ts.net:8443/webhook/generate-assets

Body:
{
  "job_id": "<job returned by Workflow 1>"
}

## Workflow 3 — Render Preparation
POST https://founder-workstation.taila75704.ts.net:8443/webhook/prepare-render

Body:
{
  "job_id": "<same job id>"
}

## Workflow 4 — Finalize
POST https://founder-workstation.taila75704.ts.net:8443/webhook/finalize-video

Body:
{
  "job_id": "<same job id>",
  "final_video_url": "<public MP4 URL>",
  "thumbnail_url": null,
  "subtitles_url": "<public SRT URL>"
}

IMPORTANT:
Workflow 4 requires a real final_video_url. Workflow 3 currently prepares the render manifest/SRT but does not itself produce the final MP4. A renderer/upload step must exist between Workflow 3 and Workflow 4.

The frontend calls Workflow 1, then Workflow 2, then Workflow 3 automatically from the Generate Video button.
