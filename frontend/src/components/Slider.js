import React, { useState }from 'react'
import { Slider, Box } from '@mui/material';
import "./pages/utils/Page.css"

function valuetext(value) {
  return `${value}°C`;
}

const minDistance = 5;

function SliderComp() {
  const [value, setValue] = useState([1950, 2022]);

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

  // const handleMinValue = (newValue) => {
  //   setValue([newValue, value[1]]);
  //   newValue = value[0];
  // }

  return (
    <Box sx={{ width: 300 }}>
      <input data-testid="minYear" type="text" readOnly={true} style={{width: "30%", maxHeight: "30px"}} value={value[0]} onChange={(e) => e.target.value = value[0]}/>
      - &nbsp;
      <input type="text" readOnly={true} style={{width: "30%", maxHeight: "30px"}} value={value[1]} onChange={(e) => e.target.value = value[1]}/>
      <Slider
        data-testid="changeYear"
        getAriaLabel={() => 'Minimum distance shift'}
        value={value}
        onChange={handleChange}
        min={1950}
        max={2022}
        valueLabelDisplay="auto"
        getAriaValueText={valuetext}
        disableSwap
      />
    </Box>
  );
}

export default SliderComp
