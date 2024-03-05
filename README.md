<!-- Designed for LEAP24 hackathon 03.2024-->
<div id="header" align="center">
  <img src="https://lablab.ai/_next/image?url=https%3A%2F%2Fstorage.googleapis.com%2Flablab-static-eu%2Fimages%2Fevents%2Fclsvwsh8m000x3b6rhvbmf7cf%2Fundefined_imageLink_xbaa800rg.jpg&w=1080&q=75" width="1050" height="400"/>
</div>
  <h1 align="center">APP NAME</h1>

## Application Description

APP DESCRIPTION

## Table of Contents

<details>
<summary>APP NAME</summary>

- [Application Description](#application-description)
- [Table of Contents](#table-of-contents)
- [Demo](#demo)
- [Prototype](#prototype)
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

## Prototype

[View Prototype](https://link.com)

## Screenshots


## Technology Stack

| Technology                                                    | Description                                                          |
| ------------------------------------------------------------- | -------------------------------------------------------------------- |
| TypeScript                                                      | TypeScript is a free and open source programming language developed and maintained by Microsoft. |



## Features

- FEATURE 1
- FEATURE 1
- FEATURE 1

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