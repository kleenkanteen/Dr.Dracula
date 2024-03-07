"use client"

import React, { FC } from "react";
import Carousel from 'react-multi-carousel';
import 'react-multi-carousel/lib/styles.css';
import colorSharp from "../assets/img/color-sharp.png";

import { UploadPDF } from "../components/uploadPDF";

const Skills: FC = () => {
  const responsive = {
    superLargeDesktop: {
      breakpoint: { max: 4000, min: 3000 },
      items: 5
    },
    desktop: {
      breakpoint: { max: 3000, min: 1024 },
      items: 3
    },
    tablet: {
      breakpoint: { max: 1024, min: 464 },
      items: 2
    },
    mobile: {
      breakpoint: { max: 464, min: 0 },
      items: 1
    }
  };

  return (
    <section className="skill" id="skills">
        <div className="container">
            <div className="row">
                <div className="col-12">
                    <div className="skill-bx wow zoomIn">
                        <h2>Upload Your Blood Test Results</h2>
                        <Carousel responsive={responsive} infinite={true} className="owl-carousel owl-theme skill-slider">
                            <div className="align-items-center">
                            <UploadPDF />
                            </div>
                        </Carousel>
                    </div>
                </div>
            </div>
        </div>
        {/* Access the URL of the image using the src property */}
        <img className="background-image-left" src={colorSharp.src} alt="Image" />
    </section>
  )
}

export default Skills;