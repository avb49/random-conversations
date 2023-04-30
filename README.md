# Random conversations

This is a small project making use of the [OpenAI API](https://beta.openai.com/docs/quickstart) so you can create fascinating dialogues and explore what it may be like if two famous figures (fictional or real, past or present) sit down and have a good-old chat. Instructions to get set up can be found below.

All you need is:
1. Two people/characters in mind
2. A topic you would like them to talk about

#### This is a WIP
Please note that this code is currently a work-in-progress, and as such, it is not entirely robust or reliable yet.
In the near future I would like to deploy this in a [Flask](https://flask.palletsprojects.com/en/2.0.x/) app, 
perhaps on GitHub pages, so it can be used through a browser.

## Example conversations

[Here's Leonardo da Vinci and Paris Hilton talking about money](conversation_example2.txt):

>_Leonardo da Vinci: "Greetings fair Paris Hilton, I am Leonardo da Vinci, artist, inventor, and philosopher, and I must say that money is but a mere trifle in the grand scheme of life."_

>_Paris Hilton: "Hey Leo, like, it's me Paris Hilton, and money is like, literally the most important thing in the world, it's what makes the world go round."_

>_Leonardo da Vinci: "Ah, fair Paris Hilton, I see that you have been led astray by the temptations of material wealth. While money may have its uses, it is merely a tool to achieve greater things, such as knowledge, creativity, and personal fulfillment. One cannot buy happiness or true success with money alone, for those things must be earned through one's own endeavors and hard work."_

>_Paris Hilton: "Um, yeah, I totally get that, Leo. But, like, money can buy you designer clothes, private jets, and diamonds. And who needs personal fulfillment when you can have all that?"_

>_Leonardo da Vinci: "Ah, fair Paris Hilton, it seems that you are blinded by the superficial pleasures that money can provide. Allow me to remind you that material possessions are fleeting and do not bring true satisfaction or happiness. The pursuit of knowledge, creativity, and personal growth should be your true focus in life, for those things will provide you with lasting fulfillment and inner peace."_

>_Paris Hilton: "But Leo, like, have you seen my closet? Money can give you exclusivity, luxury, and a life beyond anyone's wildest dreams. Who needs fulfillment when you can have all that?"_

or

[Cristiano Ronaldo and Albert Einstein talking about cars](conversation_example.txt):
>_Cristiano Ronaldo: Yo, it's CR7 here and I gotta say I love cars, they're like a work of art on wheels._

>_Albert Einstein: Greetings, Cristiano Ronaldo. I am Albert Einstein, and while I am not particularly fond of cars, I do find the mechanics and physics behind them quite fascinating._

>_Cristiano Ronaldo: Hey, Albert! It's great to meet you. I completely understand your interest, but to me, it's not just about the mechanics, it's about the style, the speed, and the feeling of owning a top-notch car._

>_Albert Einstein: I certainly appreciate the aesthetics and the rush that driving a high-performance car provides, but I am more intrigued by the scientific principles that allow these machines to function, such as the laws of motion and thermodynamics._

>_Cristiano Ronaldo: I hear you, Albert, but for me, it's all about the passion and excitement that comes with owning a luxury car like my Bugatti Veyron or Lamborghini Aventador. The feeling of pushing the pedal to the metal and feeling the horsepower beneath me is indescribable. It's like having the world at your feet._

>_Albert Einstein: I can see why one would find such an experience exhilarating, Cristiano. However, it is important to remember that with great power comes great responsibility and we must always exercise caution and consideration when behind the wheel. Safety should always be a top priority._

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