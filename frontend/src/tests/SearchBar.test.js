import React from "react";
import { render, fireEvent, cleanup, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
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

    it('should return a result on enter', () => {
        const { input } = setup()
        expect(input.value).toBe("")
        fireEvent.change(input, { target: {value: "gangnam style"}})
        expect(input.value).toBe("gangnam style")
        fireEvent.submit(screen.getByTestId("searchBar"))
        const element = screen.getByTestId("resultList")
        expect(element).toBeInTheDocument();
    })

    //setup searchbar with prop like <SearchBar setSearchResult={setSearchResult}/>
    // submit form twice and check that setSearchResult is not the same twice
})
