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
  const [similarName1, setSimilarName1] = React.useState("");
  const [similarUrl1, setSimilarUrl1] = React.useState("");
  const [similarName2, setSimilarName2] = React.useState("");
  const [similarUrl2, setSimilarUrl2] = React.useState("");
  const [play, setPlay] = useState(false);
  let src = props.preview_url;
  const audioRef = useRef(null);

  const handleExpandClick = async (e) => {
    e.preventDefault();

    if (!expanded) {
      let songParameters = {
        method: 'POST',
        mode: 'cors',
        headers: {
          "Content-Type": 'application/json'
        },
        body: JSON.stringify({
          "popularity": parseInt(props.popularity),
          "year": props.year,
          "danceability": parseFloat(props.danceability),
          "acousticness": parseFloat(props.acousticness),
          "explicit": parseInt(props.explicit),
          "energy": parseFloat(props.energy),
          "instrumentalness": parseFloat(props.instrumentalness),
          "liveness": parseFloat(props.liveness),
          "loudness": parseFloat(props.loudness),
          "speechiness": parseFloat(props.speechiness),
          "tempo": parseFloat(props.tempo),
        })
      };

      await fetch('https://nc5fwwvfbc.execute-api.us-east-1.amazonaws.com/dev/similar', songParameters).then(resp => resp.json()
      ).then(data => {
        if (data["similar_songs"].length >= 2) {
          setSimilarName1(data["similar_songs"][0]["name"]);
          setSimilarUrl1("https://open.spotify.com/track/" + data["similar_songs"][0]["id"]);
          setSimilarName2(data["similar_songs"][1]["name"]);
          setSimilarUrl2("https://open.spotify.com/track/" + data["similar_songs"][1]["id"]);
        }
      });
    }
    setExpanded(!expanded);
  };

  const handlePlay = () => {
    if (play) {
      audioRef.current.pause();
      setPlay(!play);
    } else {
      audioRef.current.load();
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
                <Typography variant="h5"><b>STATS</b></Typography>
                <Typography paragraph><b>Danceability</b> {props.danceability}</Typography>
                <Typography paragraph><b>Energy</b> {props.energy}</Typography>
                {
                  similarName1 !== "" &&
                  <span style={{ fontSize: '15px' }}><b>You may also like:</b> <ul><li>{similarName1}
                  <IconButton
                  href={similarUrl1}
                  ms="auto"
                  target="_blank"
                  sx={{ height: "40%" }}
                >
                  <Spotify />
                </IconButton></li><li>{similarName2}
                  <IconButton
                  href={similarUrl2}
                  ms="auto"
                  target="_blank"
                  sx={{ height: "40%" }}
                >
                  <Spotify />
                </IconButton></li></ul></span>
                }
              </CardContent>
            </Collapse>
          </Box>
        </Card>
      </Box>
  );
};
export default SearchResult;
