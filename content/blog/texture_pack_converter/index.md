# Texture Pack Converter

[< Back Home](/)

## Problem

I like Luanti more than Minecraft, but I don't usually like the way Luanti games look.

## Solution

What if I could just use the Minecraft texture packs I like in Luanti games? There is a Luanti game called Mineclonia that is very similar. I could make a tool that takes texture files from Minecraft packs and make a Mineclonia-compatible pack. I didn't know much programming, but that should only take a month or so, right?

Before I began, I started checking if this kind of tool already existed. It did, and it was pinned on the forum: [Forum Link](https://forum.luanti.org/viewtopic.php?t=14283). I didn't like this tool. It was a shell script that required [ImageMagick](https://imagemagick.org) to be installed. It probably still works, but I really wanted something better.

I decided to write a new script for converting textures in [the V language](https://vlang.io/). I picked V because it is easy to cross compile, easy to understand, and V files can run as script files easily. That script is "available" on [Notabug](https://notabug.org/). At the time of writing, Notabug is often down due to AI scrapers DDoSing it. That script basically was just a bunch of copy and paste operations. It had no real way of editing the textures to abide by Mineclonia's expectations. Image editing with code was a bit too advanced for me, so I stopped making progress.

Eventually, I decided to try again using [the Go language](https://go.dev/). I mainly picked it because I found this image editing library called [Imaging](https://pkg.go.dev/github.com/disintegration/imaging). This library was all that I would need. Go is also a much more used language, so it was easy to look up solutions to common problems I was running into.

## Writing out the edits was time-consuming.

There are many differences in how the textures work. I tried to avoid "just eyeballing it" as much as possible. For the chests in particular, I'd make versions of textures that had extra gradients of color or extra marks on them to check exactly how all the parts fit together. Comparing how Minecraft and Mineclonia map things is not usually necessary, but sometimes I would have the two games open next to each other just to see what needed adjusting.

See below, I used the chests from one of the Faithful texture packs.

![Chest Debug Rectangles](/images/CTC_Screenshots/Chest_Debug_Rectangles.png)

### Conclusion

Go is easy. It might be the easiest practical programming language to learn. I used [Codingame](https://www.codingame.com/) and some [Codewars](https://www.codewars.com/) to learn more. Eventually, [Boot.dev](https://www.boot.dev/) had a discount that I liked, and I started paying for their courses. I am significantly better at coding now, but some of the old code from before I got through their courses is still in my converter project. I wish I could quickly reorganise it, but that will have to wait.

### This post is not finished. I will continue writing at a future time.


