import React from "react";
import { Text, Linking } from 'react-native';
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
                    Visit our <Text classname="general" style={{ color: "red", fontSize: "18px" }} onPress={() => { Linking.openURL('https://github.com/ucsb-cs148-w23/project-t09-musicrecommendation'); }}> github </Text>
                    for more information
                </div>
                <h1 className="about-title" aria-label="disclaimer-header"><u>Disclaimer</u></h1>
                <div className="general" aria-label="disclaimer-body">
                    By connecting your spotify account you agree to allow the site to gain access to information such as your playlist or your history.
                    More information can be found here:
                </div>
                <div className="general" aria-label="disclaimer-body-link">
                    <Text classname="general" style={{ color: "red", fontSize: "18px" }} onPress={() => { Linking.openURL('https://developer.spotify.com/documentation/web-api/'); }}> spotifyAPI </Text>
                </div>
            </div>
        </div>
    )
}