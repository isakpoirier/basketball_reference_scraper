from libs.basketball_reference_scraper.teams import get_roster, get_team_stats, get_opp_stats, get_roster_stats, get_team_misc
from libs.basketball_reference_scraper.players import get_stats, get_game_logs
import pandas as pd

def scrape_data(output_loc, years):
    
    teams = [
        'ATL','BOS','CHO','CLE','DAL','PHO','NOP','NYK','PHI','CHI','POR',
        'SAS','MIN','TOR','WAS','ORL','UTA','OKC','MEM','IND','MIA','BRK',
        'GSW','HOU','DEN','SAC','LAC','LAL','DET','MIL']


    game_logs = pd.DataFrame()
    rosters = pd.DataFrame()
    team_stats_df = pd.DataFrame()
    opp_stats_df = pd.DataFrame()

    try:
        for team in teams:
            for year in years:
                print(team + ' --> ' + str(year))
                roster = get_roster(team, year)
                rosters = pd.concat([rosters, roster])
                team_stats = get_team_stats(team, year, data_format='PER_GAME')
                team_stats_df = pd.concat([team_stats_df, team_stats])
                opp_stats = get_opp_stats(team, year, data_format='PER_GAME')
                opp_stats_df = pd.concat([opp_stats_df, opp_stats])
                for player in roster['PLAYER']:
                    print(player)
                    try:
                        player_log = get_game_logs(player, year, playoffs = False)
                        game_logs = pd.concat([game_logs, player_log])
                    except:
                        pass
    except:
        pass
    game_logs.to_csv(output_loc[0], index = False)
    rosters.to_csv(output_loc[1], index = False)
    team_stats_df.to_csv(output_loc[2], index = False)
    opp_stats_df.to_csv(output_loc[3], index = False)



# game_logs = get_game_logs(player, 2023, playoffs = False)
# # s = get_team_misc('GSW', 2019)


# s = get_stats('Stephen Curry', stat_type='PER_GAME', playoffs=False, career=False)
# print(s)

# df = get_game_logs('LeBron James', 2022, playoffs=False)
# print(df)

# from basketball_reference_scraper.seasons import get_schedule, get_standings

# s = get_schedule(2018, playoffs=False)
# print(s)

# s = get_standings(date='2020-01-06')
# print(s)

# from basketball_reference_scraper.box_scores import get_box_scores

# s = get_box_scores('2020-01-13', 'CHI', 'BOS', period='GAME', stat_type='BASIC')
# print(s)


# # # play-by-play
# # from basketball_reference_scraper.pbp import get_pbp

# # s = get_pbp('2020-01-13', 'CHI', 'BOS')
# # print(s)

# # from basketball_reference_scraper.shot_charts import get_shot_chart

# # s = get_shot_chart('2020-01-13', 'CHI', 'BOS')
# # print(s)

# # from basketball_reference_scraper.injury_report import get_injury_report

# # s = get_injury_report()
# # print(s)

# from basketball_reference_scraper.players import get_game_logs, get_player_headshot

# df = get_game_logs('Pau Gasol', 2010, playoffs=False)
# print(df)

