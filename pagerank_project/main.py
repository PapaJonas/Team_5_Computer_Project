"""League table"""
import os
print(f"Current Working Directory: {os.getcwd()}")

import pagerank_read
import pagerank_algo
import pagerank_write
import visualize
import pagerank_cli
##################################################################################################

def main() -> None:
    """
    Main function to execute the tournament score processing.
    """
    # players_file = 'teams.csv' #
    # games_file = 'games.csv' #
    # filename = 'example.csv' #
    # pts_per_win = 3 #
    # pts_per_draw = 1 #
    # dumping = 0.15 #
    players_file, games_file, filename, pts_per_win, pts_per_draw, damping = pagerank_cli.cli()
    players = pagerank_read.read_players(players_file)
    results = pagerank_read.read_games(games_file)
    information = pagerank_read.update_players(results, players, pts_per_win, pts_per_draw)

    n = len(players)
    connections = pagerank_algo.connect_list(players, results)
    rank = pagerank_algo.rank_return(n, connections, damping)

    pagerank_write.write_function(filename, information, rank)
    visualize.graph_create(filename, games_file)

if __name__ == "__main__":
    main()
