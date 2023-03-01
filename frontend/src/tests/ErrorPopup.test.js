// Mocks a failed api request and checks if the error text is displayed on screen
import React from 'react';
import { render, fireEvent, screen, waitFor } from '@testing-library/react';
import SearchBar from '../components/SearchBar';
describe('Error popup component', () => {
  test('renders error popup when API call fails', async () => {
    const setSearchResult = jest.fn();
    global.fetch = jest.fn(() =>
      Promise.resolve({
        json: () => Promise.reject('Error: API request failed'),
      })
    );

    render(<SearchBar setSearchResult={setSearchResult} />);
    const searchInput = screen.getByTestId('searchInput');
    const searchBar = screen.getByTestId('searchBar');
    fireEvent.change(searchInput, { target: { value: 'Nonexistent Song' } });
    fireEvent.submit(searchBar);

    await waitFor(() =>
      expect(screen.getByText('Sorry, we could not find that song')).toBeInTheDocument()
    );
  });
});
