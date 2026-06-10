# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 15:20:04 2026

@author: LENOVO
"""

class Game:
    def __init__(self, name, genre, age_rating, duration, rating):
        self.name = name
        self.genre = genre.lower()
        self.age_rating = age_rating
        self.duration = duration
        self.rating = rating

    def __str__(self):
        return "{} | Genre: {} | {}+ | Duration: {} hours | Rating: {}".format(
            self.name, self.genre, self.age_rating, self.duration, self.rating
        )


class User:
    def __init__(self, name, age, preferred_genre, max_duration):
        self.name = name
        self.age = age
        self.preferred_genre = preferred_genre.lower()
        self.max_duration = max_duration
        self.library = []

    def add_game(self, game):
        self.library.append(game)

    def show_library(self):
        if not self.library:
            print("Library is empty.")
        else:
            print("\n--- Your Library ---")
            for game in self.library:
                print("-", game)


class GameSystem:
    def __init__(self):
        self.games = []

    def add_game(self, game):
        self.games.append(game)

    def show_all_games(self):
        print("\n--- All Games ---")
        for game in self.games:
            print(game)

    def recommend(self, user):
        suitable = []

        for game in self.games:
            if (game.age_rating <= user.age and
                game.genre == user.preferred_genre and
                game.duration <= user.max_duration):
                suitable.append(game)

        suitable.sort(key=lambda x: x.rating, reverse=True)
        return suitable

    def top_games(self):
        return sorted(self.games, key=lambda x: x.rating, reverse=True)[:3]


system = GameSystem()

system.add_game(Game("The Witcher 3", "RPG", 18, 50, 9.8))
system.add_game(Game("FIFA 23", "Sports", 3, 5, 7.5))
system.add_game(Game("Minecraft", "Sandbox", 7, 100, 9.0))
system.add_game(Game("Hades", "Action", 13, 20, 9.2))

print("=== Welcome to the Game Recommendation System ===")

name = input("Name: ")
age = int(input("Age: "))
genre = input("Preferred genre: ")
max_duration = int(input("Max game duration (hours): "))

user = User(name, age, genre, max_duration)

while True:
    print("\n--- MENU ---")
    print("1. Game Recommendations")
    print("2. Show All Games")
    print("3. Top Games")
    print("4. Add to Library")
    print("5. Show Library")
    print("6. Exit")

    choice = input("Choose: ")

    if choice == "1":
        recommendations = system.recommend(user)

        if recommendations:
            print("\nRecommended Games:")
            i = 0
            for game in recommendations:
                print(i, "-", game)
                i += 1
        else:
            print("No suitable games found.")

    elif choice == "2":
        system.show_all_games()

    elif choice == "3":
        print("\nTop Games:")
        for game in system.top_games():
            print("-", game)

    elif choice == "4":
        system.show_all_games()
        index = int(input("Enter game number to add: "))

        try:
            game = system.games[index]
            user.add_game(game)
            print("Added.")
        except:
            print("Invalid selection.")

    elif choice == "5":
        user.show_library()

    elif choice == "6":
        print("Exiting...")
        break

    else:
        print("Invalid choice.")
        
        