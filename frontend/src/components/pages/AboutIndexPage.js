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
              <h1 className="about-title"><u>About us</u></h1>
              <p className="general">
                  This app was created by Aditya Sharma, Mauricio Muñoz Valtierra, Francisco Justin Leyva, Anmol Kapoor, Ian Lai, and Parsa Hafezi
                  for the class CS148 at UCSB.
              </p>
              <p className="general">
                  Visit our <Text classname="general" style={{ color: "red", fontSize: "18px" }} onPress={() => { Linking.openURL('https://github.com/ucsb-cs148-w23/project-t09-musicrecommendation'); }}> github </Text>
                  for more information
              </p>
              <h1 className="about-title"><u>Disclaimer</u></h1>
              <p className="general">
                  By connecting your spotify account you agree to allow the site to gain access to information such as your playlist or your history.
                  More information can be found here:
              </p>
              <p className="general">
                  <Text classname="general" style={{ color: "red", fontSize: "18px" }} onPress={() => { Linking.openURL('https://developer.spotify.com/documentation/web-api/'); }}> spotifyAPI </Text>
              </p>
          </div>
      </div>
  )
}