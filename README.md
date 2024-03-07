<!-- Designed for LEAP24 hackathon 03.2024-->
<div id="header" align="center">
  <img src="./frontend/src/assets/img/drdracula-logo.png" width="700" height="400"/>
</div>
  <h1 align="center">Dr. Dracula</h1>
   <h3 align="center">Simplifying Blood Test Analysis for Personalized Health Insights</h3>

## Application Description

A web application that allows users to understand their blood test results quick easy using AI.

## Table of Contents

<details>
<summary>Dr. Dracula</summary>

- [Application Description](#application-description)
- [Table of Contents](#table-of-contents)
- [Demo](#demo)
- [Technology Stack](#technology-stack)
- [Features](#features)
- [Screenshots](#screenshots)
- [How to use the app locally](#how-to-use-the-app)
- [Using Docker to run the app](#using-docker-to-run-the-app)
- [Authors](#authors)
- [License](#license)

</details>
 
## Demo

[View Demo Video](https://dr-dracula.vercel.app/)


## Technology Stack

| Technology                                                    | Description                                                          |
| ------------------------------------------------------------- | -------------------------------------------------------------------- |
| TypeScript                                                    | TypeScript is a free and open source programming language developed and maintained by Microsoft.
| FastAPI                                                       | a modern, fast (high-performance), web framework for building APIs with Python.
| Next.js                                                       | Next.js is a popular open-source React framework for building web applications.
| ShadCn                                                        | Beautifully designed components that you can copy and paste into your apps.
| OpenAI Python Library                                         | A library that allows developers to interact with OpenAI's powerful models.
| JavaScript                                                    | A versatile and widely used programming language, primarily known for its role in web development.
| PyMuPDF                                                       | A library used for dealing with PDF files in Python.
| Beautiful Soup 4                                              | A library used for web scraping in Python.


## Features

- Seamless PDF upload for blood test analysis.
- Automated biomarker extraction from uploaded PDFs.
- In-depth analysis, comparison with medical sources, and comprehensive report generation.


## Screenshots

![pic222](https://github.com/kleenkanteen/Dr.Dracula/assets/19821445/3157c83e-abcf-45fb-8240-ebb00053982b)
![pic111](https://github.com/kleenkanteen/Dr.Dracula/assets/19821445/bcbd74d8-7a34-4444-888e-9edae922f2f4)

## How to use the app locally

**Step #1** - Clone the project

```bash
$ git clone https://github.com/kleenkanteen/leap-hackathon
```

**Step #2**

- `cd` into the `frontend` folder and type `yarn`. Please stick to yarn for consistency with the team.
- Run `yarn run dev` to run the nextjs frontend
- Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

In a separate terminal, do this:
- `cd` into the `backend` folder. Now type `pip install -r requirements.txt` to install the python dependencies.
- Run `uvicorn main:app --reload` to run the fastapi server on port 8000 with hot reload on.


## Using Docker to run the app

**Using Docker Compose**

```bash
docker-compose up --build
```

**Pull the image from Docker Hub**

**Step #1**

```bash
docker pull sandramsc/leap-hackathon
```

**Step #2**
```bash
docker run -p 3000:3000 sandramsc/leap-hackathon
```


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
