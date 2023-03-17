import React, { useState, useRef } from "react";
import { styled } from "@mui/material/styles";
import Box from "@mui/material/Box";
import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";
import CardMedia from "@mui/material/CardMedia";
import Collapse from "@mui/material/Collapse";
import Typography from "@mui/material/Typography";
import ExpandMoreIcon from "@mui/icons-material/ExpandMore";
import { IconButton } from "@mui/material";
import { PlayFill, Spotify, PauseBtn } from "react-bootstrap-icons";
import Rating from "@mui/material/Rating";


const ExpandMore = styled((props) => {
  const { expand, ...other } = props;
  return <IconButton {...other} />;
})(({ theme, expand }) => ({
  transform: !expand ? "rotate(0deg)" : "rotate(180deg)",
  marginLeft: "auto",
  transition: theme.transitions.create("transform", {
    duration: theme.transitions.duration.shortest,
  }),
}));

const SearchResult = ({ ...props }) => {
  const [expanded, setExpanded] = useState(false);
  const [play, setPlay] = useState(false);
  let src = props.preview_url;
  const audioRef = useRef(null);


  const handleExpandClick = () => {
    setExpanded(!expanded);
  };

  const handlePlay = () => {
    if (play) {
      audioRef.current.pause();
      setPlay(!play);
    } else {
      audioRef.current.play();
      setPlay(!play);
    }
  }

  return (
      <Box sx={{ display: "inline-flex", alignSelf: "flex-end", 
                 padding: 2, width: "100%", 
                 "& .MuiPaper-root": {width: "60%", position: "relative", left: "20%"},
                 "& .MuiBox-root": {width: "100%"}
              }}>
        <Card sx={{ display: "flex", width: "auto",}}>
        <CardMedia
            component="img"
            sx={{ width: "30%"}}
            image={props.album_cover}
          />
          <Box
            sx={{ display: "flex", flexDirection: "column"}}
          >
            <CardContent sx={{ flex: "1 0 auto" }}>
              
              <Typography component="div" variant="h6">
                {props.songName}
              </Typography>
              <Typography
                variant="subtitle1"
                color="text.secondary"
                component="div"
              >
                {props.artist}{"\n"}
              </Typography>
              <Typography
                variant="subtitle1"
                color="text.secondary"
                component="div"
              >
                {props.year}{" "}<br/>
                <Rating name="popularity" value={props.popularity/20} precision={0.5} readOnly/>
              </Typography>
            </CardContent>

            <Box
              sx={{
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
                pl: 1,
                pb: 1,
                width: "100px",
                "& .MuiIconButton-root": {fontSize: "24px", justifyContent: "center"},
              }}
            >
               
              <IconButton onClick={handlePlay}>
                <audio ref={audioRef}>
                  <source src={src} type="audio/mpeg"/>
                </audio>
                {play ? <PauseBtn/> : <PlayFill/> }
              </IconButton>
             
              <IconButton
                href={"https://open.spotify.com/track/" + props.song_id}
                ms="auto"
                target="_blank"
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
              <ExpandMoreIcon/>
            </ExpandMore>
            <Collapse
              in={expanded}
              timeout="auto"
              unmountOnExit
              orientation="vertical"
            >
              <CardContent>
                <Typography paragraph>Stats:</Typography>
                <Typography paragraph>danceability {props.danceability}</Typography>
                <Typography paragraph>energy: {props.energy}</Typography>
              </CardContent>
            </Collapse>



            
          </Box>


        </Card>
      </Box>
  );
};
export default SearchResult;
