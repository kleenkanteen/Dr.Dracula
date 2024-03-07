 "use client"

// import { UploadPDF } from "../components/uploadPDF";
import React from 'react';
// import logo from './logo.svg';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import NavBar from "../components/NavBar";
import Banner from "../components/Banner";
import Skills from "../components/Skills";
import Footer from "../components/Footer";

export default function HomePage() {
  return (
    <>
      <NavBar />
      <Banner />
      <Skills />
      <Footer />
    </>
  );
}
