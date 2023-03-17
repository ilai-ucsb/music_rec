import React from 'react'
import { Slider, Box, TextField } from '@mui/material';
import "./pages/utils/Page.css"

function valuetext(value) {
  return `${value}°C`;
}

const minDistance = 1;

function SliderComp({value, setValue}) {

  const handleChange = (event, newValue, activeThumb) => {
    if (!Array.isArray(newValue)) {
      return;
    }

    if (newValue[1] - newValue[0] < minDistance) {
      if (activeThumb === 0) {
        const clamped = Math.min(newValue[0], 2022 - minDistance);
        setValue([clamped, clamped + minDistance]);
      } else {
        const clamped = Math.max(newValue[1], minDistance);
        setValue([clamped - minDistance, clamped]);
      }
    } else {
      setValue(newValue);
    }
  };

  return (
    <div>
      <TextField data-testid="minValue" inputProps={{style: { padding: 5, width: 50}, readOnly: true}} value={value[0]}/>
      &nbsp;-&nbsp;
      <TextField data-testid="maxValue" inputProps={{style: { padding: 5, width: 50}, readOnly: true}} value={value[1]}/>
      <Box sx={{ width: 200 }}>
        <Slider
          getAriaLabel={() => 'slider'}
          value={value}
          onChange={handleChange}
          min={1920}
          max={2022}
          valueLabelDisplay="auto"
          getAriaValueText={valuetext}
          disableSwap
        />
      </Box>
    </div>
  );
}

export default SliderComp
