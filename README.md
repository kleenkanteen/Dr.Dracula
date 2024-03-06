<!-- Designed for LEAP24 hackathon 03.2024-->
<div id="header" align="center">
  <img src="https://lablab.ai/_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Flablab-static-eu%2Fimages%2Fevents%2Fclsvwsh8m000x3b6rhvbmf7cf%2Fundefined_imageLink_xbaa800rg.jpg&w=1080&q=75" width="1050" height="400"/>
</div>
  <h1 align="center">Dr. Dracula</h1>
   <h3 align="center">Simplifying blood test analysis</h3>

## Application Description

APP DESCRIPTION

## Table of Contents

<details>
<summary>Dr. Dracula</summary>

- [Application Description](#application-description)
- [Table of Contents](#table-of-contents)
- [Demo](#demo)
- [Screenshots](#screenshots)
- [Technology Stack](#technology-stack)
- [Features](#features)
- [How to use the app locally](#how-to-use-the-app)
- [Using Docker to run the app](#using-docker-to-run-the-app)
- [Authors](#authors)
- [License](#license)

</details>
 
## Demo

[View Demo Video](https://link.com)

## Screenshots


## Technology Stack

| Technology                                                    | Description                                                          |
| ------------------------------------------------------------- | -------------------------------------------------------------------- |
| Python                                                      | a high-level, general-purpose programming language  |
| FastAPI                                                      | a modern web framework for building RESTful APIs in Python |
| Next.js                                                      | an open-source web development framework  |
| JavaScript                                                      | a programming language and core technology of the World Wide Web |
| shadcdn                                                      | a CLI for adding components to projects |
| OpenAI Python library                                                      | provides convenient access to the OpenAI REST API from any Python 3.7+ application |
| Fitz (PyMuPDF)                                                      | a high-performance Python library for data extraction, analysis, conversion & manipulation of PDF (and other) documents |
| BeautifulSoup4                                                      | a library that makes it easy to scrape information from web pages |
| stack name                                                      | stack descr. |


## Features

- Seamless PDF upload for blood test analysis.
- Automated biomarker extraction from uploaded PDFs.
- In-depth analysis, comparison with medical sources, and comprehensive report generation.

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


## License

[![GitLicense](https://img.shields.io/badge/License-MIT-lime.svg)](https://github.com/sandramsc/leap-hackathon/blob/master/LICENSE)
