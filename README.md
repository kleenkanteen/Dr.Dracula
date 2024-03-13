<!-- Designed for LEAP24 hackathon 03.2024-->
<div id="header" align="center">
  <img src="./frontend/src/assets/img/vampire.jpg"/>

</div>
  <h1 align="center">Dr. Dracula</h1>
   <h3 align="center">Simplifying your blood test analysis</h3>

## Description

A website that allows you to understand your blood test results by simply uploading a PDF of your results.

## Table of Contents

<details>
<summary>Dr. Dracula</summary>

- [Application Description](#application-description)
- [Table of Contents](#table-of-contents)
- [Demo](#demo)
- [Technology Stack](#technology-stack)
- [Features](#features)
- [Screenshots](#screenshots)
- [Developement Guide](#how-to-use-the-app)
- [Authors](#authors)
- [License](#license)

</details>
 
## Demo

[Try the Demo](https://dr-dracula.vercel.app/)

## Watch the Pitch

[Watch project pitch](https://lablab.ai/event/leap-2024-hackathon/dracula/dr-dracula)


## Technology Stack

| Technology                                                    | Description                                                          |
| ------------------------------------------------------------- | -------------------------------------------------------------------- |
| TypeScript                                                    | The one and only.
| FastAPI                                                       | Modern web framework for building APIs with Python.
| Next.js                                                       | The goat.
| ShadCn                                                        | Beautifully designed components.
| OpenAI Python Library                                         | Library to interact with OpenAI's models.
| PyMuPDF                                                       | PDF reading library.
| Beautiful Soup 4                                              | Web scraping library.


## Features

- PDF upload for blood test analysis.
- Automated biomarker extraction from PDF.
- Analysis generated using comparison with vetted medical source, testing.com.


## Screenshots
![pic111](https://github.com/kleenkanteen/Dr.Dracula/assets/19821445/bcbd74d8-7a34-4444-888e-9edae922f2f4)
![pic222](https://github.com/kleenkanteen/Dr.Dracula/assets/19821445/3157c83e-abcf-45fb-8240-ebb00053982b)

## Developement Guide

**Step #1** - Clone the project

```bash
$ git clone https://github.com/kleenkanteen/leap-hackathon
```

**Step #2**

- `cd` into the `frontend` folder and type `yarn`. Please stick to yarn for consistency with the team.
- Run `yarn run dev` to run the nextjs frontend
- Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

In a separate terminal:
- `cd` into the `backend` folder. Run `pip install -r requirements.txt` to install the python dependencies.
- Run `uvicorn main:app --reload` to run the fastapi server on port 8000 with hot reload on.

## Authors

| Name            | Link                                   |
| --------------- | -------------------------------------- |
| Vincent Castro | https://github.com/risingsunomi |
| Sabih Sarowar | https://github.com/kleenkanteen |
| Sandra Ashipala | https://github.com/sandramsc |
| Mazen Mamdouh | https://github.com/MazenMamdouh371 |

<h2 align="center">LEAP24 Hackathon Submission</h2>

<div id="header" align="center">
  <img src="https://lablab.ai/_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Flablab-static-eu%2Fimages%2Fevents%2Fclsvwsh8m000x3b6rhvbmf7cf%2Fundefined_imageLink_xbaa800rg.jpg&w=1080&q=75" width="500" height="200"/>
</div>

## License

[![GitLicense](https://img.shields.io/badge/License-MIT-lime.svg)](https://github.com/sandramsc/leap-hackathon/blob/master/LICENSE)
