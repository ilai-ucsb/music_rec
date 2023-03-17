import * as React from "react";
import { styled } from "@mui/material/styles";

import Box from "@mui/material/Box";
import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";
import CardMedia from "@mui/material/CardMedia";
import Collapse from "@mui/material/Collapse";
import Typography from "@mui/material/Typography";
import { IconButton } from "@mui/material";
import { PlayFill, Spotify, InfoCircle } from "react-bootstrap-icons";
import ReactHowler from 'react-howler';

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

const SearchResult = ({ songName, artist, song_id, popularity, year, danceability, acousticness, energy, album_cover, preview_url }) => {
  const [expanded, setExpanded] = React.useState(false);


  const handleExpandClick = () => {
    setExpanded(!expanded);
  };
  const handlePlayClick = () => {
    <ReactHowler src={preview_url}
    playing={true}/>
    console.log(preview_url)

  };
  return (
    
    <article>
      <Box sx={{ display: "inline-flex", alignSelf: "flex-end", padding: 2 }}>
        <Card sx={{ display: "flex" }}>
        <CardMedia
            component="img"
            sx={{ width: 165}}
            image={album_cover}
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
                {artist}{"\n"}
              </Typography>
              <Typography
                variant="subtitle1"
                color="text.secondary"
                component="div"
              >
                {year}{" "}
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
               
              <IconButton sx={{ width: "7%" }} onClick={handlePlayClick}>
               <PlayFill />
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
                <Typography paragraph>danceability {danceability}</Typography>
                <Typography paragraph>energy: {energy}</Typography>
                <Typography paragraph>popularity: {popularity} </Typography>
              </CardContent>
            </Collapse>



            
          </Box>


        </Card>
      </Box>
    </article>
  );
};
export default SearchResult;
