class DictGamesUtils:
    @staticmethod
    def sort_check(dict_game):
        special_dict_game = {}
        for game, price in dict_game.items():
            special_dict_game[game] = float(price[:-4].replace(",", "."))

        temp_price = 1000000000000000000000

        for price in special_dict_game.values():
            if price <= temp_price:
                temp_price = price
            else:
                return False
        return True
