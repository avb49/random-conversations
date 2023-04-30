# Random conversations

This is an app using the [OpenAI API](https://beta.openai.com/docs/quickstart) and [Flask](https://flask.palletsprojects.com/en/2.0.x/) (TBC - not implemented yet) so you can create fascinating dialogues and explore what it might have been like if two famous figures (fictional or real) could have met and chatted. Follow the instructions below to get set up.

## Setup

1. If you don’t have Python installed, [install it from here](https://www.python.org/downloads/).

2. Clone this repository.

3. Navigate into the project directory:

   ```bash
   $ cd random-conversations
   ```

4. Create a new virtual environment:

   ```bash
   $ python -m venv venv
   $ . venv/bin/activate
   ```

5. Install the requirements:

   ```bash
   $ pip install -r requirements.txt
   ```

6. Make a copy of the example environment variables file:

   ```bash
   $ cp .env.example .env
   ```

7. Add your [OpenAI API key](https://beta.openai.com/account/api-keys) to the newly created `.env` file. This will be used for the app to do text completions.