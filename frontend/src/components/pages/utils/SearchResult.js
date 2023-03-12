// Each song will be displayed in this format

//MUI boxes, put the buttons in their own boxes, throw em on other sides of the boxes.
import * as React from "react";
import { styled } from "@mui/material/styles";

import Box from "@mui/material/Box";
import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";
import CardMedia from "@mui/material/CardMedia";
import CardActions from "@mui/material/CardActions";
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

  const handleExpandClick = () => {
    setExpanded(!expanded);
  };
  return (
    <article>
      <Box sx={{ display: "inline-flex", alignSelf: "flex-end" }}>
        <Card sx={{ display: "flex" }}>
          <Box sx={{ display: "flex", flexDirection: "column", width: "400px" }}>
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
                pl: 1,
                pb: 1,
              }}
            >
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
              <Typography paragraph>
                The stats go here
              </Typography>
            </CardContent>
          </Collapse>
        </Card>
      </Box>
    </article>
  );
};
export default SearchResult;
