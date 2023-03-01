import React from "react";
import { render, screen } from "@testing-library/react";
import NavBarApp from "../components/NavBarApp";

describe("test NavBar", () => {
    it("should render text correctly", () => {
        render(<NavBarApp />)
        const homeRoute = screen.getByText(/Home/);
        const aboutRoute = screen.getByText(/About/);
        const loginRoute = screen.getByText(/Login/); 
        expect(homeRoute).toBeInTheDocument();
        expect(aboutRoute).toBeInTheDocument();
        expect(loginRoute).toBeInTheDocument();
        expect(homeRoute).toHaveAttribute("href", "/");
        expect(aboutRoute).toHaveAttribute("href", "/about");
        expect(loginRoute).toHaveAttribute("href", "/login");
        expect(screen.getByText("Music Recommendation App")).toBeInTheDocument();
        expect(screen.getByText("Music Recommendation App")).toHaveAttribute("href", "/");
    })
})