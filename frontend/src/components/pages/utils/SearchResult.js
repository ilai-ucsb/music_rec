// Each song will be displayed in this format

// Centered the material ui boxes. used the colorthief package to update the background of the cards based on the image
//   img.src = imageUrl [imageUrl]); image={imageUrl}
import * as React from "react";
import { styled } from "@mui/material/styles";
import ColorThief from "colorthief";

import Box from "@mui/material/Box";
import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";
import CardMedia from "@mui/material/CardMedia";
import Collapse from "@mui/material/Collapse";
import Typography from "@mui/material/Typography";
import { Spotify } from "react-bootstrap-icons";
import Button from "react-bootstrap/Button";
import { PlayFill } from "react-bootstrap-icons";

const ExpandMore = styled((props) => {
  const { expand, ...other } = props;
  return <PlayFill {...other} />;
})(({ theme, expand }) => ({
  transform: !expand ? "rotate(0deg)" : "rotate(180deg)",
  marginLeft: "auto",
  transition: theme.transitions.create("transform", {
    duration: theme.transitions.duration.shortest,
  }),
}));

const SearchResult = ({ songName, artist, song_id }) => {
  const [expanded, setExpanded] = React.useState(false);
  const [bgColor, setBgColor] = React.useState("#ffffff");

  React.useEffect(() => {
    const colorThief = new ColorThief();
    const img = new Image();
    img.crossOrigin = "anonymous";
    img.addEventListener("load", () => {
      const color = colorThief.getColor(img);
      setBgColor(`rgb(${color.join(", ")})`);
    });
    img.src =
      "https://i.scdn.co/image/ab67616d0000b2736cfc57e5358c5e39e79bccbd";
  }, ["https://i.scdn.co/image/ab67616d0000b2736cfc57e5358c5e39e79bccbd"]);

  const handleExpandClick = () => {
    setExpanded(!expanded);
  };

  return (
    <article>
      <Box sx={{ display: "inline-flex", alignSelf: "flex-end" }}>
        <Card sx={{ display: "flex", backgroundColor: bgColor }}>
          <Box
            sx={{ display: "flex", flexDirection: "column", width: "400px" }}
          >
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

            <Box
              sx={{
                display: "flex",
                flexDirection: "column",
                alignItems: "center",
                justifyContent: "center",
                pl: 1,
                pb: 1,
                width: "100%",
              }}
            >
              <Button sx={{ width: "50%" }}>
                <PlayFill></PlayFill>
              </Button>

              <Button
                href={"https://open.spotify.com/track/" + song_id}
                ms="auto"
                target="_blank"
                sx={{ width: "50%" }}
                style={{ backgroundColor: "#1DB954" }}
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

          <ExpandMore
            expand={expanded}
            onClick={handleExpandClick}
            aria-expanded={expanded}
            aria-label="show more"
          >
            <PlayFill></PlayFill>
          </ExpandMore>
          <Collapse in={expanded} timeout="auto" unmountOnExit>
            <CardContent>
              <Typography paragraph>Stats:</Typography>
              <Typography paragraph>The stats go here</Typography>
            </CardContent>
          </Collapse>
        </Card>
      </Box>
    </article>
  );
};
export default SearchResult;
