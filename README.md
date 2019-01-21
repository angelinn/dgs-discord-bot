# Repost Guardian - a discord bot

## About
**Discord Guardian** is a discord bot that prevents images from being reposted.

Its main purpose is to prevent memes from being spammed and reposted in the **#meme** channel.

## How does it work?
The application gets the hashes of the images and saves them in memory and in a file. Each time the same hash has appeared, the message with the image is deleted.

## Commands
The commands are prefixed with the `r!` prefix.
* `r!about` - displays information about the bot
* `r!off` - turns off the repost protection
* `r!on` - turns on the repost protection

The `on` and `off` commands are only available to users with the `Administrato` permisson.

## Permissions
The bot needs permissions **10240**, which are:
* Read messages
* Manage messages

## License
The bot is licensed under the MIT license.
