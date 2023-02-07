import React from "react";
import { render, screen } from "@testing-library/react";
import HomeIndexPage from "../components/pages/HomeIndexPage";

describe("HomeIndexPage component", () => {
    it("should render the searchBox in HomeIndexPage correctly", () => {
        render(<HomeIndexPage />)
        const element = screen.getByRole("searchbox");
        expect(element).toBeInTheDocument();
    })
})