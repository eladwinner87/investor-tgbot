# Welcome to Investor Telegram Bot - the ultimate tool for true sloth investors🦥

A self-hosted, compact Python application that uses a personal Telegram bot to automate and simplify Dollar-Cost Averaging (DCA) investments. It calculates investment amounts based on your salary, converts currencies, and accounts for commissions, providing you with the exact numbers to use in your brokerage app with zero mental energy wasted🙏

## ✨ Features

- **Automated Calculations**: Automatically calculates investment amounts based on a predefined portion of your salary.
- **DCA Strategy**: Simplifies your DCA investment strategy by providing consistent, accurate real-time numbers.
- **Multi-Stock Support**: Define which stocks to invest in and what percentage of the total amount to allocate to each.
You can optionally use either Israeli, American investment targets or both!
- **Real-time Currency Conversion**: Uses an exchange rate API to handle currency conversions accurately in real time.
- **Dockerized**: Includes a `Dockerfile` and `docker-compose.yml` for easy, containerized deployment.
- **Configurable**: All settings are managed via a simple `.env` file.

## 🏁 Getting Started

Follow these instructions to get your own instance of the bot up and running.

### Required Personal Credentials

Before you begin, you will need to gather the following credentials:

1.  **Telegram Bot Token**:
    - Open Telegram and chat with [@BotFather](https://t.me/BotFather).
    - Create a new bot to get an API Token.
    - **Important**: You must send a message to your new bot at least once for it to be able to contact you.

2.  **Telegram Chat ID**:
    - Chat with [@userinfobot](https://t.me/userinfobot) on Telegram to get your personal Chat ID.

3.  **Exchange Rate Service**:
    - Go to [exchangeratesapi.io](https://exchangeratesapi.io/) and sign up for a free API key.

### Installation

1.  **Clone the repository:**
    ```sh
    git clone <your-repository-url>
    cd investor-tgbot
    ```

2.  **Set up the configuration file:**
    - Rename the `.env.example` file. This file will hold all your secrets and settings.
    ```sh
    mv .env.example .env
    ```
    - Now, edit the `.env` file and fill in the credentials you gathered already, along with your investment preferences:
    1. What portion of your salary you wish to invest
    2. Which stocks to consider and what portion of the total amount to invest in each
    3. For how long should the bot session run before shutting down
    4. Modify the logs directory for stroing your investments if you want

---

## 🚀 Usage

You can now run the bot on a Docker container or directly using Python.

### Method 1: Running with Docker (Recommended)

1.  **Build and run the container:**
    ```sh
    docker-compose up --build
    ```
2.  The bot will start, and you will be prompted on Telegram for your latest salary.

### Method 2: Running Directly with Python

1.  **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

2.  **Run the bot:**
    ```sh
    python bot.py
    ```

---

## 🤖 Automating with Cronjob

For true "lazy investor" automation, you may schedule the bot to run periodically using a tool like `cron` on linux or `Task Scheduler` on Windows.

For example, to run the bot on the first day of every month, you could add the following to your crontab:

```cron
0 17 4 * * docker-compose -f /path/to/your/investor-tgbot up --build
```
This command will navigate to your project directory and launch the bot at 5 PM on the 4th of every month.
