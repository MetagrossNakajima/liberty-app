from bs4 import BeautifulSoup
import os


"""
# インターネット大会順位ダウンロードスクリプト

★★★使い方★★★

1. 次のサイトへアクセス
https://resource.pokemon-home.com/battledata/t_internetcompetition.html?r=474277
2. ダウンロードしたい大会ページへアクセス
3. ページを右クリックして「名前をつけて保存」を選択
4. liberty-appディレクトリ配下にダウンロードしたファイルを保存
5. ↓のHTML_FILENAMEのファイル名をダウンロードしたファイル名に変更
"""

HTML_FILENAME = "Internet Competition.html"


def main(path: str):

    # ファイルを読み込む
    with open(path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
        user_names = soup.find_all('div', class_='userName')
        ranks = soup.find_all('div', class_='rankText')
        points = soup.find_all('div', class_='point')
        for user, rank, point in zip(user_names, ranks, points):
            # 出力フォーマットを変更したい場合はここを変更
            print(f"{rank.text},{user.text},{int(float(point.text))}")


if __name__ == "__main__":
    path = os.path.join(os.path.dirname(__file__), HTML_FILENAME)
    main(path)
