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
        userEvent.selectOptions(screen.getByTestId("select"), "1")
        fireEvent.click(screen.getByRole("button", {name: "close"}))
        fireEvent.change(input, {target: {value: "gangnam style"}})
        Simulate.submit(screen.getByRole("searchbox"))
        setTimeout(async () => await waitFor(() => expect(screen.queryByTestId("songElements")).toBeInTheDocument()), 5000);
    })
})