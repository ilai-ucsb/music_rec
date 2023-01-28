# Spotify's Web API

**client ID** 059936209b6a44c08ee2b55ed2ce6e6a

**client secret** d3304a27fd884633a8a6b660afd17f79

1. [Introduction](#intro)
1. [How we can use it](#how-we-can-use-it)
1. [Sources](#sources) 

## Intro:
APIs are a way for us to use spotify's complex code to build our own software in a facilitated manner. I've gone ahead and [registered an app with spotify](https://developer.spotify.com/dashboard/applications/059936209b6a44c08ee2b55ed2ce6e6a).  We're using multiple [endpoints](https://developer.spotify.com/documentation/web-api/reference/#/operations/search) for our development. To use these endpoints we're going to use [Authorization Scopes](https://developer.spotify.com/documentation/general/guides/authorization/scopes/). 

## How we can use it: 
 Spotify's documentation includes exetremely in depth guides for developers such as ourselves. It includes guides on various aspects of web app development that we'll need such as [Authoritization](https://developer.spotify.com/documentation/general/guides/authorization/). Authorization seems to be our biggest concern in my opinoin. We need the user's authorization to use their data and we need to disclaim what data we'r'e going to be using. Luckily spotify wrote a documentation on [Authorization Scopes](https://developer.spotify.com/documentation/general/guides/authorization/scopes/). "Scopes provide Spotify users using third-party apps the confidence that only the information they choose to share will be shared, and nothing more." The majority of these we will not be using but ones I think we'll find the most useful include 
 1.   playlist-read-private
 1. user-follow-modify
 1. user-follow-read
 1. user-library-modify
 1. playlist-modify-private
1. playlist-modify-public
1. user-top-read
1. user-library-read

Spotify has as an immense amount of resources for us to read and use, most of which would be superfluous for our small scope but I think it's a good idea to include the ones I considered most useful on this file. For the hour I've spent researching the API I can see it'll be exetremly useful for our final product.

## Sources:

[Spotify's official page on the web API](https://developer.spotify.com/documentation/web-api/)

[web API libraries that demonstrate the capabilites of the web API](https://developer.spotify.com/documentation/web-api/libraries/)

[API's reference](https://developer.spotify.com/documentation/web-api/reference/#/)

['Working with Playlists' official guide](https://developer.spotify.com/documentation/general/guides/working-with-playlists/)

[authorization code](https://developer.spotify.com/documentation/general/guides/authorization/code-flow/)

[How to use the Access Token](https://developer.spotify.com/documentation/general/guides/authorization/use-access-token/)

[public repository with examples](https://github.com/spotify/web-api-examples)

[helpful Youtube Video](https://www.youtube.com/watch?v=1vR3m0HupGI)
