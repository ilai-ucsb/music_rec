import React from "react";
import { render, screen, fireEvent, getByLabelText, getByTestId } from "@testing-library/react";
import '@testing-library/jest-dom/extend-expect'
import HomeIndexPage from "../components/pages/HomeIndexPage"
import SearchBar from "../components/SearchBar";

describe("HomeIndexPage tests", () => {
    const setup = () => {
        const utils = render(<SearchBar />)
        const input = utils.getByLabelText("search-bar")
        return {
            input,
            ...utils,
        }
    }
    it("should display a search bar", () => {
        render(<HomeIndexPage />)
        const element = screen.getByRole("searchbox")
        expect(element).toBeInTheDocument();
    })
    it("should display result on submit", () => {
        const { input } = setup()
        fireEvent.change(input, { target: { value: "joji" } })
        fireEvent.submit(getByTestId('form'))
    })
})