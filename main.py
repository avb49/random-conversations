# from flask import Flask, redirect, render_template, request, url_for

from character import Character

ITERATIONS = 6


def append_text_to_file(text: str, file_name: str):
    """Appends a given text to a file"""
    with open(file_name, 'a', encoding="utf-8") as file:
        file.write(text)


def main():

    topic = "dogs"
    character1_name = "Dolly Parton"
    character2_name = "Harry Styles"

    character_1 = Character(
        name=character1_name,
        topic=topic,
        speaking_to=character2_name
    )
    character_2 = Character(
        name=character2_name,
        topic=topic,
        speaking_to=character1_name
    )
    characters = [character_1, character_2]
    current_character = characters[0]
    
    for iteration in range(ITERATIONS):

        message = current_character.get_response()
        message_format = f"{current_character.name}: {message}\n"
        print(message_format)

        # save message to both characters' message histories
        for character in characters:
            character.update_message_history(message)

        # save to chat history file
        append_text_to_file(
            text=message_format + "\n",
            file_name="conversation.txt"
        )

        # switch current character
        if iteration % 2 == 0:
            current_character = characters[1]
        else:
            current_character = characters[0]

if __name__ == "__main__":
    main()
    