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
    it("should display the filter popup when clicked", () => {
        render(<HomeIndexPage/>)
        const filterBtn = screen.getByRole("button", {name: "filters"});
        expect(filterBtn).toBeInTheDocument();
        fireEvent.click(filterBtn);
        const closeBtn = screen.getByRole("button", {name: "close"});
        const filterText = screen.getByText("explicit:")
        expect(closeBtn).toBeInTheDocument();
        expect(filterText).toBeInTheDocument();
    })
    it("should change values when a different option is selected", () => {
        render(<HomeIndexPage/>)
        const filterBtn = screen.getByRole("button", {name: "filters"});
        fireEvent.click(filterBtn);
        userEvent.selectOptions(screen.getByTestId('select'), "1")
        expect(screen.getByTestId("select").value).toBe("1")
    })
    it("should not display the filter popup when the close button is clicked", () => {
        render(<HomeIndexPage/>)
        fireEvent.click(screen.getByRole("button", {name: "filters"}));
        fireEvent.click(screen.getByRole("button", {name: "close"}));
        expect(screen.queryByText("explicit:")).not.toBeInTheDocument();
    })
})