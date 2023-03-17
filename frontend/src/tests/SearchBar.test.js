import React from "react";
import { render, fireEvent, screen } from "@testing-library/react";
import SearchBar from "../components/SearchBar";
import '@testing-library/jest-dom/extend-expect'
// import HomeIndexPage from "../components/pages/HomeIndexPage";

describe("SearchBar component", () => {
    const setup = () => {
        const utils = render(<SearchBar />)
        const input = utils.getByTestId("searchInput")
        return {
            input,
            ...utils,
        }
    }

    it('checking that the input is changed', () => {
        const { input } = setup()
        expect(input.value).toBe("")
        fireEvent.change(input, { target: {value: "hello"}})
        expect(input.value).toBe("hello"); 
    })

    it("should display the suggestions when a user inputs something", async () => {
        const { input } = setup();
        fireEvent.change(input, { target: { value: "gangnam style" }});
        expect(await screen.getByTestId("suggestions")).toBeInTheDocument();
    })
})
