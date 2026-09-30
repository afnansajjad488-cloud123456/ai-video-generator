# ShortForge AI — Urdu AI Shorts

## Website

https://afnansajjad488-cloud123456.github.io/ai-video-generator/

## Repository

https://github.com/afnansajjad488-cloud123456/ai-video-generator

ShortForge AI is an AI-powered Urdu video studio for creating faceless YouTube Shorts from an optional topic prompt.

## Features

- Urdu AI Shorts
- Optional topic input
- Automatic topic generation when topic is blank
- AI script generation
- 10 AI scene definitions
- AI visual generation workflow
- Automated video generation through n8n
- Supabase authentication
- Email verification / OTP
- Password reset
- Daily 4-video server-side limit
- Video preview
- Topic and narration metadata
- Original video open/download
- Full-video slow-motion editing
- Original and slow-motion versions kept separately

## Tech

- HTML
- CSS
- JavaScript
- Supabase
- Supabase Edge Functions
- n8n
- Gemini
- Cloudinary
- FFmpeg / TTS where applicable

## Deployment

The official free website is the GitHub Pages URL above. The unregistered `urduclipforge.com` domain is not used by this project.

## Architecture

Website → Supabase Auth → Supabase Edge Function → n8n → Gemini / media pipeline → Cloudinary → final video.

Slow motion uses an authenticated Edge Function and a separate derived video URL; the original generated video is not overwritten.
