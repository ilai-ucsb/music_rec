import React from "react";
import { Linking } from "react-native";
import { render, screen, fireEvent } from "@testing-library/react";
import AboutIndexPage from "../components/pages/AboutIndexPage";

jest.mock("react-native/Libraries/Linking/Linking", () => ({
    openURL: jest.fn(() => Promise.resolve("mockResolve")),
}))

describe("test about page", () => {
    it("should have the necessary headers and body", () => {
        render(<AboutIndexPage />)
        expect(screen.getByLabelText("about-header")).toBeInTheDocument();
        expect(screen.getByLabelText("about-body")).toBeInTheDocument();
        expect(screen.getByLabelText("about-body-link")).toBeInTheDocument();
        expect(screen.getByLabelText("disclaimer-header")).toBeInTheDocument();
        expect(screen.getByLabelText("disclaimer-body")).toBeInTheDocument();
        expect(screen.getByLabelText("disclaimer-body-link")).toBeInTheDocument();
    })
})