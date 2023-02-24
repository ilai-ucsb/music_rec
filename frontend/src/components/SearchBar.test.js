import { render, screen } from '@testing-library/react';
import App from '../App.js'

test('renders search bar', () => {
  render(<App />);
  const searchElement = screen.getByTestId("searchBar")
  expect(searchElement).toBeInTheDocument();
});
