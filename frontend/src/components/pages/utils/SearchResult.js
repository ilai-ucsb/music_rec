// Each song will be displayed in this format


//MUI boxes, put the buttons in their own boxes, throw em on other sides of the boxes.
import * as React from "react";
import { useTheme } from "@mui/material/styles";
import Box from "@mui/material/Box";
import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";
import CardMedia from "@mui/material/CardMedia";
import IconButton from "@mui/material/IconButton";
import Typography from "@mui/material/Typography";
import { Spotify } from "react-bootstrap-icons";
import Button from "react-bootstrap/Button";
import { PlayFill } from "react-bootstrap-icons";
const SearchResult = ({ songName, artist, song_id }) => {
  const theme = useTheme();

  return (
    <article>
      <Box sx={{display: "inline-flex", alignSelf: 'flex-end'}}>
      <Card sx={{ display: "flex" }}>
        <Box sx={{ display: "flex", flexDirection: "column" }}>
          <CardContent sx={{ flex: "1 0 auto" }}>
            <Typography component="div" variant="h6">
              {songName}
            </Typography>
            <Typography
              variant="subtitle1"
              color="text.secondary"
              component="div"
            >
              {artist}{" "}
            </Typography>
          </CardContent>
          
          <Box sx={{ display: "flex",flexDirection:"column", alignItems: "center", pl: 1, pb: 1 }}>
            <Button>
              <PlayFill></PlayFill>
            </Button>

            <Button
              href={"https://open.spotify.com/track/" + song_id}
              size="sm"
              variant="success"
              ms="auto"
            >
              <Spotify />
            </Button>
          </Box>
        </Box>
        <CardMedia
          component="img"
          sx={{ width: 151 }}
          image="https://i.scdn.co/image/ab67616d0000b2736cfc57e5358c5e39e79bccbd"
        />
      </Card>
      </Box>
    </article>
  );
};
export default SearchResult;
