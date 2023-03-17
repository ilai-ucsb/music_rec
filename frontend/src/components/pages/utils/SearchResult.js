import * as React from "react";
import { styled } from "@mui/material/styles";

import Box from "@mui/material/Box";
import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";
import CardMedia from "@mui/material/CardMedia";
import Collapse from "@mui/material/Collapse";
import Typography from "@mui/material/Typography";
import { Spotify } from "react-bootstrap-icons";
import { IconButton } from "@mui/material";
import { PlayFill, PauseFill, InfoCircle } from "react-bootstrap-icons";
import Sound from 'react-sound';
const ExpandMore = styled((props) => {
  const { expand, ...other } = props;
  return <InfoCircle {...other} />;
})(({ theme, expand }) => ({
  transform: !expand ? "rotate(0deg)" : "rotate(180deg)",
  marginLeft: "auto",
  transition: theme.transitions.create("transform", {
    duration: theme.transitions.duration.shortest,
  }),
}));

const SearchResult = ({ songName, artist, song_id, preview_url }) => {
  const [expanded, setExpanded] = React.useState(false);
  const [playStatus, setPlayStatus] = React.useState(Sound.status.STOPPED);


  const handleExpandClick = () => {
    setExpanded(!expanded);
  };

  const handlePlayClick = () => {
    setPlayStatus(Sound.status.PLAYING);
    
  };

  const handlePauseClick = () => {
    setPlayStatus(Sound.status.PAUSED);
  };
  return (
    
    <article>
      <Box sx={{ display: "inline-flex", alignSelf: "flex-end", padding: 2 }}>
        <Card sx={{ display: "flex" }}>
        <CardMedia
            component="img"
            sx={{ width: 165, height: 165 }}
            image="https://i.scdn.co/image/ab67616d0000b2736cfc57e5358c5e39e79bccbd"
          />
          <Box
            sx={{ display: "flex", flexDirection: "column", width: "600px" }}
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
                alignItems: "center",
                justifyContent: "center",
                pl: 1,
                pb: 1,
                width: "100%",
              }}
            >
               
              <IconButton sx={{ width: "7%" }}       onClick={playStatus === Sound.status.PLAYING ? handlePauseClick : handlePlayClick}
                aria-label={playStatus === Sound.status.PLAYING ? "Pause" : "Play"}
              >
                {playStatus === Sound.status.PLAYING ? <PauseFill /> : <PlayFill />}
              </IconButton>
             
              <IconButton
                href={"https://open.spotify.com/track/" + song_id}
                ms="auto"
                target="_blank"
                sx={{ width: "7%" }}
              >
                <Spotify />
              </IconButton>
            </Box>
{/* 
what follows is the expanded function
Change what's inside of Card content to change what's shown on expansion
*/}

    
            <ExpandMore
              expand={expanded}
              onClick={handleExpandClick}
              aria-expanded={expanded}
              aria-label="show more"
            >
            </ExpandMore>
            <Collapse
              in={expanded}
              timeout="auto"
              unmountOnExit
              orientation="vertical"
            >
              <CardContent>
                <Typography paragraph>Stats:</Typography>
                <Typography paragraph>danceability</Typography>
                <Typography paragraph>energy</Typography>
                <Typography paragraph>popularity </Typography>
              </CardContent>
            </Collapse>



            
          </Box>


        </Card>
      </Box>
    </article>
  );
};
export default SearchResult;
