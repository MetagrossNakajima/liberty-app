import os
import json
from PIL import Image

from utils.csv import read

ICON_SIZE = (70, 70)
ICON_START_X = 64
ICON_START_Y = 205
NEXT_COLUMN = 460
NEXT_ROW = 136
NEXT_POKEMON = 60

TWITTER_X = 120
TWITTER_Y = 120

PLAYER_NAME_X = 120
PLAYER_NAME_Y = 120

text_pokemons = [
    ["1000", "1001", "1002", "1003", "1004", "1005"],
    ["0999", "0998", "0997", "0996", "0995", "0994"],
    ["0995", "0993", "0993", "0992", "0992", "0991"],
    ["0989", "0988", "0987", "0986", "0985", "0984"],
    ["0939", "0938", "0937", "0936", "0935", "0974"],
    ["0969", "0968", "0967", "0966", "0965", "0964"],
    ["0969", "0968", "0967", "0966", "0965", "0964"],
    ["0969", "0968", "0967", "0966", "0965", "0964"],
]


def main(image_path: str, csv_path: str):
    json_file = open('pokedata/pokemons.json', 'r', encoding="utf8", )
    pokejson = json.load(json_file)

    result = read(csv_path)
    pokemons = []

    for user in result:
        pokemons.append([
            replace_name_to_id(pokejson, replace_name(poke))
            for poke in user if replace_name_to_id(pokejson, replace_name(poke))])

    create_image(image_path, pokemons)


def replace_name_to_id(pokejson: list[dict], name: str):
    for poke in pokejson:
        if poke["ja"] == name:
            return poke["key"]

    return None


def replace_name(pokename: str) -> str:
    names = (
        # ガチグマ
        ("暁ガチグマ", "ガチグマ(アカツキ)"),
        ("ガチグマ暁", "ガチグマ(アカツキ)"),
        ("ガチグマ", "ガチグマ(通常)"),
        # ウーラオス
        ("水ウーラオス", "ウーラオス(連撃)"),
        ("悪ウーラオス", "ウーラオス(一撃)"),
        ("ウーラオス水", "ウーラオス(連撃)"),
        ("ウーラオス悪", "ウーラオス(一撃)"),
        # コピペロス
        ("霊獣ランドロス", "ランドロス(霊獣)"),
        ("霊獣ボルトロス", "ボルトロス(霊獣)"),
        ("霊獣トルネロス", "トルネロス(霊獣)"),
        ("ランドロス霊獣", "ランドロス(霊獣)"),
        ("ボルトロス霊獣", "ボルトロス(霊獣)"),
        ("トルネロス霊獣", "トルネロス(霊獣)"),
        ("化身ランドロス", "ランドロス(化身)"),
        ("化身トルネロス", "トルネロス(化身)"),
        ("化身ボルトロス", "ボルトロス(化身)"),
        ("ランドロス化身", "ランドロス(化身)"),
        ("トルネロス化身", "トルネロス(化身)"),
        ("ボルトロス化身", "ボルトロス(化身)"),
        # オーガポン
        ("草オーガポン", "オーガポン(草)"),
        ("水オーガポン", "オーガポン(水)"),
        ("炎オーガポン", "オーガポン(炎)"),
        ("岩オーガポン", "オーガポン(岩)"),
        ("オーガポン草", "オーガポン(草)"),
        ("オーガポン水", "オーガポン(水)"),
        ("オーガポン炎", "オーガポン(炎)"),
        ("オーガポン岩", "オーガポン(岩)"),
    )

    for name in names:
        if (name[0] == pokename):
            return pokename.replace(name[0], name[1])

    return pokename


def create_image(image_path: str, pokemons: list[list[str]]):
    with Image.open(image_path).convert("RGBA") as baseImage:
        back_im = baseImage.copy()

        for i, pokeicons in enumerate(pokemons):
            for j, pokeicon in enumerate(pokeicons):
                icon_path = os.path.join("pokeicon", f"{pokeicon}.png")
                with Image.open(icon_path).convert("RGBA") as icon:
                    is_first_column = i < 4
                    resized_icon = icon.resize(ICON_SIZE)

                    x = ICON_START_X + NEXT_POKEMON * \
                        j + (0 if is_first_column else NEXT_COLUMN)

                    y_div = NEXT_ROW * \
                        i if is_first_column else NEXT_ROW * (i - 4)
                    y = ICON_START_Y + y_div

                    # im2のアルファチャンネルをマスクとして使用して貼り付ける
                    back_im.paste(resized_icon, (x, y), resized_icon)

        back_im.save('output.png', quality=100)


if __name__ == "__main__":
    image_path = os.path.join("result_image_editor", "image.png")
    csv_path = os.path.join("result_image_editor", "ResultTemplate.csv")
    main(image_path, csv_path)
