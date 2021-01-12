# -*- coding: utf-8 -*-
"""
DSC 430 Assignment 1002

Scott Elmore
11/20/19

 “I have not given or received any
unauthorized assistance on this assignment”


YouTube Link : https://youtu.be/DSastmlstX4




Title:

    Game Theory with Monte Carlo and the NFL

Description of problem:

    Sundays in the fall, millions of NFL fans around the country partake
    in Pick'Em pools with their friends.  The objective of a Pick'Em pool
    is to pick the highest number of correct teams that win their games.
    You are in a league with 9 of your friends, you each put $100 into a pot,
    and now you want to take all their money and rub it in their faces.
    To do so, you need to come up with a model to prove that
    the teams you are selecting will in fact net you a profit over your friends.
    For sake of simpliticty, this week in the NFL there are 15 games being
    played, and the favored team  has a win probability of .6 in each game
    (Clearly, the Bears not being one of those teams).  Also, all of your
    friends are very risk averse people, meaning they chose to take the favorite
    in each game.  So, if you too take all favorites your expected profit would
    be $0, as you would all tie no matter the outcome.

    So you will want to choose upsets, and the number of upsets you're willing
    to choose can be maximized using a Monte Carlo simulation(1000 simulations)
    to prove that your maximizing your expected winnings.  Show me at what level
    of risk(0 to 1, each percent) for picking upsets you have maximized your winnings.
"""

import random


def getRandomGameOutcomes(num_games, p):
    """get the random outcomes given a number of games and probability,
    so set to 1 for favored team, 0 if underdog team"""

    teams = []
    for x in range(num_games):
        # assign based on if random is less than probability
        teams.append(int(random.random() < p))
    return teams


def playerCorrectPicks(player_teams, winning_teams):
    """get the score of player, number of correct picks"""
    score = 0
    for i, team in enumerate(player_teams):
        # pick is correct if your teams match the winnings teams
        score += int(player_teams[i] == winning_teams[i])
    return score


def myShare(scores, pot, num_players):
    """given the users score and the size of the pot and the number of players in the pool
    calculate the users winnings"""

    # subtract the entry fee
    entry = -(pot / num_players)

    # player wins
    if scores[0] == max(scores):
        return entry + (pot / scores.count(max(scores)))
    else:
        # player loses
        return entry


def main():
    """set up the game by iterating through each possible percent of risk you're willing
    to give to the favored team.  Then iterate through an appropraite number of iterations (1000)
    to get an answer for the average winnings given each risk level. Return the maximum level
    and the expected winnings"""

    # constants defined in problem
    num_players = 10
    num_games = 15
    win_prob = .6
    winning_pot = 1000

    # create dictionary of risk levels between 0 and 1 for every percent
    risk_levels = list(x / 100 for x in range(0, 101))
    risk_dict = dict.fromkeys(risk_levels, 0)

    # iterate through each risk level to calcualte winnings
    for risk_level in risk_dict:
        winnings = []
        iterations = 1000

        # iterate 10000 times to create a good monte carlo simulation
        for i in range(iterations):
            # keep track of score of each player in the pool (self is at index 0)
            scores = []

            # get the winning teams by passing in constant win probability
            winning_teams = getRandomGameOutcomes(num_games, win_prob)

            # get your teams based on the current risk level
            my_teams = getRandomGameOutcomes(num_games, risk_level)

            # get your correct picks by comparing your teams to the winning teams
            scores.append(playerCorrectPicks(my_teams, winning_teams))

            # competitors in this problem all take the favored team (meaning every team is 1)
            competitor_teams = [1] * num_games

            # append the score of each of the competitors (all the same)
            for player in range(num_players - 1):
                scores.append(playerCorrectPicks(
                    competitor_teams, winning_teams))

            # calculate and add winnings to a list
            winnings.append(myShare(scores, winning_pot, num_players))

        # get average winnings by dividing by # of iterations
        avg_winnings = sum(winnings) / iterations

        # set value of risk dictionary to the avg winnings
        risk_dict[risk_level] = avg_winnings

    print('Best possible upset risk level: {}\nExpected winnings: {}\n'.format(
        max(risk_dict, key=risk_dict.get), max(risk_dict.values())))


# call Main()
main()
