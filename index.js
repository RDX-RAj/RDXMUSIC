```
const { Telegraf } = require('telegraf');
const bot = new Telegraf(process.env.BOT_TOKEN);

bot.start((ctx) => {
  ctx.reply('Bot is running!');
});

bot.launch();

// RDX Music Bot Code
const fs = require('fs');
const ytdl = require('ytdl-core');
const ytSearch = require('yt-search');

bot.on('message', (msg) => {
  const chatId = (link unavailable);
  const args = msg.text.split(' ');

  if (args[0] === '!play') {
    const song = args[1];
    ytSearch(song, (err, res) => {
      if (err) {
        console.log(err);
      } else {
        const video = res.videos[0];
        const url = video.url;
        ytdl(url, { filter: 'audioonly' }, (err, stream) => {
          if (err) {
            console.log(err);
          } else {
            bot.telegram.sendAudio(chatId, stream, {
              caption: `Now playing: ${video.title}`,
            });
          }
        });
      }
    });
  }
});
```
