import React from "react";
import { render, fireEvent } from "@testing-library/react";

describe("test slider", () => {
    it("should call useState", () => {
        const setStateMock = jest.fn();
        const useStateMock = (useState) => [useState, setStateMock];
        jest.spyOn(React, 'useState').mockImplementation(useStateMock);
        
    })
})