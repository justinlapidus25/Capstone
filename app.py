import streamlit as st
import pickle
import pandas as pd
from PIL import Image
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler



im = Image.open('sdfadsfga.png')
st.set_page_config(page_title="Hey Now! Are You an Allstar?", page_icon = im,layout="wide")

NBAstats = pd.read_csv('Data Nba/NBA_Dataset.csv')
RAPTOR = pd.read_csv('Untitled Folder/archive (9)/historical_RAPTOR_by_player.csv')

NBAstats1 = NBAstats.set_index('player')
NBAstats1.fillna(0)
NBAstats2= NBAstats1.reset_index()

RAPTOR1 = RAPTOR.drop(columns=['pace_impact', 'player_id', 'predator_total', 'predator_defense', 'predator_offense', 'poss', 'war_total', 'mp', 'war_playoffs', 'war_reg_season'])

RaptorFinal = pd.merge(NBAstats1, RAPTOR1, left_on=['player', 'season'], right_on=['player_name', 'season'], how='left')
RaptorFinal = RaptorFinal.dropna()

Allstar_2002= pd.read_csv('Untitled Folder/archive (9)/2002-03 NBA - Sheet1.csv')
Allstar_2003= pd.read_csv('Untitled Folder/archive (9)/2003-04 NBA - Sheet1.csv')
Allstar_2004= pd.read_csv('Untitled Folder/archive (9)/2004-05 NBA - Sheet1 (1).csv')
Allstar_2005= pd.read_csv('Untitled Folder/archive (9)/2005-06 NBA - Sheet1.csv')
Allstar_2006= pd.read_csv('Untitled Folder/archive (9)/2006-07 NBA - Sheet1.csv')
Allstar_2007= pd.read_csv('Untitled Folder/archive (9)/2007-08 NBA - Sheet1.csv')
Allstar_2008= pd.read_csv('Untitled Folder/archive (9)/2008-09 NBA - Sheet1.csv')
Allstar_2009= pd.read_csv('Untitled Folder/archive (9)/2009-10 NBA - Sheet1.csv')
Allstar_2010= pd.read_csv('Untitled Folder/archive (9)/2010-11 NBA - Sheet1.csv')
Allstar_2011= pd.read_csv('Untitled Folder/archive (9)/2010-11 NBA - Sheet1.csv')
Allstar_2012= pd.read_csv('Untitled Folder/archive (9)/2011-12 NBA - Sheet1.csv')
Allstar_2013= pd.read_csv('Untitled Folder/archive (9)/2012-13 NBA - Sheet1.csv')
Allstar_2014= pd.read_csv('Untitled Folder/archive (9)/2013-14 NBA - Sheet1.csv')
Allstar_2015= pd.read_csv('Untitled Folder/archive (9)/2014-15 NBA - Sheet1 (1).csv')
Allstar_2016= pd.read_csv('Untitled Folder/archive (9)/2015-16 NBA - Sheet1.csv')
Allstar_2017= pd.read_csv('Untitled Folder/archive (9)/2016-17 NBA - Sheet1.csv')
Allstar_2018= pd.read_csv('Untitled Folder/archive (9)/2017-18 NBA - Sheet1.csv')
Allstar_2019= pd.read_csv('Untitled Folder/archive (9)/2018-19 NBA - Sheet1 (1).csv')
Allstar_2020= pd.read_csv('Untitled Folder/archive (9)/2019-20 NBA - Sheet1.csv')
Allstar_2021= pd.read_csv('Untitled Folder/archive (9)/2020-21 NBA - Sheet1.csv')
Allstar_2022= pd.read_csv('Untitled Folder/archive (9)/2021-22 NBA - Sheet1.csv')


Allstar_2002['Year'] =2002
Allstar_2003['Year'] =2003
Allstar_2004['Year']=2004
Allstar_2005['Year']=2005
Allstar_2006['Year']=2006
Allstar_2007['Year']=2007
Allstar_2008['Year']=2008
Allstar_2009['Year']=2009
Allstar_2010['Year']=2010
Allstar_2011['Year']=2011
Allstar_2012['Year']=2012
Allstar_2013['Year']=2013
Allstar_2014['Year']=2014
Allstar_2015['Year']=2015
Allstar_2016['Year']=2016
Allstar_2017['Year']=2017
Allstar_2018['Year']=2018
Allstar_2019['Year']=2019
Allstar_2020['Year']=2020
Allstar_2021['Year']=2021
Allstar_2022['Year']=2022

allstar_combined = pd.concat([
    Allstar_2002, Allstar_2003, Allstar_2004,Allstar_2005,Allstar_2006,Allstar_2007,Allstar_2008,Allstar_2009,Allstar_2010,Allstar_2011,Allstar_2012,Allstar_2013,Allstar_2014,Allstar_2015,Allstar_2016,Allstar_2017,Allstar_2018,Allstar_2019,Allstar_2020,Allstar_2021,Allstar_2022] , ignore_index=True)
def was_allstar(player, year):
    return player in allstar_combined[allstar_combined['Year'] == year]['Player'].values

allstar_combined['Was_Allstar'] = allstar_combined.apply(lambda row: was_allstar(row['Player'], row['Year']), axis=1)
columns_to_drop = ['Pos', '3P%', '2P%', 'FT%', 'Tm', '3P', '3PA', '2PA', '2P', 'eFG%', 'FT', 'FTA', 'ORB', 'G', 'GS', 'MP', 'FG', 'FGA', 'FG%', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']

allstar_combined.drop(columns=columns_to_drop, inplace=True)

merged_df = pd.merge(NBAstats2, allstar_combined, left_on=['player', 'season'], right_on=['Player', 'Year'], how='left')
merged_df1 = merged_df.drop(columns=['Player', 'Age']) 

merged_df1['Year'] = merged_df['season'].copy()

merged_df1_modified = merged_df1.copy()

merged_df1_modified['Was_Allstar'] = merged_df1_modified['Was_Allstar'].fillna(False)

Finaldf= merged_df1_modified.dropna()

RAPTOR= pd.read_csv('Untitled Folder/archive (9)/historical_RAPTOR_by_player.csv')

RAPTOR1= RAPTOR.drop(columns=['pace_impact','player_id','predator_total','predator_defense','predator_offense','poss','war_total','mp','war_playoffs','war_reg_season'])


RaptorFinal = pd.merge(Finaldf, RAPTOR1, left_on=['player', 'season'], right_on=['player_name', 'season'], how='left')
    
RaptorFinal.dropna()

RaptorFinal = RaptorFinal.dropna()
y = RaptorFinal.reset_index()["Was_Allstar"]
X = RaptorFinal.drop("Was_Allstar", axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
X_test_numerical = X_test.select_dtypes(["int64", "float64"]).copy()
X_train_numerical = X_train.select_dtypes(["int64", "float64"]).copy()

scaler = MinMaxScaler()


X_test_scaled = pd.DataFrame(
    scaler.fit_transform(X_test_numerical),
    index=X_test_numerical.index,
    columns=X_test_numerical.columns
)


scaler = MinMaxScaler()

X_train_scaled = pd.DataFrame(
    scaler.fit_transform(X_train_numerical),
    index=X_train_numerical.index,
    columns=X_train_numerical.columns
)
 




with open('gridsearch.pkl', 'rb') as file:
    loaded_gridsearch = pickle.load(file)

predicted_labels = loaded_gridsearch.predict(X_test_scaled)



st.title('Hey Now! Your\'e an Allstar?')
image = Image.open('nbaasg-feat1.jpeg')
st.image(image, caption='Allstars Through Time')




RaptorFinal.dropna()


def get_teams_by_year(selected_year):
    if selected_year < 2023:
        return RaptorFinal[RaptorFinal['season'] == selected_year]['team_id'].unique()
    else: 
        return RaptorFinal['team_id'].unique()

        




year_options = list(range(2002, 2023))  
selected_year = st.sidebar.selectbox('Select Year', year_options, key='year')
selected_team = st.sidebar.selectbox('Select Team', get_teams_by_year(selected_year), key=hash('team'))

spec_player = st.sidebar.text_input('if player not listed put player name here')
def get_player_by_year(selected_year, selected_team):
    if selected_year < 2023:
        return RaptorFinal[(RaptorFinal['season'] == selected_year  )& (RaptorFinal['team_id'] == selected_team)]['player_name'].unique()
    

filtered_players = get_player_by_year(selected_year, selected_team)
selected_player = st.sidebar.selectbox('Select Player', get_player_by_year(selected_year, selected_team), key=hash('player'))



st.subheader('This application will tell you whether a player was an allstar or not!')

selected_player_stats = RaptorFinal[(RaptorFinal['player_name'] == selected_player) & (RaptorFinal['season'] == selected_year) & (RaptorFinal['team_id'] == selected_team)]

st.header('Player Stats for Selected Year and Team')
st.write(selected_player_stats[['pos', 'raptor_total', 'season', 'age', 'pts_per_g', 'orb_per_g', 'trb_per_g', 'ast_per_g', 'stl_per_g', 'blk_per_g']])

prediction = RaptorFinal[(RaptorFinal['player_name'] == selected_player) & (RaptorFinal['season'] == selected_year) & (RaptorFinal['team_id'] == selected_team)]['Was_Allstar'].values[0]
if prediction == 1:
    st.header(" All-Star")
else:
    st.header(" Not an All-Star")



player= RaptorFinal['player']
def player(selected_year):
    if selected_year < 2023:
        return RaptorFinal[RaptorFinal['player'] == selected_year]['player'].unique()
   
def season(selected_year):
    if selected_year < 2023:
        return RaptorFinal[RaptorFinal['season'] == selected_year]['team_id'].unique()

    
pos= RaptorFinal['pos']
age= RaptorFinal['age']
team_id= RaptorFinal['team_id']
g= RaptorFinal['g']
gs= RaptorFinal['gs']
mp_per_g= RaptorFinal['mp_per_g']
fg_per_g= RaptorFinal['fg_per_g']
fga_per_g= RaptorFinal['fga_per_g']
fg_pct= RaptorFinal['fg_pct']
fg3_per_g= RaptorFinal['fg3_per_g']
fg3a_per_g= RaptorFinal['fg3a_per_g']
fg3_pct= RaptorFinal['fg3_pct']
fg2_per_g= RaptorFinal['fg2_per_g']
fg2a_per_g= RaptorFinal['fg2a_per_g']
fg2_pct= RaptorFinal['fg2_pct']
efg_pct= RaptorFinal['efg_pct']
ft_per_g= RaptorFinal['ft_per_g']
fta_per_g= RaptorFinal['fta_per_g']
ft_pct= RaptorFinal['ft_pct']
orb_per_g= RaptorFinal['orb_per_g']
drb_per_g= RaptorFinal['drb_per_g']
trb_per_g= RaptorFinal['trb_per_g']
ast_per_g= RaptorFinal['ast_per_g']
stl_per_g= RaptorFinal['stl_per_g']
blk_per_g= RaptorFinal['blk_per_g']
tov_per_g= RaptorFinal['tov_per_g']
pf_per_g= RaptorFinal['pf_per_g']
pts_per_g= RaptorFinal['pts_per_g']
mp= RaptorFinal['mp']
per= RaptorFinal['per']
ts_pct= RaptorFinal['ts_pct']
fg3a_per_fga_pct= RaptorFinal['fg3a_per_fga_pct']
fta_per_fga_pct= RaptorFinal['fta_per_fga_pct']
orb_pct= RaptorFinal['orb_pct']
drb_pct= RaptorFinal['drb_pct']
trb_pct=  RaptorFinal['trb_pct']
ast_pct= RaptorFinal['ast_pct']
stl_pct= RaptorFinal['stl_pct']
blk_pct= RaptorFinal['blk_pct']
tov_pct= RaptorFinal['tov_pct']
usg_pct= RaptorFinal['usg_pct']
ows= RaptorFinal['ows']
dws= RaptorFinal['dws']
ws= RaptorFinal['ws']
ws_per_48= RaptorFinal['ws_per_48']
obpm= RaptorFinal['obpm']
dbpm= RaptorFinal['dbpm']
bpm= RaptorFinal['bpm']
vorp= RaptorFinal['vorp']
award_share= RaptorFinal['award_share']
mov= RaptorFinal['mov']
mov_adj= RaptorFinal['mov_adj']
win_loss_pct= RaptorFinal['win_loss_pct']
raptor_offense= RaptorFinal['raptor_offense']
raptor_defense= RaptorFinal['raptor_defense']
raptor_total= RaptorFinal['raptor_total']




