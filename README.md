### Welcome to Investor telegram bot - the ultimate tool for true sloths investors!

This project includes a self-hosted, compact python application powered by a personal telegram bot,
to simplify and automate your DCA style investment sparing you the headache of sitting every month,
calculating, converting currencies, considering commissions -
and just provide you with accurate, real-time numbers
leaving you only to insert them straight into your broker app with zero mental energy wasted🙏

# How to configure:

Clone this repository,

Everything you need to set for the bot to work is completely controlled through
the ```.env``` file (remove the .example postfix to activate it), where you declare all your personal preferences:

1. What portion of your salary you wish to invest
2. Which stocks to consider and what portion of the total amount to invest in each
3. For how long should the bot session run before shutting down
4. modifying the logs directory for stroing your investments if you want

## Required Personal Credentials:

# Telegram
* Go to @BotFather in Telegram, create a bot and an API Token for it and keep them

* Get your personal telegram chat id from @userinfobot

* IMPORTANT! in order to let your bot send you messages, it's neccesary for you to send it a message first on the first time, so after creation,look for it on telegram and start it. 

# Exchange Rate Service
Go to https://exchangeratesapi.io/ and generate yourself a free API key

After finishing setting your .env file, you can easily run your bot by simply running the following command:

```docker compose -f your-cloned-repo-path/docker-compose.yml up --build```

then you will get prompted for your latest salary on telegram

You may want to run it periodically by a cronjob or such tools to automate and simplify your DCA investment 😀