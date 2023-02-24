import React from "react";
import { render, screen, fireEvent} from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import '@testing-library/jest-dom/extend-expect'
import HomeIndexPage from "../components/pages/HomeIndexPage"

describe("HomeIndexPage tests", () => {
    it("should display a search bar", () => {
        render(<HomeIndexPage />)
        const element = screen.getByRole("searchbox")
        expect(element).toBeInTheDocument();
    })
    
    it("should contain list for results", () => {
        render(<HomeIndexPage/>)
        const element = screen.getByTestId("searchInput")
        element.focus()
        fireEvent.change(screen.getByTestId("searchInput"), { target: {value: "gangnam style"}})
        // userEvent.type("gangnam style")
        fireEvent.submit(screen.getByTestId("submitButton"))

        const element2 = screen.getByTestId("resultList")
        expect(element2).toBeInTheDocument();
    })
})