import React from "react";
import { render, screen, fireEvent, waitFor} from "@testing-library/react";
import '@testing-library/jest-dom/extend-expect'
import userEvent from '@testing-library/user-event';
import App from "../App"
import { Simulate } from "react-dom/test-utils";

describe("App integration test", () => {
    it("should render songs when a song is inputted", async () => {
        render(<App />)
        const input = screen.getByTestId("searchInput")
        const filterBtn = screen.getByRole("button", {name: "filters"})
        
        fireEvent.click(filterBtn)
        userEvent.selectOptions(screen.getByTestId("explicit-select"), "1")
        expect(screen.getByTestId('minValue')).toBeInTheDocument();
        expect(screen.getByTestId('maxValue')).toBeInTheDocument();

        userEvent.selectOptions(screen.getByTestId("explicit-select"), "1")
        userEvent.selectOptions(screen.getByTestId("loud-select"), "0.5")

        fireEvent.click(screen.getByRole("button", {name: "close"}))
        
        fireEvent.change(input, {target: {value: "gangnam style"}})
        Simulate.submit(screen.getByRole("searchbox"))
        setTimeout(async () => await waitFor(() => expect(screen.queryByTestId("songElements")).toBeInTheDocument()), 5000);
    })

    it("should render another set of songs with same input", async () => {
        render(<App/>)
        // Enter initial search input
        const input = screen.getByTestId("searchInput")
        fireEvent.change(input, {target: {value: "gangnam style"}})

        // Submit search and expect results
        Simulate.submit(screen.getByRole("searchbox"))
        setTimeout(async () => await waitFor(() => expect(screen.queryByTestId("songElements")).toBeInTheDocument()), 5000);

        // Search value should not have changed
        expect(input.value).toBe("gangnam style")

        // Resubmit same input for different results
        setTimeout(async () => await waitFor(() => expect(screen.queryByTestId("songElements")).toBeInTheDocument()), 5000);
    })
})