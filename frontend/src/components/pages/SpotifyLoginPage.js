import React from "react";
import { Text, Linking } from 'react-native';
import NavBarApp from "../NavBarApp";
import "./utils/Page.css"

export default function SpotifyLoginPage() {
    return (
        <div>
            <NavBarApp />
            <div className="App-header">
                <h1 className="about-title" aria-label="about-header"><u>Log into your Spotify Account</u></h1>
                <div className="general" aria-label="about-body">
                    Login form here
                </div>
            </div>
        </div>
    )
}