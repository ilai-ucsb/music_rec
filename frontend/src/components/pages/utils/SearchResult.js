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

const SearchResult = ({
  ...props
}) => {
  const [expanded, setExpanded] = React.useState(false);
  const [similarName1, setSimilarName1] = React.useState("");
  const [similarUrl1, setSimilarUrl1] = React.useState("");
  const [similarName2, setSimilarName2] = React.useState("");
  const [similarUrl2, setSimilarUrl2] = React.useState("");

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

      await fetch('https://i2w798wse2.execute-api.us-east-1.amazonaws.com/similar', songParameters).then(resp => resp.json()
      ).then(data => {
        if (data["similar_songs"].length >= 2) {
          setSimilarName1(data["similar_songs"][0]["name"]);
          setSimilarUrl1("https://open.spotify.com/track/" + data["similar_songs"][0]["id"]);
          setSimilarName2(data["similar_songs"][1]["name"]);
          setSimilarUrl2("https://open.spotify.com/track/" + data["similar_songs"][1]["id"]);
        }
      });
      // let resJson = response.json().["similar_songs"];

      // similar_name = resJson[0]["name"];
      // similar_url = "https://open.spotify.com/track/" + resJson[0]["id"];

    }
    setExpanded(!expanded);
  };
  const handlePlayClick = () => {
    <ReactHowler src={props.preview_url}
    playing={true}/>
    console.log(props.preview_url)

  };
  return (
    
    <article>
      <Box sx={{ display: "inline-flex", alignSelf: "flex-end", padding: 2 }}>
        <Card sx={{ display: "flex" }}>
        <CardMedia
            component="img"
            sx={{ width: 165}}
            image={props.album_cover}
          />
          <Box
            sx={{ display: "flex", flexDirection: "column", width: "600px" }}
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
                {props.year}{" "}
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
                href={"https://open.spotify.com/track/" + props.song_id}
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
                <Typography variant="h5"><b>STATS</b></Typography>
                <Typography paragraph><b>Danceability</b> {props.danceability}</Typography>
                <Typography paragraph><b>Energy</b> {props.energy}</Typography>
                <Typography paragraph><b>Popularity</b> {props.popularity} </Typography>
                {
                  similarName1 !== "" &&
                  <Typography paragraph><b>You may also like:</b> <a href={similarUrl1}>{similarName1}</a> and <a href={similarUrl2}>{similarName2}</a> </Typography>
                }
              </CardContent>
            </Collapse>



            
          </Box>


        </Card>
      </Box>
    </article>
  );
};
export default SearchResult;
