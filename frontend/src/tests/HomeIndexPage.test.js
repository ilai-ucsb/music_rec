import React from "react";
import { render, screen, fireEvent, waitFor } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import '@testing-library/jest-dom/extend-expect'
import HomeIndexPage from "../components/pages/HomeIndexPage"

describe("HomeIndexPage tests", () => {
    it("should display a search bar", () => {
        render(<HomeIndexPage />)
        const element = screen.getByRole("searchbox")
        expect(element).toBeInTheDocument();
    })
    it("should display the filter popup when clicked", async () => {
        render(<HomeIndexPage/>)
        const filterBtn = await waitFor(() => screen.getByRole("button", {name: "filters"}));
        expect(filterBtn).toBeInTheDocument();
        fireEvent.click(filterBtn);
        const closeBtn = await waitFor(() => screen.getByRole("button", {name: "close"}));
        const filterText = await waitFor(() => screen.getByText("explicit: loud:"));
        
        expect(closeBtn).toBeInTheDocument();
        expect(filterText).toBeInTheDocument();
    })
    it("should change explicit filter values when a different option is selected", async () => {
        render(<HomeIndexPage/>)
        const filterBtn = screen.getByRole("button", {name: "filters"});
        fireEvent.click(filterBtn);
        await waitFor(() => userEvent.selectOptions(screen.getByTestId('explicit-select'), "1"));
        expect(screen.getByTestId("explicit-select").value).toBe("1")
    })

    it("should change loud values when a different option is selected", async () => {
        render(<HomeIndexPage/>)
        const filterBtn = screen.getByRole("button", {name: "filters"});
        fireEvent.click(filterBtn);
        await waitFor(() => userEvent.selectOptions(screen.getByTestId('loud-select'), "0.5"));
        expect(screen.getByTestId("loud-select").value).toBe("0.5")
    })

    it("should not display the filter popup when the close button is clicked", async () => {
        render(<HomeIndexPage/>)
        await waitFor(() => fireEvent.click(screen.getByRole("button", {name: "filters"})));
        await waitFor(() => fireEvent.click(screen.getByRole("button", {name: "close"})));
        expect(screen.queryByText("explicit:")).not.toBeInTheDocument();
    })
})