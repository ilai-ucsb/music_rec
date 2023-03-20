import React from "react";
import NavBarApp from "../NavBarApp";
import "./utils/Page.css"

// Basic about page. Not really sure what to put here so feel free to change it.

export default function AboutIndexPage() {
    return (
        <div>
            <NavBarApp />
            <div className="App-header">
                <h1 className="about-title" aria-label="about-header"><u>About us</u></h1>
                <div className="general" aria-label="about-body">
                    This app was created by Aditya Sharma, Mauricio Muñoz Valtierra, Francisco Justin Leyva, Anmol Kapoor, Ian Lai, and Parsa Hafezi
                    for the class CS148 at UCSB.
                </div>
                <div className="general" aria-label="about-body-link">
                    Visit our
                    <a href="https://github.com/ucsb-cs148-w23/project-t09-musicrecommendation" style={{margin: "0px 0.5em"}}>github</a>
                    for more information
                </div>
                <h1 className="about-title" aria-label="disclaimer-header" style={{marginTop: "10px"}}><u>Disclaimer</u></h1>
                <div className="general" aria-label="disclaimer-body">
                    By connecting your spotify account you agree to allow the site to gain access to information such as your playlist or your history. <br/> <br/>
                    Also note that you would need to contact one of the developers in order to sign in with spotify. Sorry for the inconvenience and we hope to fix it in the future :)
                    <br/> <br/>
                    More information can be found here:
                </div>
                <div className="general" aria-label="disclaimer-body-link">
                    <a href="https://developer.spotify.com/documentation/web-api/">spotifyAPI</a>
                </div>
            </div>
        </div>
    )
}